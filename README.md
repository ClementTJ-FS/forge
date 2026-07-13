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

- [ ] Sprint 0
- [ ] Sprint 1
- [ ] Authentication
- [ ] Blog
- [ ] AI Assistant
- [ ] RAG
- [ ] Agents

## Local development

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
