# AI Judgment Trail (AJT)

**Minimal structured log schema for AI decision accountability**

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
