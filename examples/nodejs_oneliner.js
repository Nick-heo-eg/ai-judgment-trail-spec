/**
 * Node.js One-Liner Example
 *
 * Minimal AJT logging - just console.log with structure.
 * No packages, no setup.
 */

// One-liner helper
const logAJT = (model, decision, riskLevel, policyVersion, humanInLoop = false) =>
  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    run_id: crypto.randomUUID(),
    model,
    decision,
    risk_level: riskLevel,
    human_in_loop: humanInLoop,
    policy_version: policyVersion,
    app_version: process.env.npm_package_version || "1.0.0",
    session_id: crypto.randomUUID()
  }));


// Example usage
if (require.main === module) {
  // Example 1: Allow decision
  logAJT("gpt-4", "allow", "low", "v1.0");

  // Example 2: Block with human review
  logAJT("claude-3-opus", "block", "high", "v1.0", true);

  // Example 3: Escalate
  logAJT("gemini-pro", "escalate", "medium", "v1.0");

  console.log("\n✅ Three AJT records logged above");
}

module.exports = { logAJT };
