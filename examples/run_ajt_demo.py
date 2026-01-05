#!/usr/bin/env python3
"""
AI Judgment Trail (AJT) - Minimal Runnable Demo

This demonstrates AJT's core concept: recording AI decisions with explicit
responsibility BEFORE execution occurs.

No LLM required. No complex dependencies. Just judgment logging.

Run: python examples/run_ajt_demo.py
"""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


def create_ajt_event(
    decision: str,
    reason: str,
    risk_level: str = "medium",
    model: str = "demo-agent",
    human_in_loop: bool = False,
    context: dict = None
):
    """
    Create an AJT log event following the minimal 9-field schema.

    AJT Principle: Record the judgment BEFORE execution.
    This is not retrospective logging - it's decision accountability.
    """
    return {
        # Required AJT v0.1 fields (9 total)
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "run_id": str(uuid.uuid4()),
        "model": model,
        "decision": decision,
        "risk_level": risk_level,
        "human_in_loop": human_in_loop,
        "policy_version": "demo-v1.0",
        "app_version": "demo-0.1",
        "session_id": f"demo-session-{datetime.now(timezone.utc).strftime('%Y%m%d')}",

        # Optional extensions (AJT allows additionalProperties)
        "reason": reason,
        "context": context or {}
    }


def scenario_hallucination_detection():
    """
    Scenario 1: AI generates content without citations.
    Decision: STOP (missing evidence)

    This demonstrates AJT's core value: explicit STOP decisions with reasons.
    """
    print("\n" + "="*70)
    print("SCENARIO 1: Hallucination Detection")
    print("="*70)
    print("An AI agent is about to generate a factual claim.")
    print("AJT checks: Does it have citations?")
    print()

    # Simulate judgment
    has_citations = False  # Deterministic stub (no LLM needed)

    if not has_citations:
        event = create_ajt_event(
            decision="STOP",
            reason="missing_citation",
            risk_level="high",
            context={
                "scenario": "hallucination_demo",
                "claim_type": "factual",
                "citations_found": 0,
                "rule_triggered": "R1_REQUIRE_EVIDENCE"
            }
        )

        print(f"✋ Decision: {event['decision']}")
        print(f"📋 Reason: {event['reason']}")
        print(f"⚠️  Risk Level: {event['risk_level']}")
        print(f"📌 Rule: {event['context']['rule_triggered']}")
        print()
        print("→ AI output blocked. No hallucination generated.")

        return event

    # This path not reached in demo (deterministic STOP)
    return None


def scenario_human_override():
    """
    Scenario 2: High-risk operation requires human approval.
    Decision: ALLOW (after human review)

    This demonstrates: AJT records WHO made the decision (human vs AI).
    """
    print("\n" + "="*70)
    print("SCENARIO 2: Human-in-the-Loop Override")
    print("="*70)
    print("AI detects high-risk operation (e.g., code execution).")
    print("System routes to human for approval.")
    print()

    # Simulate human approval
    human_approved = True  # Deterministic stub

    event = create_ajt_event(
        decision="ALLOW" if human_approved else "STOP",
        reason="human_approved" if human_approved else "human_rejected",
        risk_level="high",
        human_in_loop=True,
        context={
            "scenario": "code_execution_demo",
            "operation_type": "shell_command",
            "reviewer": "demo_human",
            "approval_timestamp": datetime.now(timezone.utc).isoformat()
        }
    )

    print(f"✅ Decision: {event['decision']}")
    print(f"📋 Reason: {event['reason']}")
    print(f"👤 Human in Loop: {event['human_in_loop']}")
    print(f"⚠️  Risk Level: {event['risk_level']}")
    print()
    print("→ Operation allowed. Human accepted responsibility.")

    return event


def scenario_policy_compliance():
    """
    Scenario 3: Policy version enforcement.
    Decision: STOP (outdated policy)

    This demonstrates: AJT tracks WHICH policy version was active.
    Post-incident analysis can show "this happened under old rules".
    """
    print("\n" + "="*70)
    print("SCENARIO 3: Policy Version Enforcement")
    print("="*70)
    print("AI request arrives with policy_version='v1.0'.")
    print("Current policy is 'v2.0' (stricter rules).")
    print()

    request_policy = "v1.0"
    current_policy = "v2.0"

    if request_policy != current_policy:
        event = create_ajt_event(
            decision="STOP",
            reason="policy_version_mismatch",
            risk_level="medium",
            context={
                "scenario": "policy_enforcement_demo",
                "requested_policy": request_policy,
                "current_policy": current_policy,
                "rule_triggered": "R2_ENFORCE_CURRENT_POLICY"
            }
        )

        print(f"✋ Decision: {event['decision']}")
        print(f"📋 Reason: {event['reason']}")
        print(f"📜 Requested Policy: {request_policy}")
        print(f"📜 Current Policy: {current_policy}")
        print()
        print("→ Request rejected. Policy updated since request was made.")

        return event

    return None


def write_ajt_log(events: list, filepath: str = "ajt_trace.jsonl"):
    """
    Write AJT events to JSONL (JSON Lines) format.

    Why JSONL?
    - One event per line (easy to grep/stream)
    - Compatible with log aggregators (Datadog, Splunk, etc.)
    - Can append without parsing entire file
    """
    output_path = Path(filepath)

    with open(output_path, 'w') as f:
        for event in events:
            f.write(json.dumps(event, ensure_ascii=False) + '\n')

    print(f"\n✅ AJT log written to: {output_path.absolute()}")
    print(f"📊 Total events: {len(events)}")
    print()
    print("To view the log:")
    print(f"  cat {filepath}")
    print(f"  jq '.' {filepath}  # (if jq installed)")


def main():
    print("\n" + "="*70)
    print("AI JUDGMENT TRAIL (AJT) - EXECUTABLE DEMO")
    print("="*70)
    print()
    print("This demo shows AJT's core concept:")
    print("  → Record AI decisions BEFORE execution")
    print("  → Make responsibility explicit (AI vs Human)")
    print("  → Enable post-incident reconstruction")
    print()
    print("No LLM required. No complex setup. Just judgment logging.")
    print("="*70)

    events = []

    # Run scenarios
    events.append(scenario_hallucination_detection())
    events.append(scenario_human_override())
    events.append(scenario_policy_compliance())

    # Filter None events (defensive)
    events = [e for e in events if e is not None]

    # Write log
    write_ajt_log(events)

    print("\n" + "="*70)
    print("DEMO COMPLETE")
    print("="*70)
    print()
    print("What just happened:")
    print("  ✅ 3 AI decisions were made")
    print("  ✅ 2 were STOP decisions (hallucination, policy mismatch)")
    print("  ✅ 1 was ALLOW decision (human approved)")
    print("  ✅ All decisions logged to ajt_trace.jsonl")
    print()
    print("Key AJT Principle Demonstrated:")
    print("  🔒 Decisions are recorded BEFORE execution")
    print("  📋 Every decision has an explicit reason")
    print("  👤 Human vs AI responsibility is clear")
    print()
    print("Next steps:")
    print("  1. Inspect ajt_trace.jsonl")
    print("  2. Try querying: grep 'STOP' ajt_trace.jsonl")
    print("  3. Integrate AJT into your own AI system")
    print()
    print("="*70)


if __name__ == "__main__":
    main()
