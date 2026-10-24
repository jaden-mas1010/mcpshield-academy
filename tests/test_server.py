import server


def test_analyst_cannot_close(monkeypatch):
    monkeypatch.setattr(server,'LAB_ROLE','analyst')
    assert server.close_alert('ALERT-001')['error']=='Permission denied'


def test_analyst_cannot_read_bob_in_secure_mode(monkeypatch):
    monkeypatch.setattr(server,'LAB_ROLE','analyst')
    monkeypatch.setattr(server,'LAB_USER','alice')
    monkeypatch.setattr(server,'LAB_MODE','secure')
    assert server.read_alert('ALERT-002') == {'error':'Permission denied'}


def test_vulnerable_mode_exposes_bob(monkeypatch):
    monkeypatch.setattr(server,'LAB_ROLE','analyst')
    monkeypatch.setattr(server,'LAB_USER','alice')
    monkeypatch.setattr(server,'LAB_MODE','vulnerable')
    assert server.read_alert('ALERT-002')['assigned_to']=='bob'


def test_synthetic_incident_detection():
    assert server.investigate_security_logs()['threats_detected']==3
