from code_lab.challenges.mission03 import authorize_agent_action


def test_normal_untrusted_data_can_be_summarized():
    assert authorize_agent_action("tool_response", "summarize_alert", False) is True


def test_untrusted_log_cannot_authorize_privileged_action():
    assert authorize_agent_action("tool_response", "close_alert", False) is False
    assert authorize_agent_action("tool_response", "close_alert", True) is False


def test_trusted_request_requires_out_of_band_approval():
    assert authorize_agent_action("trusted_request", "close_alert", False) is False
    assert authorize_agent_action("trusted_request", "close_alert", True) is True


def test_unknown_sources_and_actions_fail_closed():
    assert authorize_agent_action("fake_source", "close_alert", True) is False
    assert authorize_agent_action("tool_response", "export_database", True) is False
    assert authorize_agent_action("fake_source", "summarize_alert", False) is False
