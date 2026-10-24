# Instructor Guide

## Audience and duration

Introductory to intermediate cybersecurity learners with basic Python/JSON familiarity. Suggested 45–75 minute session: 10-minute introduction, 25–45 minutes of challenges, 10-minute debrief, 5-minute demonstrations.

## Learning objectives

Students will (1) explain BOLA and RBAC differences, (2) recognise MCP metadata tampering, (3) identify instructions in untrusted tool results, (4) enforce least-privilege tool grants, and (5) apply simple MCP audit detection rules.

## Teaching workflow

Use Mission 01 as a guided worked example. Ask the student to observe Alice retrieving Bob's alert, then change only the ownership setting in the JSON policy. Have them validate. Guide Missions 02–05 with fewer hints. Require the knowledge check for completion.

The dashboard has demonstration controls and the separate actual policy workshop; **do not award credit simply for clicking demonstration buttons**. The browser's stored progress is only instructional; it can be edited by the user and is not an LMS record.

## Assessment

A browser mission is complete only if all its policy test scenarios pass *and* the learner selects the correct knowledge response. The Python coding track expects 10 automated checks to pass once students fix five deliberately flawed functions. As an instructor, ask students to explain why the fixed code preserves normal behaviour and denies the attack.

## Protocol demonstration

Start `python server.py` (port 8000) separately from `python dashboard.py` (port 8088). Open MCP Inspector using Streamable HTTP at `http://127.0.0.1:8000/mcp`. Demonstrate `read_alert("ALERT-001")`, `inspect_tool_metadata`, and `investigate_security_logs`.

The MCP layer is real protocol traffic, but the simulated roles and attacks are *not* production IAM or model-red-teaming results.

## Before class

- Verify Docker or Python is installed.
- Verify no other programs occupy ports 8000 and 8088.
- Run `python -m pytest -v --import-mode=importlib` with secure Mission 01 reference code.
- Capture one dashboard screenshot and one evidence / grading screenshot for reports.
- Never insert real data into the fictional alert database.

## Reset between learners

For the web lab, select Reset starter or reload in a fresh browser/profile. For Python Mission 01, run `python reset_mission01.py --reset` (backs up the current implementation); this deliberately reintroduces the vulnerability. Restore the secure reference afterward and restart the MCP server before running the full suite.

For a completely clean Docker session: `docker compose down` and `docker compose up --build -d` (browser local progress must also be cleared/reset separately).
