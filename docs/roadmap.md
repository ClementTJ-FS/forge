# Forge Roadmap

Forge is built in small, verified milestones. Each milestone should leave the
project in a working state and improve one part of the full-stack AI engineering
journey.

## 1. Foundation

Establish a reproducible local development environment before adding product
features.

- [x] Initialize the repository, project documentation, and ignore rules
- [x] Create the React, TypeScript, and Vite frontend
- [x] Create the FastAPI backend and `GET /health` endpoint
- [x] Document and verify the local developer workflow
- [x] Add baseline code quality checks: backend formatting, linting, and a health-endpoint test
- [x] Run the Foundation release checklist

## 2. Portfolio Experience

Turn Forge into a clear portfolio for the work being built.

- [ ] Create the portfolio landing page
- [ ] Add an about page
- [ ] Build a projects showcase
- [ ] Add a contact page

## 3. Content Publishing

Document the journey through technical writing.

- [ ] Add a blog
- [ ] Add Markdown authoring and rendering support

## 4. Platform Foundations

Introduce the persistence and identity capabilities needed for a real product.

- [ ] Add PostgreSQL persistence
- [ ] Add authentication

## 5. AI Engineering Lab

Build AI capabilities incrementally on top of the application foundation.

- [ ] Build an AI assistant
- [ ] Add retrieval-augmented generation (RAG) search
- [ ] Explore agent workflows

## Guiding Principles

- Keep `main` working at all times.
- Deliver one focused issue at a time.
- Verify each milestone locally before merging it.
- Record meaningful technical decisions in the decision log.
