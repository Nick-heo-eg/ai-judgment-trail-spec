# Why This Exists

AI Judgment Trail (AJT) exists to solve a problem that most systems only notice **after something goes wrong**.

When an AI system causes harm, confusion, or loss, the questions are rarely about performance.

They are about responsibility.

* Who allowed this output?
* Under which rules?
* Was this automatic, or did a human approve it?
* What boundary failed — if any?

Most AI systems cannot answer these questions cleanly.

Not because they are careless,
but because they were never designed to.

---

## The Core Problem

Modern AI systems are excellent at execution.

They generate outputs, route requests, optimize latency, and scale inference.
Observability tools help us understand **what happened**.

But when incidents occur, the critical question changes:

> **Why was this allowed to happen?**

Traditional logs and traces struggle here because responsibility is implicit:

* Scattered across configs
* Embedded in code paths
* Lost in dashboards or tickets
* Reconstructed after the fact

AJT exists to make responsibility **explicit at the moment of judgment**.

---

## Four Concepts That Define This Project

AJT is not a tool-first project.
It is a boundary-first project.

Everything here is built around four ideas.

---

### 1. STOP

STOP is not a failure.

STOP is a **valid outcome of judgment**, equal to allow.

If a system cannot stop, it does not have judgment — only execution.

AJT treats:

* `allow`
* `deny`
* `defer`
* `escalate`

as first-class decision outcomes, not errors.

---

### 2. Boundary

A boundary is not a prompt.
It is not a model.
It is not a heuristic.

A boundary defines **where authority ends**.

If something can bypass it silently, it is not a boundary.

AJT does not enforce boundaries.
It **records which boundary was in effect** when a decision was made.

---

### 3. Judgment Trail (AJT)

AJT is not:

* reasoning logs
* explanations
* chain-of-thought
* prompt storage

AJT is a **permission record**.

It answers:

* Which model acted
* Under which policy version
* With what risk classification
* With or without human involvement

Nothing more. Nothing less.

---

### 4. Before Execution

Most tools operate *after* execution:

* Metrics
* Errors
* Traces
* Audits

AJT focuses on the moment **before execution is allowed**.

This is where responsibility lives.

Once execution happens, reconstruction is already compromised.

---

## What This Is Not

AJT is deliberately **not**:

* A runtime enforcement framework
* A guardrail engine
* A compliance platform
* A visualization tool
* A replacement for OpenTelemetry or GRC systems

AJT is designed to **attach to existing stacks**, not compete with them.

If you already log structured JSON, you can emit AJT.

---

## Why This Exists Now (Even If You Don't Need It Yet)

Most teams do not need AJT today.

That is expected.

Historically, concepts like:

* Zero Trust
* SBOM
* Model Cards

only became mandatory **after major incidents**.

AJT exists early so that:

* the concept is available
* the schema is simple
* adoption is cheap
* responsibility does not need to be reverse-engineered later

---

## The Goal

AJT aims to become a small, boring, obvious thing:

> "Of course we log judgments."

If that sentence ever feels obvious,
this project has succeeded.

---

## Status

* Experimental
* Open specification
* OpenTelemetry-aligned
* Zero runtime impact
* Apache 2.0 licensed

This is a boundary, not a product.
