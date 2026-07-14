# Forge

Forge is an AI-powered portfolio, knowledge base, and engineering lab.

## Goals

- Learn Python
- Learn AI Engineering
- Build production-ready software
- Document the journey
- Showcase projects

## Tech Stack

Frontend
- React
- TypeScript
- Vite

Backend
- FastAPI
- Python

Database
- PostgreSQL

AI
- (Coming Soon)

## Roadmap

- [x] Foundation: repository setup, React frontend, and FastAPI health service
- [ ] Portfolio: build the about, projects, and contact pages
- [ ] Content: add a blog with Markdown publishing
- [ ] Platform: add authentication and PostgreSQL persistence
- [ ] AI: build an assistant, RAG search, and agent workflows

## Local development

### Prerequisites

node.js v22.12.0
Python 3.14.5

### Frontend

```bash
cd frontend
npm install
npm run dev
```

To verify the frontend, run `npm run lint` and `npm run build` from `frontend/`.


### Backend

#### Windows — Git Bash

```bash
cd backend
py -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

#### Windows — PowerShell

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

#### macOS/Linux

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Once the backend is running:

- Health: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Quality checks

### Frontend

From `frontend/`, run the following commands to verify linting and the production build:

```bash
npm run lint
npm run build
```

### Backend

From `backend/`, with the virtual environment activated:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

To apply formatting automatically:

```bash
python -m ruff format .
```

## License

This project is licensed under the [MIT License](LICENSE).
