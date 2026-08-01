# 02. Architecture

Project : AITF (AI Technology Framework)

Version : v1.0

Status : Designing

---

# 1. Architecture Overview

## 목적

AITF는 기업 문서를 AI가 검색하고 질의응답하는 Enterprise AI Knowledge Platform이다.

AITF는 일반적인 ChatGPT 서비스나 Upload 기반 RAG와 다르다.

AITF는 NAS를 Source of Truth로 사용하며,
검색을 위한 Metadata와 Embedding만 관리한다.

---

# 2. Design Philosophy

AITF는 다음 설계 철학을 따른다.

## 2.1 Backend First

Business Logic은 모두 Backend에 존재한다.

Frontend는

- 화면 표시
- 사용자 입력
- API 호출

만 수행한다.

---

## 2.2 Service Oriented

Business Logic은 Service가 담당한다.

API는 Service를 호출하는 역할만 수행한다.

---

## 2.3 Provider Pattern

외부 시스템은 Provider를 통해 접근한다.

Provider는 언제든 교체 가능해야 한다.

---

## 2.4 Reproducibility First

모든 AI 답변은

왜 그렇게 답했는지

재현 가능해야 한다.

---

## 2.5 Security First

권한은 반드시 Backend가 검사한다.

LLM은 권한을 알지 못한다.

---

# 3. High Level Architecture

                React

                  │

          REST API (HTTPS)

                  │

                  ▼

             FastAPI

                  │

    ┌─────────────┼────────────────┐

    ▼             ▼                ▼

 Authentication  Chat         NAS Sync

                  │

                  ▼

             RAG Service

                  │

        ┌─────────┼─────────┐

        ▼         ▼         ▼

    Embedding   Vector    Evidence

        │

        ▼

   Provider Layer

        │

┌───────┼─────────────────────────────┐

▼       ▼             ▼              ▼

NAS   Ollama      ChromaDB        SQLite

---

# 4. Layer Architecture

AITF는 5개의 Layer를 가진다.

Presentation

↓

Application

↓

Service

↓

Provider

↓

Infrastructure

---

## 4.1 Presentation Layer

기술

- React
- TypeScript

역할

- 로그인

- NAS Tree

- Chat

- History

- Evidence

Business Logic은 존재하지 않는다.

---

## 4.2 Application Layer

FastAPI Router

예시

POST /login

POST /chat

GET /nas/tree

GET /conversation

역할

- Request

- Validation

- Response

- Service 호출

---

## 4.3 Service Layer

AITF의 핵심 계층

모든 Business Logic 수행

대표 Service

AuthenticationService

NASService

NASSyncService

IndexingService

ChunkService

EmbeddingService

VectorSearchService

RAGService

ChatService

ConversationService

EvidenceService

AuditService

---

### Service 의존성

ChatService

↓

NASSyncService

↓

RAGService

↓

EvidenceService

↓

ConversationService

---

Service끼리는 필요한 경우만 의존한다.

순환 참조는 허용하지 않는다.

---

## 4.4 Provider Layer

외부 시스템 접근

Provider 예시

SynologyProvider

OllamaProvider

EmbeddingProvider

ChromaDBProvider

Provider는

Interface

↓

Implementation

구조를 유지한다.

Service는 구현체를 직접 알지 않는다.

---

## 4.5 Infrastructure

실제 시스템

Synology NAS

SQLite

ChromaDB

Ollama

Docker

---

# 5. Directory Structure

backend/

    app/

        api/

        core/

        models/

        schemas/

        services/

        providers/

        parsers/

        utils/

        dependencies/

    tests/

    docker/

    scripts/

---

## api/

FastAPI Router

Business Logic 금지

---

## services/

Business Logic

프로젝트 핵심

---

## providers/

외부 시스템 접근

---

## parsers/

문서 파싱

지원 예정

PDF

DOCX

PPTX

XLSX

TXT

---

## models/

SQLAlchemy Entity

---

## schemas/

Pydantic DTO

---

## core/

Config

Database

Security

---

# 6. Chat Architecture

Chat는 다음 순서로 동작한다.

User

↓

POST /chat

↓

ChatService

↓

NASSyncService

↓

Indexing

↓

Embedding

↓

Vector Search

↓

Prompt 생성

↓

Ollama

↓

Answer 생성

↓

Conversation 저장

↓

Evidence 저장

↓

Response

---

# 7. NAS Sync

AITF는 질문마다

선택한 범위만 Sync한다.

동작

선택 Folder

↓

NAS 조회

↓

Hash 비교

↓

변경 없음

↓

Search

---------------

변경 있음

↓

새 Version 생성

↓

Chunk 생성

↓

Embedding 생성

↓

Vector 저장

↓

Search

---

# 8. Search Architecture

Question

↓

Embedding

↓

ChromaDB

↓

Top K Chunk

↓

SearchResult 저장

↓

Prompt 생성

↓

LLM

↓

Answer

---

# 9. Evidence Architecture

답변 생성 후

Evidence를 생성한다.

Message

↓

Evidence

↓

Chunk

↓

FileVersion

↓

File

이를 통해

답변 당시 문서를 복원할 수 있다.

---

# 10. File Version Architecture

File

↓

FileVersion

↓

Chunk

Chunk는

File이 아니라

FileVersion을 참조한다.

이 구조를 변경하지 않는다.

---

# 11. Conversation Architecture

Conversation

↓

SearchSession

↓

Message

↓

Evidence

SearchSession은

검색 자체를 의미한다.

Message는

사용자 질문

AI 답변

만 관리한다.

---

# 12. Dependency Rules

허용

API

↓

Service

↓

Provider

↓

Infrastructure

금지

API → Provider

Provider → Service

Provider → Provider

Frontend → Database

LLM → NAS

---

# 13. Security

권한은

Backend

↓

NAS

에서 확인한다.

LLM은

권한을 절대 판단하지 않는다.

허용된 Chunk만 전달한다.

---

# 14. Future Expansion

현재 구조는

다음 기능을 추가할 수 있도록 설계한다.

OCR

Redis

Collection

Agent

Workflow

GPU

SSO

Teams

Slack

Outlook

Document Compare

Version Diff

---

# 15. Architecture Decision Record (ADR)

## ADR-001

NAS를 Source of Truth로 사용한다.

이유

문서 이중화를 방지한다.

---

## ADR-002

Repository Pattern을 사용하지 않는다.

이유

프로젝트 규모에서 불필요한 추상화이며, Service + SQLAlchemy만으로 충분하다.

---

## ADR-003

UnitOfWork를 사용하지 않는다.

이유

트랜잭션 범위가 단순하며 SQLAlchemy Session으로 충분히 관리 가능하다.

---

## ADR-004

File과 FileVersion을 분리한다.

이유

답변 재현성과 감사(Audit)를 지원하기 위함이다.

---

## ADR-005

Evidence를 필수로 저장한다.

이유

AI 답변의 신뢰성과 추적성을 확보하기 위함이다.

---

## ADR-006

SearchSession을 독립 엔티티로 관리한다.

이유

검색 범위, 검색 결과, 성능 분석, RAG 튜닝을 지원하기 위함이다.

---

# 16. GPT Context

새로운 GPT는 다음 사실을 반드시 기억해야 한다.

이 프로젝트는 Upload 기반 RAG가 아니다.

NAS가 Source of Truth이다.

Backend가 권한을 검사한다.

ChatService가 전체 흐름을 제어한다.

RAG는 ChatService 내부 기능이다.

Evidence는 반드시 생성한다.

답변은 반드시 재현 가능해야 한다.

Repository Pattern은 사용하지 않는다.

UnitOfWork는 사용하지 않는다.

Service 중심 구조를 유지한다.

Provider는 언제든 교체 가능해야 한다.
