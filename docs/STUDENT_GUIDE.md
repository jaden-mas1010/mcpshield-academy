# Student Guide — MCPShield Academy

## Learning goals

By the end of the lab you should be able to (1) distinguish authentication from role- and object-level authorisation, (2) identify tampered tool metadata, (3) separate untrusted log content from authority, (4) enforce least privilege for an AI agent, and (5) investigate synthetic MCP audit events.

## Before you start

Open http://127.0.0.1:8088 after the instructor starts the lab. Choose one of the five missions. Each includes a fictional incident and evidence. Everything is simulated and **must remain inside the training environment**.

## For each mission

1. **Investigate:** read the scenario and provided evidence; state the trust boundary or control that failed.
2. **Reproduce:** run vulnerable mode, compare with hardened mode, and inspect the result. This helps you understand the scenario but does *not* award completion.
3. **Repair:** in Student Workshop, edit the JSON configuration in the built-in editor. Do **not** change the expected answer fields or invent new schema keys.
4. **Validate:** click `Validate my security fix` and inspect any failing cases. Your configuration must both block malicious actions and preserve authorised actions.
5. **Explain:** answer the mission's knowledge question correctly; a policy-only score is insufficient to complete the mission.
6. **Reset:** use `Reset starter` to start again if needed. This resets the in-browser policy editor.

## Expected results and hints

| Mission | What your fix must achieve | Hint |
|---|---|---|
| 01 | Alice reads ALERT-001 but is denied ALERT-002; supervisor still reads both | An analyst's role is not sufficient: compare the alert's trusted `assigned_to` value |
| 02 | A known `read_alert` description is accepted but any poisoned/unknown description is rejected | Compare descriptions against trusted metadata, not untrusted server text |
| 03 | A synthetic `[AGENT_CMD:CLOSE_ALERT]` log entry cannot close an alert; trusted approved actions still work | Logs are *data*, not instructions with authority |
| 04 | The SOC summary agent can read and summarise; cannot close/delete/export | Restrict privileges to the actual task |
| 05 | Detect 3 suspicious patterns, avoid false positives on normal activity | Use privileged tools, tamper indicator, and a 3-denial threshold |

## Hands-on Python track — recommended practical assessment

The dashboard's JSON-policy editor introduces concepts; the **Python Defence Engineering** panel lets you inspect starter Python and download your edited function. The live server does not execute browser-submitted Python. To earn **source-code competency**, work locally in VS Code:

1. Open `code_lab/challenges/mission01.py` and identify the vulnerability.
2. Run `python -m code_lab.runner --mission 1` to observe failing security tests.
3. Edit `can_read_alert()` to enforce ownership without blocking legitimate access.
4. Rerun tests; explain why the failing tests now pass.
5. Repeat for missions 02–05. Each has an independent source file and test suite.
6. Run `python -m code_lab.runner` for the full 23-check coding track.

The intentionally insecure starters yield **15 failed, 8 passed**. The instructors' tested reference implementations pass **23/23**. Run `python -m code_lab.reset --mission 3 --yes` to back up then reset an exercise.

For a discussion of real-world implementation, read [Production Bridge](../code_lab/PRODUCTION_BRIDGE.md). The lab functions are **not ready for public production deployment** without verified identity, tenant boundaries, properly protected config and live integration tests.

## Reflection questions

1. Why isn't a role allowlist sufficient to protect individual alerts?
2. What makes an MCP tool description a potentially untrusted input?
3. Why must permission enforcement occur *outside* a model's prompt instructions?
4. What is the difference between tool registration and tool authorisation?
5. How do detection rules avoid false positives, not merely catch attacks?

Write a short reflection (3–5 sentences per question) if requested by your instructor.
