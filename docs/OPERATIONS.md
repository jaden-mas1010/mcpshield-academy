# Setup, Start, Reset, Troubleshoot and Safe Shutdown

## Prerequisites

Python 3.11+, pip and VS Code (local mode), or Docker Desktop + Docker Compose v2 (container mode). Node.js with `npx` is optional for MCP Inspector.

## Docker start

```powershell
docker compose up --build -d
docker compose ps
docker compose logs --tail=40 academy mcp
```

Browser: http://127.0.0.1:8088. MCP Streamable HTTP: `http://127.0.0.1:8000/mcp` — connect with an MCP client, not a normal GET to browser address bar.

## Local start

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe dashboard.py
```

Optional separate terminal:

```powershell
.\.venv\Scripts\python.exe server.py
```

## Reset

- Browser: `Reset starter` in each mission. Browser progress is local, not a secured gradebook.
- Local source exercise Mission 01: `python reset_mission01.py --reset` backs up existing code to `.lab-backups/` then replaces it with the insecure original.
- Docker lab state: `docker compose down` followed by `docker compose up --build -d`; no persistent volumes are used, so in-memory alert modifications reset when containers restart.
- After editing Mission 01 Python code, restart the Python MCP process; the dashboard may also need restarting to reload imported code.

## Troubleshooting

| Symptom | Likely issue | Fix |
|---|---|---|
| `WinError 10048` or address already in use | Another process has port 8000 or 8088 | Stop previous known lab terminal with Ctrl+C; check which PID owns the port before stopping any process |
| MCP Inspector says Missing session ID | Endpoint opened directly or stale MCP session | Connect via Streamable HTTP Inspector and initialise/reconnect |
| `ModuleNotFoundError: mcp` | SDK not installed in active virtual environment | `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` |
| Dashboard doesn't load | Wrong working directory / server stopped | Start `dashboard.py` from project root; open http://127.0.0.1:8088 |
| Test suite finds 0 tests | Missing files or wrong project root | Confirm `tests/test_*.py` files exist and are nonempty |
| `import file mismatch` | Duplicated named tests in `test/` and `tests/` | Remove duplicate and use `--import-mode=importlib` |
| Five Mission 01 secure tests fail | Reset script restored the vulnerable starter | Restore the secure Mission 01 reference implementation |
| MCP Inspector cannot connect to Docker | Stopped MCP container or wrong host binding | `docker compose ps`, then connect to `http://127.0.0.1:8000/mcp` |
| Browser loads old dashboard | Browser cache | Hard reload with Ctrl+F5 |

## Safe shutdown

Local terminals: press `Ctrl+C` in both `dashboard.py` and `server.py` windows.

Docker:

```powershell
docker compose down
```

No production network, host scanner, or real external targets should be used. The lab only contains synthetic records and in-memory simulated actions.
