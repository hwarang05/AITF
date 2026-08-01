# 99. TODO

Project : AITF (AI Technology Framework)

Version : v1.0

Status : Active

Last Updated : 2026-07-31

---

# 목적

본 문서는 AITF 프로젝트의 개발 로드맵이다.

단순한 TODO List가 아니라

현재 프로젝트 진행 상태와

우선순위를 관리한다.

새로운 개발자 또는 GPT는

본 문서를 가장 먼저 확인하여

현재 진행 상황을 파악한다.

---

# 개발 원칙

우선순위

★★★★★

필수 기능

★★★★☆

v1 완료 기능

★★★☆☆

v2 기능

★★☆☆☆

향후 기능

★☆☆☆☆

아이디어

---

# Phase 1

프로젝트 설계

Status

✅ 완료

---

□ Project.md

✅ 완료

□ RULE.md

✅ 완료

□ Architecture.md

✅ 완료

□ ERD.md

✅ 완료

□ API.md

✅ 완료

□ RAG.md

✅ 완료

---

목표

프로젝트 기준 문서 작성

---

# Phase 2

Backend Foundation

Status

🟨 진행 예정

Priority

★★★★★

---

□ SQLAlchemy Base

□ Database 연결

□ Config

□ Dependency Injection

□ Logging

□ AppException

□ Exception Handler

□ JWT

□ Authentication

□ Swagger

---

완료 조건

Backend 실행 가능

---

# Phase 3

Database

Priority

★★★★★

---

□ User

□ Conversation

□ SearchSession

□ SearchResult

□ Message

□ File

□ FileVersion

□ Chunk

□ Evidence

---

완료 조건

ERD 구현 완료

---

# Phase 4

Provider

Priority

★★★★★

---

□ Synology Provider

□ Ollama Provider

□ Embedding Provider

□ ChromaDB Provider

---

완료 조건

Provider 독립 구현

---

# Phase 5

Authentication

Priority

★★★★★

---

□ DSM Login

□ JWT

□ Refresh Token

□ Logout

□ Auth Middleware

---

# Phase 6

NAS

Priority

★★★★★

---

□ NAS Login

□ Folder Tree

□ File Metadata

□ Permission

□ Hash

---

# Phase 7

Sync

Priority

★★★★★

---

□ Hash Compare

□ FileVersion

□ Chunk

□ Embedding

□ ChromaDB

---

완료 조건

Incremental Sync

---

# Phase 8

RAG

Priority

★★★★★

---

□ Prompt Builder

□ Vector Search

□ SearchResult

□ Evidence

□ ChatService

---

완료 조건

AI 답변 가능

---

# Phase 9

Frontend

Priority

★★★★☆

---

□ Login

□ Folder Tree

□ Chat

□ Conversation

□ History

□ Evidence

---

# Phase 10

Optimization

Priority

★★★☆☆

---

□ Streaming

□ Cache

□ Prompt Optimization

□ Logging

□ Performance

---

# v2

Priority

★★☆☆☆

---

□ Collection

□ Document Compare

□ Version Compare

□ OCR

□ Workflow

□ Agent

□ Statistics

□ Admin

---

# v3

Priority

★☆☆☆☆

---

□ Teams

□ Slack

□ Outlook

□ Multi LLM

□ GPU

□ Redis

□ SSO

---

# 현재 진행률

설계

██████████████████

100%

Backend

░░░░░░░░░░░░░░░░░░

0%

Frontend

░░░░░░░░░░░░░░░░░░

0%

RAG

░░░░░░░░░░░░░░░░░░

0%

전체

████░░░░░░░░░░░░░░

약 20%

---

# 현재 가장 중요한 작업

★★★★★

SQLAlchemy Model 구현

★★★★★

Database 연결

★★★★★

Authentication

★★★★★

Synology Provider

★★★★★

ChatService

---

# GPT Context

새로운 GPT는

현재 프로젝트가

설계 완료 상태임을 기억한다.

다음 작업은

SQLAlchemy Model 구현이다.

구현 순서는

Model

↓

Service

↓

Provider

↓

API

↓

Frontend

순서를 유지한다.

Repository Pattern은 사용하지 않는다.

UnitOfWork는 사용하지 않는다.

ERD를 기준으로 구현한다.
