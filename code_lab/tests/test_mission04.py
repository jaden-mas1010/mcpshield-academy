from code_lab.challenges.mission04 import agent_tool_allowed


def test_summarizer_can_do_required_work():
    assert agent_tool_allowed("soc_summarizer", "read_alert") is True
    assert agent_tool_allowed("soc_summarizer", "summarize_alert") is True


def test_summarizer_cannot_change_or_delete_data():
    assert agent_tool_allowed("soc_summarizer", "close_alert") is False
    assert agent_tool_allowed("soc_summarizer", "delete_alert") is False


def test_summarizer_cannot_export_database():
    assert agent_tool_allowed("soc_summarizer", "export_database") is False


def test_unknown_agent_role_denied():
    assert agent_tool_allowed("unregistered_agent", "read_alert") is False
    assert agent_tool_allowed("", "summarize_alert") is False
    assert agent_tool_allowed("soc_summarizer", "unknown_tool") is False
