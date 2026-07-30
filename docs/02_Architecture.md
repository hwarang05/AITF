# 02. Architecture

**Project Name** : AITF (AI Technology Framework)

**Version** : v0.1

---

# 1. Architecture Overview

AITF는 AI 기반 기업 문서 검색 및 질의응답 시스템이다.

Frontend와 Backend를 완전히 분리하며,
모든 Business Logic은 Backend에서 처리한다.

LLM은 답변 생성만 담당하며,
권한 확인 및 문서 검색은 수행하지 않는다.

---

# 2. High Level Architecture

```text
                        User
                         │
                         ▼
                 React Frontend
                         │
                    REST API
                         │
                         ▼
                  FastAPI Backend
                         │
 ┌───────────────────────┼────────────────────────┐
 │                       │                        │
 ▼                       ▼                        ▼
Auth Service      Chat Service          Document Service
 │                       │                        │
 │                       ▼                        │
 │                Search Service                  │
 │                       │                        │
 └───────────────┬───────┴────────────────────────┘
                 │
                 ▼
            Provider Layer
                 │
 ┌───────────────┼─────────────────────────────────┐
 ▼               ▼                ▼                ▼
Synology      PostgreSQL      Qdrant          Ollama
```

---

# 3. Layer Architecture

AITF는 다음 계층으로 구성된다.

```
Presentation Layer

↓

Application Layer

↓

Service Layer

↓

Provider Layer

↓

Infrastructure
```

---

## 3.1 Presentation Layer

구성

- React
- TypeScript

역할

- 사용자 화면
- 입력 처리
- API 호출

Business Logic을 포함하지 않는다.

---

## 3.2 Application Layer

FastAPI Endpoint를 제공한다.

예시

```
POST /chat

POST /login

GET /documents

GET /history
```

역할

- Request 수신
- Validation
- Service 호출
- Response 반환

---

## 3.3 Service Layer

프로젝트의 핵심 계층이다.

Business Logic을 수행한다.

예시

- ChatService
- AuthService
- SearchService
- DocumentService
- ConversationService
- AdminService

---

## 3.4 Provider Layer

외부 시스템과 통신한다.

예시

Synology Provider

Qdrant Provider

Ollama Provider

PostgreSQL Provider

Provider를 교체해도
Service Layer는 변경되지 않는다.

---

## 3.5 Infrastructure

실제 시스템

- Synology NAS
- PostgreSQL
- Ollama
- Qdrant

---

# 4. Component

## Frontend

역할

- 사용자 인터페이스
- 채팅 화면
- 최근 대화
- 로그인
- 관리자 페이지

---

## Backend

역할

- 인증
- 권한
- 검색
- AI 요청
- 대화 저장

---

## Synology

역할

- 문서 저장
- 사용자 권한
- LDAP/DSM 인증

---

## PostgreSQL

역할

- 사용자 정보
- 대화
- 로그
- 시스템 설정

---

## Qdrant

역할

- Embedding 저장
- Vector Search

---

## Ollama

역할

- AI 답변 생성

---

# 5. Chat Flow

사용자가 질문을 입력하면
다음 순서로 처리된다.

```
User

↓

React

↓

POST /chat

↓

ChatService

↓

권한 확인

↓

SearchService

↓

Qdrant 검색

↓

검색 결과 반환

↓

Context 생성

↓

Ollama

↓

AI 답변

↓

대화 저장

↓

React 응답
```

---

# 6. Security Architecture

권한 확인은 반드시 Backend에서 수행한다.

LLM은

- 사용자 정보
- 권한 정보
- NAS

에 직접 접근하지 않는다.

허용된 문서만 Context에 포함된다.

---

# 7. Design Principles

AITF는 다음 원칙을 따른다.

- Interface First
- Backend First
- Security First
- Loose Coupling
- Replaceable Provider
- Single Responsibility
- Dependency Injection

---

# 8. Future Expansion

향후 다음 기능을 쉽게 추가할 수 있도록 설계한다.

- OCR
- 음성 인식
- 다중 LLM
- Redis Cache
- SSO
- Teams
- Slack
- Outlook
- AI Agent