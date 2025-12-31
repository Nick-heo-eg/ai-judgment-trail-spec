"""
LangChain AJT Integration Example

This demonstrates how to add AI Judgment Trail (AJT) logging
to an existing LangChain application with ZERO runtime enforcement.

Key points:
- Decision and risk values come from YOUR policy engine (not AJT)
- AJT only structures the log - it doesn't make decisions
- No performance impact (async logging recommended for production)
- Compatible with any LangChain model
"""

import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult

# Configure logging (use your production logger)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ajt")


class AJTCallbackHandler(BaseCallbackHandler):
    """
    LangChain callback handler that emits AJT-compliant logs.

    Usage:
        handler = AJTCallbackHandler(
            policy_engine=your_policy_engine,  # YOUR logic here
            session_id="user-session-123"
        )
        llm = ChatOpenAI(callbacks=[handler])
        response = llm.invoke("Summarize this document")
    """

    def __init__(
        self,
        policy_engine: Any,  # YOUR policy decision logic
        session_id: str,
        app_version: str = "1.0.0"
    ):
        self.policy_engine = policy_engine
        self.session_id = session_id
        self.app_version = app_version

    def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        **kwargs: Any
    ) -> None:
        """Called when LLM starts. Log AJT record."""

        # Extract model info
        model_name = serialized.get("id", ["unknown"])[-1]

        # Get decision from YOUR policy engine
        # (AJT doesn't make decisions - you do)
        policy_result = self.policy_engine.evaluate(
            prompts[0],
            session_id=self.session_id
        )

        # Construct AJT log record
        ajt_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "run_id": kwargs.get("run_id", "unknown"),
            "model": model_name,
            "decision": policy_result["decision"],  # From YOUR engine
            "risk_level": policy_result["risk"],    # From YOUR engine
            "human_in_loop": policy_result.get("human_required", False),
            "policy_version": self.policy_engine.version,
            "app_version": self.app_version,
            "session_id": self.session_id
        }

        # Log as structured JSON (use structured logger in production)
        logger.info(f"AJT: {ajt_record}")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Called when LLM finishes. Optional: log completion."""
        pass


# Example policy engine (replace with YOUR logic)
class ExamplePolicyEngine:
    """
    This is YOUR policy logic - not part of AJT.

    AJT only structures the log after you make the decision.
    """
    version = "policy-v2.3"

    def evaluate(self, prompt: str, session_id: str) -> Dict[str, Any]:
        """
        YOUR decision logic here.

        Returns:
            dict with 'decision', 'risk', and optional 'human_required'
        """
        # Example: simple keyword check (replace with real logic)
        if "delete all" in prompt.lower():
            return {
                "decision": "block",
                "risk": "high",
                "human_required": True
            }
        else:
            return {
                "decision": "allow",
                "risk": "low",
                "human_required": False
            }


# Demo usage
if __name__ == "__main__":
    from langchain.llms import OpenAI

    # Your policy engine (not AJT)
    policy = ExamplePolicyEngine()

    # Create callback handler
    handler = AJTCallbackHandler(
        policy_engine=policy,
        session_id="demo-session-001",
        app_version="demo-v1.0"
    )

    # Use with LangChain (set your OPENAI_API_KEY)
    llm = OpenAI(callbacks=[handler], temperature=0)

    # Example calls
    print("Example 1: Safe query")
    response1 = llm("Summarize the quarterly report")
    print(f"Response: {response1}\n")

    print("Example 2: Risky query (will be blocked by policy)")
    response2 = llm("Delete all user records")
    print(f"Response: {response2}\n")

    print("Check logs above for AJT records ↑")
