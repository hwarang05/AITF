# AITF (AI Technology Framework)

Enterprise AI Knowledge Platform

---

# 프로젝트 소개

AITF는 Synology NAS에 저장된 기업 문서를 AI가 검색하고 질의응답하는 Enterprise AI Knowledge Platform이다.

이 프로젝트는 일반적인 Upload 기반 RAG가 아니다.

모든 문서는 NAS를 원본(Source of Truth)으로 사용하며,

권한은 Synology DSM을 그대로 따른다.

---

# 프로젝트 목표

- Enterprise RAG
- Permission Based Search
- Evidence
- Reproducibility
- Maintainability
- Provider Pattern

---

# 프로젝트 상태

현재 상태

Design Completed

Backend Development Ready

---

# 프로젝트 문서

프로젝트를 이해하려면 반드시 아래 순서대로 문서를 읽는다.

① docs/00_RULE.md

프로젝트 최상위 규칙

↓

② docs/01_Project.md

프로젝트 개요

↓

③ docs/02_Architecture.md

전체 시스템 구조

↓

④ docs/04_ERD.md

Database 구조

↓

⑤ docs/05_RAG.md

RAG 설계

↓

⑥ docs/03_API.md

API 설계

↓

⑦ docs/99_TODO.md

현재 개발 상태

↓

⑧ docs/06_DevLog.md

최근 변경 이력

---

# 현재 프로젝트 진행 상태

Architecture

100%

ERD

100%

RAG Design

100%

API Design

100%

Backend

시작 전

Frontend

시작 전

---

# 기술 스택

Backend

- FastAPI
- SQLAlchemy

Database

- SQLite

Vector Database

- ChromaDB

LLM

- Ollama

Storage

- Synology NAS

Frontend

- React
- TypeScript

Container

- Docker

---

# 핵심 설계 원칙

- NAS가 Source of Truth
- Upload 기반 RAG 사용 안 함
- Backend First
- Service Pattern
- Provider Pattern
- Repository Pattern 사용 안 함
- UnitOfWork 사용 안 함
- 모든 답변은 Evidence를 가진다.
- 모든 답변은 재현 가능해야 한다.

---

# 개발 순서

다음 순서를 변경하지 않는다.

1. SQLAlchemy Model

↓

2. Service

↓

3. Provider

↓

4. API

↓

5. Frontend

---

# 현재 구현 우선순위

★★★★★

Database Model

★★★★★

Authentication

★★★★★

Synology Provider

★★★★★

ChatService

★★★★★

RAG

---

# GPT에게

새로운 GPT는 반드시 다음 사항을 기억한다.

이 프로젝트는 일반적인 RAG 프로젝트가 아니다.

NAS가 원본이다.

Service 중심 구조를 유지한다.

ERD를 변경하지 않는다.

Evidence를 제거하지 않는다.

답변 재현 기능을 유지한다.

Repository Pattern은 사용하지 않는다.

UnitOfWork는 사용하지 않는다.

Provider는 언제든 교체 가능해야 한다.

프로젝트의 기준 문서는 docs 폴더이다.

README보다 docs를 우선한다.