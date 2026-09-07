# Learning Path: AI for a Java Backend Engineer

## Goal

In six months of consistent practice (about 8–10 hours per week), build the ability to design, evaluate, deploy, and maintain AI-powered backend services. The target is not only to call an LLM API, but to understand the data, models, retrieval, evaluation, security, and operational concerns behind a reliable AI feature.

## Guiding principle

Learn by building. For every concept, create a small implementation, write down what you observed, and commit it. Your Java/Spring Boot experience is valuable: apply it to API design, testing, resilience, security, Docker, and observability while learning the AI-specific pieces in Python.

## Phase 1 — Python and data foundations (Weeks 1–3)

Learn enough Python to work productively in the AI ecosystem. Focus on virtual environments, packages, functions, classes, type hints, files, notebooks, NumPy, pandas, and matplotlib.

Outcome: load a public CSV dataset, clean it, explore it, and communicate three useful findings with plots.

Folder: `01-python-data/`

## Phase 2 — Classical machine learning (Weeks 4–7)

Learn the vocabulary and workflow shared by nearly all ML systems: features and labels, train/validation/test sets, regression, classification, preprocessing, cross-validation, overfitting, data leakage, and evaluation metrics.

Outcome: train and evaluate a ticket-priority or customer-churn classifier using scikit-learn. Explain why the selected metric is appropriate.

Folder: `02-classical-ml/`

## Phase 3 — Essential math intuition (Weeks 8–9)

Study only the math that makes model behavior understandable: vectors and matrices, dot products, distributions, mean/variance, conditional probability, loss functions, derivatives, and gradient descent.

Outcome: implement linear regression and gradient descent once using NumPy. The goal is understanding, not replacing ML libraries.

Folder: `03-math-intuition/`

## Phase 4 — Deep learning (Weeks 10–13)

Learn tensors, neural-network layers, activation functions, backpropagation, optimizers, regularization, embeddings, and the high-level idea of transformers. Use PyTorch to build your intuition.

Outcome: train a small image or text classifier, save the model, and write an inference script.

Folder: `04-deep-learning/`

## Phase 5 — LLM engineering (Weeks 14–18)

Learn how modern AI features are actually built: tokens and context windows, prompt design, structured output, embeddings, vector search, retrieval-augmented generation (RAG), tool calling, safety, and evaluation.

Outcome: build a document Q&A service over a small set of Spring Boot documentation. Answers should include retrieved source references and a response when the evidence is insufficient.

Folder: `05-llm-engineering/`

## Phase 6 — Production AI systems (Weeks 19–24)

Make the LLM project production-minded. Learn FastAPI, Docker, async jobs, caching, rate limiting, authentication, observability, cost/latency measurement, prompt/version management, automated evaluations, and failure handling. Integrate the AI service with Spring Boot.

Outcome: deploy a small AI backend service with tests, a health endpoint, structured logs, and a documented API contract.

Folder: `06-production-ai/`

## Portfolio projects

Build these sequentially; each should have a README with architecture, setup instructions, trade-offs, and tests.

1. **Support-ticket classifier** — classical ML model exposed through an API.
2. **Documentation assistant** — RAG system over technical documents with citations and evaluation cases.
3. **Incident assistant** — retrieves runbooks and summarizes logs to suggest diagnostic next steps. Do not let it execute production actions.

Folder: `projects/`

## Weekly rhythm

- 3 hours: study one focused concept.
- 4 hours: implement an exercise or project increment.
- 1 hour: write short notes in the relevant module.
- 1–2 hours: test, refactor, or deploy what you built.

## What to postpone

Do not begin with training a foundation model, advanced research papers, multi-agent frameworks, or expensive GPU infrastructure. First gain strong instincts for data quality, evaluation, retrieval, and reliable software design.
