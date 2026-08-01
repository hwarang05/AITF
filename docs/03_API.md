# 03. API

Project : AITF (AI Technology Framework)

Version : v1.0

Status : Designing

---

# 1. 목적

본 문서는 AITF Backend API 명세를 정의한다.

모든 API는 RESTful 원칙을 따르며,
FastAPI Router는 본 문서를 기준으로 구현한다.

Swagger는 구현 결과이며,
본 문서가 API의 기준(SSOT)이다.

---

# 2. 공통 규칙

## Base URL

/api/v1

---

## Content-Type

application/json

---

## Authentication

JWT Bearer Token

Authorization

Bearer <token>

---

## Response Format

모든 API는 동일한 응답 형식을 사용한다.

성공

{
    "success": true,
    "data": {},
    "message": null
}

실패

{
    "success": false,
    "data": null,
    "message": "Error Message"
}

---

## HTTP Status

200

성공

201

생성 성공

204

삭제 성공

400

잘못된 요청

401

인증 실패

403

권한 없음

404

리소스 없음

409

충돌

500

서버 오류

---

# 3. Authentication API

================================================

POST

/auth/login

================================================

Purpose

사용자 로그인

DSM 인증 수행

---

Request

username

password

---

Response

access_token

refresh_token

user

---

Flow

Login

↓

DSM 인증

↓

JWT 생성

↓

Response

================================================

POST

/auth/logout

================================================

Purpose

로그아웃

Refresh Token 제거

---

# 4. NAS API

================================================

GET

/nas/tree

================================================

Purpose

사용자가 접근 가능한

Folder Tree 조회

---

Response

Folder

File

Children

Permission

---

================================================

GET

/nas/file

================================================

Purpose

파일 메타데이터 조회

---

Response

Name

Path

Size

Modified Time

Hash

---

# 5. Chat API

================================================

POST

/chat

================================================

Purpose

AI 질의응답

---

Request

question

folders

files

conversation_id

---

Flow

SearchSession 생성

↓

Sync

↓

Search

↓

LLM

↓

Evidence

↓

Response

---

Response

assistant_message

conversation_id

message_id

reference_files

---

# 6. Conversation API

================================================

GET

/conversations

================================================

Purpose

대화 목록 조회

---

================================================

POST

/conversations

================================================

Purpose

새 대화 생성

---

================================================

GET

/conversations/{id}

================================================

Purpose

대화 상세 조회

---

================================================

DELETE

/conversations/{id}

================================================

Purpose

대화 삭제

---

# 7. Message API

================================================

GET

/messages/{id}

================================================

Purpose

메시지 조회

---

================================================

DELETE

/messages/{id}

================================================

Purpose

메시지 삭제

---

# 8. Evidence API

================================================

GET

/messages/{id}/evidence

================================================

Purpose

답변 근거 조회

---

Response

File

Folder

Version

Chunk

Citation Order

---

# 9. SearchSession API

================================================

GET

/search-sessions/{id}

================================================

Purpose

검색 이력 조회

---

Response

Question

Search Scope

Search Time

Sync Result

Search Result Count

---

# 10. SearchResult API

================================================

GET

/search-sessions/{id}/results

================================================

Purpose

검색 결과 조회

---

Response

Rank

Score

Chunk

Selected

---

# 11. Health API

================================================

GET

/health

================================================

Purpose

서비스 상태 확인

---

Response

Backend

SQLite

ChromaDB

Ollama

NAS

---

# 12. Error Policy

Business Logic에서 발생하는 예외는

AppException을 사용한다.

FastAPI Router에서는

HTTPException을 직접 발생시키지 않는다.

Exception Handler가

AppException을 HTTP Response로 변환한다.

---

# 13. Validation

모든 Request는

Pydantic Schema를 사용한다.

Router에서 Validation을 수행한다.

Service는 Validation을 수행하지 않는다.

---

# 14. API Design Rules

API는 Service만 호출한다.

Router에서

Business Logic을 작성하지 않는다.

Provider를 직접 호출하지 않는다.

Database를 직접 접근하지 않는다.

---

# 15. Future API

향후 추가 예정

Collection

Document Compare

Prompt Template

Workflow

Admin

Statistics

Audit

Model Management

---

# 16. GPT Context

새로운 GPT는 반드시 다음 규칙을 따른다.

FastAPI Router는 얇게 유지한다.

Business Logic은 Service에서 수행한다.

Provider는 Router에서 호출하지 않는다.

모든 API는 AppException을 사용한다.

Swagger보다 본 문서를 우선한다.
