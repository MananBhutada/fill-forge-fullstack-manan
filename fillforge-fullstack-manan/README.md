
# FillForge-Auto (Universal Autofill Platform) - Demo Scaffold

This repository is a scaffolded demo for a **Universal Autofill Platform** that uses `.docx` templates with placeholders
(e.g., `{{NAME}}`, `{{DOB}}`) and auto-fills them from stored user profiles and uploaded documents.

> This ZIP contains a complete starter project with a FastAPI backend, a sample Next.js frontend scaffold,
> Docker Compose configuration (MySQL + Adminer + backend + frontend), Alembic migrations placeholder,
> sample `.docx` templates, and a basic ML mapping module using `rapidfuzz` for fuzzy matching.

## Quick start (Docker)
1. Copy `.env.example` to `.env` and adjust values if required.
2. Run:
```bash
docker compose up --build
```
3. Open the frontend at `http://localhost:3000` and the backend at `http://localhost:8000`.

## Quick start (local dev)
- Backend:
  - Create a Python venv and install requirements from `backend/requirements.txt`.
  - Set `DATABASE_URL` in env (MySQL URI or fallback to sqlite in examples).
  - Run `uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000`

- Frontend:
  - `cd frontend`
  - `npm install` or `pnpm install`
  - `npm run dev`

## What's included
- `backend/` - FastAPI app with auth (JWT), profile, documents, forms endpoints, and ML mapping + docx filling.
- `frontend/` - Next.js scaffold (TypeScript) with pages for Profile, Documents, Forms and a simple Dashboard.
- `samples/` - 3 `.docx` templates and dummy documents (small images).
- `docker-compose.yml` - MySQL 8, Adminer, backend, frontend services.
- `db/` - Alembic placeholder and seed script for test user/data.
- `tests/` - basic pytest for mapping logic.
- `openapi.json` - exported API schema placeholder.
- `README.md` - you are reading it.

## Test credentials (seeded)
- Email: `ravi.kumar@example.com`
- Password: `Passw0rd!`

---
This is a scaffold for demonstration and local development. It avoids any external cloud dependency.
