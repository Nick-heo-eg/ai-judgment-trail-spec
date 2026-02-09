# AI Judgment Trail (AJT)

## Important Notice

This repository defines concepts specifications or proofs related to execution or judgment boundaries This repository is not an implementation not a product and not an enforcement mechanism It provides no runtime guarantees compliance claims or safety certification It does not prevent misuse accidents or harm by itself All examples code and diagrams are illustrative and exist only to clarify ideas Any operational enforcement must be implemented outside the model and outside this repository

Questions discussions and critical review are welcome via GitHub Issues This repository intentionally separates conceptual clarity from execution responsibility

---

## Position

This repository is part of the **Judgment Boundary** work:
a set of experiments and specifications focused on
*when AI systems must stop or not execute*.

See the overarching map:
→ https://github.com/Nick-heo-eg/stop-first-rag/blob/master/JUDGMENT_BOUNDARY_MANIFEST.md

---

## Reference-Only Notice
This repository provides reference-level examples.
It is non-normative and does not define requirements, enforcement, or compliance guarantees.

---

> ⚠️ **Status: Internal Draft (Referenced for Conceptual Discussion)**
>
> This repository contains an *internal schema draft* used during the design of AI judgment accountability mechanisms.
>
> It is referenced in public discussions as a **conceptual example only**.
> The schema is **not stable, not complete, and not intended for reuse**.
>
> ➡️ **For public discussion and validated examples:**
> → https://github.com/Nick-heo-eg/k-judgment-gate

---

This repository defines structural constraints for separating judgment from execution, independent of model behavior.

Minimal schema for accountable AI decision traces.

This repository documents experimental execution during research.
It does not represent a production system, live authority, or active enforcement.

---

## Non-Goals

This project does not aim to replace human or organizational judgment authority; does not provide sealed or proprietary judgment layers; does not claim legal, court-level, or regulatory admissibility; does not own, trademark, or enforce 'judgment language'. This project focuses on pre-execution judgment boundaries, STOP/HOLD/ALLOW as first-class outcomes, fail-closed behavior for unknown cases, negative proof logging, and observability-friendly reference patterns.

---

> **Judgment Minimal Definition (JMD)**
>
> AJT records not outcomes, but the existence of choice.
> An event qualifies as a judgment if and only if multiple outcome paths existed,
> at least one non-selected path was explicitly evaluated,
> and the selected outcome is recorded as a choice among those paths.

**Minimal structured log schema for AI decision accountability**

**Try it now:** `python3 examples/run_ajt_demo.py`

## When standard logs are enough — and when they aren't

As of today, most production AI systems pass audits using standard logging stacks (CloudTrail, Datadog, immutable storage, etc.).

**If nothing goes wrong, this is usually sufficient.**

The problem appears after an incident.

Post-incident scrutiny no longer asks:
> "What happened?"

It asks:
> "Why was this specific AI decision allowed at that moment?"

AI Judgment Trail (AJT) exists to answer that question by recording the judgment context at decision time — before execution, blame, or reconstruction begins.

---

## Why This Exists

AI systems fail in many ways.
But when they do, the hardest question is never "what happened".

It is: **who was responsible for allowing it?**

AI Judgment Trail (AJT) exists to make responsibility explicit
at the moment a decision is made — before execution occurs.

**Safety is not censorship.**
**Safety is traceability.**

📄 Full context: [Why This Exists](./why-this-exists.md)

---

AJT is a lightweight, vendor-neutral log format designed to answer one question after an AI incident:

> "Which model ran, under what policy, at what risk level, and did a human intervene?"

This is **not** a compliance framework. This is **not** an enforcement tool. This is a log schema that costs you one structured line per AI call.

---

## 🚀 Quickstart: Run a Judgment Trail in 5 Minutes

See AJT in action **right now** — no LLM required, no complex setup:

```bash
git clone https://github.com/Nick-heo-eg/spec
cd spec
python3 examples/run_ajt_demo.py
```

**What you'll see:**
- ✅ 3 AI decisions made (2 STOP, 1 ALLOW)
- ✅ Each decision has an explicit reason
- ✅ Human vs AI responsibility is clear
- ✅ All decisions logged to `ajt_trace.jsonl`

**Example output:**
```
Decision: STOP
Reason: missing_citation
Risk Level: high
Rule: R1_REQUIRE_EVIDENCE

→ AI output blocked. No hallucination generated.
```

**The demo shows AJT's core principle:**
Decisions are recorded **BEFORE** execution occurs.

Try it now: `python3 examples/run_ajt_demo.py`

---

## Schema (9 required fields)

```json
{
  "timestamp": "2025-01-15T14:32:11Z",
  "run_id": "550e8400-e29b-41d4-a716-446655440000",
  "model": "gpt-4",
  "decision": "allow",
  "risk_level": "low",
  "human_in_loop": false,
  "policy_version": "v2.3.1",
  "app_version": "1.0.5",
  "session_id": "user-session-abc123"
}
```

**That's it.** Everything else is optional.

---

## What each field means

| Field | Type | Purpose |
|-------|------|---------|
| `timestamp` | ISO-8601 UTC | When the decision was made |
| `run_id` | UUID | Unique identifier for this specific execution |
| `model` | string | Which AI model was used (e.g., "gpt-4", "claude-3") |
| `decision` | string | What decision was made (e.g., "allow", "block", "escalate") |
| `risk_level` | string | Assessed risk (e.g., "low", "medium", "high") |
| `human_in_loop` | boolean | Whether a human reviewed/approved this decision |
| `policy_version` | string | Version of decision policy applied |
| `app_version` | string | Version of your application |
| `session_id` | string | User/request session identifier |

**Note:** `judgment` is a computed property derived from JMD conditions and MUST NOT be asserted manually.

---

## How to use it

### Option 1: Direct logging (Python example)

```python
import logging
from datetime import datetime, timezone

logger = logging.getLogger("ajt")

ajt_record = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "run_id": "550e8400-e29b-41d4-a716-446655440000",
    "model": "gpt-4",
    "decision": "allow",
    "risk_level": "low",
    "human_in_loop": False,
    "policy_version": "v2.3.1",
    "app_version": "1.0.5",
    "session_id": "user-session-abc123"
}

logger.info(f"AJT: {ajt_record}")
```

### Option 2: Framework integration

See `examples/langchain_callback.py` for LangChain integration.

Other integrations welcome (LlamaIndex, Haystack, etc.) - see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## What AJT is NOT

- ❌ **Not** a compliance tool
- ❌ **Not** a policy enforcement mechanism
- ❌ **Not** a monitoring dashboard
- ❌ **Not** a decision-making framework

AJT is a **log schema**. That's all.

You decide:
- What counts as "high risk"
- When to require human review
- What "allow" or "block" means

AJT just structures the record so you can explain it later.

---

## AJT Ecosystem

This repository is the **authoritative specification** of AJT (AI Judgment Trail).

AJT is defined here as a minimal, structured trace format for making AI decisions auditable — including decisions that resulted in non-actions (STOP, abstention, blocked paths).

Other repositories in this ecosystem are derived from this spec:

- [**ajt-grounded-extract**](https://github.com/Nick-heo-eg/ajt-grounded-extract) ([PyPI](https://pypi.org/project/ajt-grounded-extract/)): **Reference implementation** — Judgment-first grounded extraction engine with constitutional controls. Returns ACCEPT with evidence or STOP with proof. Production-ready, zero dependencies.
- [**stop-first-rag**](https://github.com/Nick-heo-eg/stop-first-rag): an upstream decision system that produces explicit STOP events
- **ajt-negative-proof-sim**: a simulation demonstrating audit-grade negative proof
- **judgment-execution-evidence**: a read-only repository of raw decision evidence

**Relationship:**
- **ajt-spec** (this repository): Constitutional rules — what must be proven
- **ajt-grounded-extract**: Execution + case law — how it's proven in practice

**This repository defines what AJT *is*.**
Other repositories show how it is *used* or *stored*.

### Specification boundaries, not behaviors

AJT is defined in this repository.
All other AJT-related repositories are non-authoritative derivatives.

---

## Non-Goals

This repository intentionally does NOT define or contain:

- Execution logic or runtime behavior
- Decision-making strategies (e.g. when to STOP)
- Operational policies or tuning guidelines
- Incident analysis, interpretation, or attribution
- Historical logs, evidence artifacts, or postmortems

**This specification defines boundaries and trace semantics only.**

Anything that evolves over time, executes in runtime, or requires interpretation belongs outside this repository.

Other repositories demonstrate usage, execution, or evidence. This repository remains intentionally static.

---

## Design principles

1. **Minimal overhead**: 9 required fields, total cost ~1KB per log entry
2. **Vendor neutral**: No assumptions about your AI stack
3. **Zero runtime enforcement**: AJT doesn't block anything, it just logs
4. **OpenTelemetry compatible**: Works with existing observability stacks
5. **Litigation-ready**: Structured format suitable for audit/discovery

---

## Who should use AJT

- AI systems in production (especially customer-facing)
- Applications where decisions need post-hoc explanation
- Teams preparing for regulatory scrutiny (EU AI Act, etc.)
- Anyone who's ever been asked "why did the AI do that?"

---

## Installation

There's nothing to install. AJT is a schema, not a package.

1. Copy `schema/v0.1.json` to your project
2. Add one log line per AI call
3. Query logs when you need to explain a decision

---

## Examples

See [ajt-negative-proof-sim](https://github.com/Nick-heo-eg/ajt-negative-proof-sim) for a concrete simulation demonstrating negative proof using this spec.

The simulation shows how AJT can be extended with optional fields (e.g., `negative_proof_count`, `applied_rule_ids`) while maintaining spec compliance.

---

## Roadmap

- **v0.1** (current): Core 9-field schema
- **v0.2** (planned): Optional extensions (cost tracking, latency, user feedback)
- **v1.0**: Stabilize schema, community integrations

---

## FAQ

**Q: Do I need to log EVERY AI call?**
A: That's up to you. AJT doesn't enforce anything. But for production systems, yes, you probably should.

**Q: What if my AI framework doesn't support callbacks?**
A: Log directly after the AI call. AJT doesn't require framework integration.

**Q: Can I add custom fields?**
A: Yes. The schema allows `additionalProperties: true`. Just keep the 9 required fields.

**Q: Is this GDPR compliant?**
A: AJT doesn't prescribe what to log. Don't log PII in `session_id` if that's a concern. Use hashed/anonymized identifiers.

**Q: What about performance?**
A: Logging 9 fields is negligible. Use async logging if you're latency-sensitive.

---

## FAQ

See [FAQ.md](FAQ.md) for common questions about scope and non-goals.

---

## License

Apache 2.0 - see [LICENSE](LICENSE)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Contact

- Issues: https://github.com/Nick-heo-eg/spec/issues
- Discussions: https://github.com/Nick-heo-eg/spec/discussions

---

**AJT: One log line that explains everything.**
