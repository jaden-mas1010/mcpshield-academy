from code_lab.challenges.mission01 import can_read_alert


def test_authorized_access_still_works():
    assert can_read_alert("analyst", "alice", {"assigned_to": "alice"}) is True
    assert can_read_alert("supervisor", "sam", {"assigned_to": "bob"}) is True


def test_analyst_cannot_read_other_users_alert():
    assert can_read_alert("analyst", "alice", {"assigned_to": "bob"}) is False


def test_missing_owner_or_identity_denied():
    assert can_read_alert("analyst", "alice", {}) is False
    assert can_read_alert("analyst", "", {"assigned_to": ""}) is False


def test_unknown_roles_denied():
    assert can_read_alert("stranger", "eve", {"assigned_to": "eve"}) is False
    assert can_read_alert("", "alice", {"assigned_to": "alice"}) is False
