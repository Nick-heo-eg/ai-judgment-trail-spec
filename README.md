# AI Judgment Trail (AJT)

**Role:** Minimal vendor-neutral log schema for recording AI decision context before execution.

⚠️ **Status:** Draft Specification (Reference Only)

AJT defines trace semantics for AI decisions made prior to execution.
It does not provide enforcement, compliance guarantees, or runtime safety.

---

## Overview

AI systems are typically logged after execution.

AJT records the context of a decision **before execution occurs**, so that post-incident analysis can answer:

> Why was this decision allowed at that moment?

AJT structures decision traces. It does not control behavior.

---

## Judgment Minimal Definition (JMD)

An event qualifies as a judgment if:

1. Multiple outcome paths existed
2. At least one non-selected path was evaluated
3. The selected outcome was recorded as a choice among those paths

AJT records the context of that choice.

---

## Quickstart

```bash
git clone https://github.com/Nick-heo-eg/ai-judgment-trail-spec
cd ai-judgment-trail-spec
python3 examples/run_ajt_demo.py
```

The demo generates example decision traces (STOP / ALLOW) and writes them to `ajt_trace.jsonl`.

No LLM or external services are required.

---

## Core Schema (9 Required Fields)

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

Full schema definition: `schema/v0.1.json`

Everything else is optional.

---

## Field Summary

| Field          | Purpose                                         |
| -------------- | ----------------------------------------------- |
| timestamp      | When the decision was made (UTC)                |
| run_id         | Unique execution identifier                     |
| model          | Model used                                      |
| decision       | Decision outcome (e.g., allow, block, escalate) |
| risk_level     | Assessed risk level                             |
| human_in_loop  | Whether a human reviewed the decision           |
| policy_version | Decision policy version                         |
| app_version    | Application version                             |
| session_id     | Request/session identifier                      |

Note: `judgment` is derived from JMD conditions and must not be manually asserted.

---

## What AJT Is Not

* Not a policy enforcement mechanism
* Not a compliance framework
* Not a monitoring system
* Not a decision engine

AJT defines trace semantics only.

---

## Design Principles

* Minimal overhead (9 required fields)
* Vendor-neutral
* Compatible with existing observability stacks (e.g., OpenTelemetry)
* Suitable for audit and post-incident review
* Independent of model implementation

---

## Installation

There is nothing to install.

1. Copy `schema/v0.1.json`
2. Log one AJT record per AI decision
3. Query logs when explanation is required

---

## Scope

This repository defines schema and trace semantics only.

Execution logic, enforcement mechanisms, policy design, and runtime behavior belong outside this repository.

---

## Roadmap

* v0.1 — Core schema
* v0.2 — Optional extensions
* v1.0 — Stabilized specification

---

## License

Apache 2.0
