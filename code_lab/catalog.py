"""Public exercise metadata: readable from the dashboard, never executed there."""
from pathlib import Path

BASE = Path(__file__).resolve().parent

MISSIONS = {
    1: {"title": "Object-level authorisation", "goal": "Use a trusted role and resource owner to make an allow/deny decision.",
        "hint": "Supervisor is allowed; analyst must match assigned_to; missing owner or role defaults to deny.",
        "production": "Authenticated principal + database-owned alert + per-request policy check.",
        "why": "Fixes BOLA/IDOR; role checks alone do not protect individual resources."},
    2: {"title": "Tool definition integrity", "goal": "Reject changed descriptions, parameter schemas and annotations.",
        "hint": "Compare the complete tool definition with the pre-approved manifest, not only its name.",
        "production": "Pin reviewed schemas with a signed or protected manifest; verify before tools enter model context or execute.",
        "why": "Tool descriptions and schemas can carry instructions or change authority hints."},
    3: {"title": "Prompt-injection trust boundary", "goal": "Never let retrieved content authorise privileged tool calls.",
        "hint": "Summaries are safe; close_alert needs trusted_request AND independently verified approval.",
        "production": "At the tool executor, authorise every action using verified identity, scope and out-of-band approval.",
        "why": "Untrusted tool output must remain data, even when it sounds authoritative."},
    4: {"title": "Least privilege for agents", "goal": "Give the summariser only the read and summarise tools.",
        "hint": "Use an allowlist by known agent role. Unknown roles get an empty set.",
        "production": "Scoped tokens and per-tool policy checks tied to the authenticated agent and user.",
        "why": "A compromised agent cannot misuse capabilities it does not possess."},
    5: {"title": "Security audit detections", "goal": "Detect privilege misuse, metadata tampering and repeated denied tool calls.",
        "hint": "Track denials by (actor, tool); flag tampered integrity and privileged tool ALLOWED by restricted roles.",
        "production": "Tamper-resistant structured events, secrets redaction, rolling time windows, SIEM alerts and triage.",
        "why": "Monitoring should catch threats without alerting on every legitimate request."},
}


def public_code_mission(number: int) -> dict:
    if type(number) is not int or number not in MISSIONS:
        raise ValueError("Unknown coding mission")
    item = MISSIONS[number]
    code = (BASE / "challenges" / f"mission{number:02}.py").read_text(encoding="utf-8")
    return {**item, "mission": number, "code": code,
            "path": f"code_lab/challenges/mission{number:02}.py",
            "command": f"python -m pytest code_lab/tests/test_mission{number:02}.py -v --import-mode=importlib"}
