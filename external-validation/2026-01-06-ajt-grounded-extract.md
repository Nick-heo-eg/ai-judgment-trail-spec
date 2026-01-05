# External Execution Instance: 2026-01-06

**Date**: 2026-01-06
**Event**: ajt-grounded-extract v0.1 published and executed

---

## Observed Execution

Repository **ajt-grounded-extract** was published as a public implementation at https://github.com/Nick-heo-eg/ajt-grounded-extract.

The system executed document extraction with the following observed behavior:
- STOP-first decision logic operational
- Evidence grounding to document spans (quote + byte offsets)
- Negative proof generation for STOP events

---

## Verified Facts

**STOP-First Execution**:
- Extraction halted when no candidates found (reason: `no_candidates_found`)
- Proof artifact generated: `{"searched": true, "candidates_found": 0}`

**Evidence-Grounded Extraction**:
- ACCEPT decisions included document span mapping
- Evidence structure: quote, start offset, end offset, line number

**Negative Proof Reproduction**:
- STOP events contained machine-readable proof objects
- Artifacts timestamped and hashed (SHA-256)

---

## Scope Exclusions

This observation does not claim:
- Specification changes in ajt-negative-proof-sim
- Addition of normative rules
- Direction change in design principles
- Endorsement or evaluation of implementation quality

---

## References

- Observed implementation: https://github.com/Nick-heo-eg/ajt-grounded-extract
- Reference system: https://github.com/anthropics/ajt-negative-proof-sim

---

**This record does not modify the specification; it documents an observed execution instance only.**
