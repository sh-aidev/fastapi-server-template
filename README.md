<div align="center">

# FastAPI Server Template

[![python](https://img.shields.io/badge/-Python_%7C_3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![fastapi](https://img.shields.io/badge/FastAPI_%7C_0.110+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![uv](https://img.shields.io/badge/uv_%7C_0.11+-de5fe9?logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
![license](https://img.shields.io/badge/License-MIT-green?logo=mit&logoColor=white)

A minimal FastAPI server template managed with [uv](https://github.com/astral-sh/uv), with a `health` endpoint and a `greeting` endpoint.

</div>

## 📌 Feature
- [x] `uv` for dependency management
- [x] TOML + Pydantic based config
- [x] Health endpoint
- [x] Greeting endpoint
- [x] Centralized logging (loguru)
- [x] Custom exception handling

## 📁 Project Structure
The directory structure of the project looks like this:

```
├── LICENSE
├── Makefile
├── README.md
├── __main__.py
├── configs
│   └── config.toml
├── outputs
├── pyproject.toml
└── src
    ├── __init__.py
    ├── app.py
    ├── server
    │   ├── __init__.py
    │   └── server.py
    └── utils
        ├── __init__.py
        ├── config.py
        ├── exceptions.py
        ├── logger.py
        └── models.py
```

## 🚀 Getting Started

### Step 1: Install dependencies
```bash
uv sync
```

### Step 2: Run the server
```bash
uv run python __main__.py
# or
make run
```

The server starts at the host/port configured in `configs/config.toml` (default `0.0.0.0:8000`).

### Step 3: Try the endpoints
```bash
curl http://localhost:8000/v1/health
curl http://localhost:8000/v1/greet/world
```

## 📜 References
- [FastAPI](https://fastapi.tiangolo.com/)
- [uv](https://github.com/astral-sh/uv)
