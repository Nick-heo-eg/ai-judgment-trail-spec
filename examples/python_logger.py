"""
Plain Python Logger Example

Minimal AJT logging with standard library only.
No frameworks, no dependencies.
"""

import logging
import json
from datetime import datetime, timezone
from uuid import uuid4

# Configure standard Python logger
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger("ajt")


def log_ai_judgment(
    model: str,
    decision: str,
    risk_level: str,
    policy_version: str,
    human_in_loop: bool = False,
    session_id: str = None
):
    """
    Log an AI judgment in AJT format.

    This is just a structured log line. No enforcement, no blocking.
    """
    ajt_record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "run_id": str(uuid4()),
        "model": model,
        "decision": decision,
        "risk_level": risk_level,
        "human_in_loop": human_in_loop,
        "policy_version": policy_version,
        "app_version": "1.0.0",
        "session_id": session_id or str(uuid4())
    }

    # Just log it
    logger.info(json.dumps(ajt_record))


# Example usage
if __name__ == "__main__":
    # Example 1: Simple AI call
    log_ai_judgment(
        model="gpt-4",
        decision="allow",
        risk_level="low",
        policy_version="v1.0"
    )

    # Example 2: High-risk decision with human review
    log_ai_judgment(
        model="claude-3-opus",
        decision="escalate",
        risk_level="high",
        policy_version="v1.0",
        human_in_loop=True,
        session_id="user-session-abc123"
    )

    # Example 3: Blocked request
    log_ai_judgment(
        model="llama-2-70b",
        decision="block",
        risk_level="critical",
        policy_version="v1.0"
    )

    print("\n✅ Three AJT records logged above")
