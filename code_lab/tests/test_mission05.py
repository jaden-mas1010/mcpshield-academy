from code_lab.challenges.mission05 import detect_attack_types


def evt(actor="alice", role="analyst", tool="read_alert", decision="ALLOWED", integrity="trusted"):
    return dict(actor=actor, role=role, tool=tool, decision=decision, integrity=integrity)


def test_normal_activity_produces_no_threats():
    normal = [evt(), evt(actor="sam", role="supervisor", tool="close_alert")]
    assert detect_attack_types(normal) == set()


def test_privileged_export_by_agent_detected():
    events = [evt(actor="bot", role="agent", tool="export_database")]
    assert "EXCESSIVE_PRIVILEGE" in detect_attack_types(events)


def test_metadata_tampering_detected():
    events = [evt(actor="bot", role="agent", integrity="tampered")]
    assert "TOOL_TAMPERING" in detect_attack_types(events)


def test_three_denials_same_actor_and_tool_detected():
    events = [evt(tool="close_alert", decision="BLOCKED") for _ in range(3)]
    assert "REPEATED_DENIALS" in detect_attack_types(events)


def test_mixed_denials_do_not_create_false_positive():
    events = [evt(actor="alice", tool="close_alert", decision="BLOCKED"),
              evt(actor="bob", tool="close_alert", decision="BLOCKED"),
              evt(actor="alice", tool="export_database", decision="BLOCKED")]
    assert "REPEATED_DENIALS" not in detect_attack_types(events)


def test_full_scenario_detects_three_threats():
    events = [evt(tool="close_alert", decision="BLOCKED") for _ in range(3)]
    events += [evt(actor="bot", role="agent", tool="export_database"),
               evt(actor="bot", role="agent", integrity="tampered")]
    assert detect_attack_types(events) == {"REPEATED_DENIALS", "EXCESSIVE_PRIVILEGE", "TOOL_TAMPERING"}
