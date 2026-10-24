# Demonstration Script (approx. 3 minutes)

**0:00–0:20 — Brief:** "MCPShield Academy is a standalone cyber range for MCP/AI-agent security. All data is synthetic and services are localhost-only. Five missions teach access control, tool poisoning, indirect prompt injection, least privilege and audit detection."

**0:20–0:50 — Architecture:** Show `docs/architecture.png`. Explain separate dashboard (`:8088`) and real MCP tool server (`:8000`) with Python mission functions and grading engine.

**0:50–1:30 — Mission 01:** In the dashboard select The Exposed Alert, show vulnerable mode letting Alice see Bob's alert, then secure mode denying it. Scroll to Student Workshop and click validate on the *insecure* starter; discuss which checks fail.

**1:30–2:05 — Hands-on repair:** Change `enforce_owner_for_analyst` from `false` to `true`. Answer the mission question, then validate again and show 100% with named passing tests. Emphasise it isn't enough to click an attack simulation.

**2:05–2:25 — Further missions:** Show Mission 02 poisoned tool description and Mission 05's 3 detected threats in 6 synthetic audit events.

**2:25–2:45 — Real MCP:** Open MCP Inspector, connect to `http://127.0.0.1:8000/mcp`, run `read_alert` or `investigate_security_logs` and show actual protocol tool results. Explain that the browser animation itself is simulated.

**2:45–3:00 — Verification:** Show local `pytest` output and Docker Compose containers, then `docker compose down` for safe shutdown. End with the GitHub repository and documentation.

## Evidence capture suggestions

1. Dashboard overview with five missions.
2. Mission 01 vulnerable data exposure.
3. Failed policy-validation results before fixing.
4. Passing policy-validation results after fixing.
5. MCP Inspector real tool output.
6. Terminal test summary and Docker Compose running status.

Capture **your own screenshots** from your machine. The supplied preview files are reference imagery, not evidence that your specific Windows Docker deployment was tested.

## Five-mission coding workshop (recommended live demonstration)

1. In the dashboard, scroll to **Python Defence Engineering**. Select **Mission 01**. Point out the `TODO` and ask why Alice can read Bob's alert.
2. Open `code_lab/challenges/mission01.py` in VS Code. Run `python -m code_lab.runner --mission 1` and show the failed ownership checks.
3. Add a role-and-owner check, rerun the tests and explain why an unassigned alert must be denied. If using the browser editor, download the edited `.py`, save into `code_lab/challenges/` and test locally.
4. Briefly select Missions 02–05 in the dashboard to demonstrate each editable code exercise, hint and per-mission test command.
5. Show `code_lab/PRODUCTION_BRIDGE.md`, explaining verified identity, trusted manifests, independent tool authorisation, least-privilege tokens and time-bounded audit monitoring.
6. To reset after the demo, use `python -m code_lab.reset --mission 1 --yes` (backs up the edited code).

Do not run unknown Python submitted through the web dashboard; student source tests belong in the learner's local, isolated environment.
