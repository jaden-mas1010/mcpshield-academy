# RedKross Final Submission Checklist

## Before uploading to GitHub

- [ ] Run `python -m pytest -v --import-mode=importlib` and save a screenshot of the actual result.
- [ ] Run the Docker startup on your own computer, open the dashboard, and test the real MCP endpoint using Inspector.
- [ ] Complete at least one Student Workshop task from insecure JSON through correct validation.
- [ ] Capture screenshots of the overview, student repair flow, validator and MCP tool execution.
- [ ] Run `docker compose down` and verify containers stop.
- [ ] Ensure the repository does **not** include `.venv/`, `.env`, `.lab-backups/`, secrets, API keys or private RedLens code.
- [ ] Verify the architecture and README links display correctly on GitHub.
- [ ] Check any internship IP or publication restrictions before publishing publicly; private repositories can be shared subject to terms.

## Git commands (from project root)

```powershell
git init
git add .
git status
git commit -m "Build MCPShield cyber range lab"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mcpshield-academy.git
git push -u origin main
```

Create the empty repository on GitHub **before** running the remote/push commands, and replace YOUR_USERNAME with your real handle. If a remote already exists, use `git remote -v` and adjust instead of blindly adding another. Never publish sensitive values.

## Submission email checklist

To: research@redkross.org.in  
CC: ojas@redkross.org.in

Subject: Cyber Range Lab Development & Automation — MCPShield Academy — Project Submission

Include: GitHub URL, README/setup instructions, short implementation and test summary with actual results, attached/linked screenshots, and demo video link if recorded.

## Important scope statement

"The lab provides five local, synthetic security exercises with a browser policy workshop and automated grading. A separate Python MCP server demonstrates actual tool discovery and calls via MCP Inspector. The AI-agent animation and some attacks are deterministic simulations rather than live model inference."

The original assignment states final deadline **25 October 2027**; verify any shorter deadline directly with the internship coordinator.

- [ ] Demonstrate a student editing `code_lab/challenges/mission01.py` and rerunning `python -m code_lab.runner --mission 1` until the security tests pass.
- [ ] Show all five coding exercises and the `code_lab/PRODUCTION_BRIDGE.md` guide.
- [ ] Do not include instructor answer key in student-facing public repository unless intended.
