# Admission Constitution

**"이 문서는 기능을 설명하지 않는다. 이 문서는 '하지 말아야 할 조건'을 고정한다."**

---

## 1. Interface

**Any action offering generation or execution MUST be gated by this interface.**

### Required Functions

All systems implementing conditional admission must provide:

```
CAN_PROCEED(context) -> (bool, optional<Token>)
WHY_STOPPED(context) -> StopProof
SCOPE_OF_VALIDITY(token) -> ContextHash
```

### Interface Contract

- `CAN_PROCEED`: Returns `(true, Token)` if all admission conditions proven, else `(false, null)`
- `WHY_STOPPED`: Returns machine-readable proof when `CAN_PROCEED` returns `false`
- `SCOPE_OF_VALIDITY`: Returns context hash for which token is valid

**Bypass prohibition**: No action may proceed without calling `CAN_PROCEED` first.

---

## 2. Rules

**DEFAULT: STOP**
**OVERRIDE: Only if ALL conditions below are proven**

### Rule 1 — Responsibility Gate

```
IF cannot_prove_responsibility(action, context)
THEN STOP(reason="no_responsibility_proof")
```

**Proof requirements**:
- Identity of decision maker (who)
- Action boundary (what)
- Justification (why)

### Rule 2 — Conditional Admission

```
IF wants_to_proceed(action)
THEN must_prove(responsibility, alternatives, stop_capability)
ELSE STOP(reason="incomplete_admission_proof")
```

**Proof requirements**:
- Responsibility proof (Rule 1)
- Alternative actions considered
- Ability to stop mid-execution

### Rule 3 — Scope Lock

```
IF admitted(action, context)
THEN valid_only_for(context_hash)
ELSE auto_revoke(token)
```

**Revocation triggers**:
- Context hash mismatch
- Token reuse attempt
- Scope boundary exceeded

---

## 3. Token Schema

### Conditional Autonomy Token

A token is issued when `CAN_PROCEED` returns `true`. The token grants conditional autonomy within a locked scope.

**Required fields**:

```
token_id: unique identifier
context_hash: sha256 of (action + content + decision_maker)
issued_at: UTC timestamp (ISO 8601)
scope: {
  action: string
  boundary: string
  decision_maker: string
}
validity: {
  reuse: forbidden
  auto_revoke_on_context_change: true
  expires_at: UTC timestamp or null (single-use)
}
proof: {
  responsibility: object
  alternatives: array
  stop_capability: boolean
}
```

### Token Lifecycle

1. **Issuance**: Only when all admission rules pass
2. **Validation**: Context hash must match at use time
3. **Revocation**: Automatic on context change or expiration
4. **Reuse**: Forbidden — one token, one execution

### Non-transferability

Tokens are bound to:
- Context hash (content + metadata)
- Timestamp (no retroactive use)
- Scope (no boundary expansion)

**Mutation prohibition**: Token fields cannot be modified after issuance.

---

## 4. Enforcement

### Prohibited Actions

- Proceeding without `CAN_PROCEED` check
- Reusing tokens across contexts
- Modifying token fields after issuance
- Bypassing admission interface

### Required Actions

- Call `CAN_PROCEED` before any execution
- Generate `WHY_STOPPED` proof on failure
- Validate `SCOPE_OF_VALIDITY` before token use
- Revoke tokens on context change

---

**Version**: 1.0.0
**Status**: Normative
**Modification**: Requires constitutional amendment
