# 00. RULE

Project : AITF (AI Technology Framework)

Version : v1.0

Status : Active

---

# 목적

이 문서는 AITF 프로젝트의 최상위 규칙(Constitution)이다.

본 문서에 정의된 내용은 프로젝트 전체에서 항상 우선한다.

새로운 기능을 추가하거나 구조를 변경하더라도 본 문서의 원칙은 유지되어야 한다.

---

# 1. 프로젝트 철학

AITF는 단순한 AI Chatbot이 아니다.

AITF는 기업 문서를 기반으로 한 Enterprise AI Knowledge Platform이다.

목표는 AI 답변이 아니라,

"신뢰할 수 있는 답변"

을 제공하는 것이다.

모든 설계는 다음 원칙을 따른다.

- 유지보수성
- 확장성
- 재현성
- 보안
- 감사(Audit)

---

# 2. Source of Truth

Synology NAS가 유일한 원본(Source of Truth)이다.

AITF는 문서를 저장하지 않는다.

AITF는 검색을 위한 메타데이터와 Index만 저장한다.

즉,

NAS

↓

AITF

이며

AITF

↓

NAS

구조는 존재하지 않는다.

---

# 3. NAS 권한

AITF는 자체 권한 시스템을 만들지 않는다.

모든 권한은 Synology DSM 권한을 그대로 사용한다.

Backend는 NAS 권한을 확인한 후

허용된 문서만 검색한다.

LLM은 권한을 절대 판단하지 않는다.

---

# 4. Backend First

모든 Business Logic은 Backend(Service Layer)에 존재한다.

Frontend는

- 화면 표시
- 사용자 입력
- API 호출

만 담당한다.

Business Logic은 포함하지 않는다.

---

# 5. Service Pattern

AITF는 Service 중심 구조를 사용한다.

API

↓

Service

↓

Provider

↓

External System

Repository Pattern은 사용하지 않는다.

UnitOfWork도 사용하지 않는다.

Database 접근은 Service에서 SQLAlchemy Session을 이용한다.

---

# 6. Provider Pattern

외부 시스템은 반드시 Provider를 통해 접근한다.

예시

- Ollama
- ChromaDB
- Synology
- Embedding Model

Provider는 언제든 교체 가능해야 한다.

Service는 Provider 구현체를 직접 알지 않는다.

---

# 7. RAG

AITF는 Upload 기반 RAG가 아니다.

모든 문서는 NAS에서 선택된다.

동작 순서

사용자

↓

NAS Tree 조회

↓

폴더 선택

↓

질문

↓

Sync

↓

Vector Search

↓

LLM

↓

Answer

---

# 8. Sync

질문이 들어오면

선택된 범위만 Sync한다.

전체 NAS를 Index하지 않는다.

Sync는

Hash 기반 변경 감지

를 사용한다.

Hash가 동일하면 재색인을 수행하지 않는다.

---

# 9. File Version

File과 FileVersion은 반드시 분리한다.

File

↓

FileVersion

↓

Chunk

Chunk는 File이 아니라

FileVersion을 참조한다.

---

# 10. Evidence

모든 AI 답변은 Evidence를 가진다.

Evidence는

Message

↓

Chunk

↓

FileVersion

↓

File

관계를 유지해야 한다.

Evidence가 없는 답변은 허용하지 않는다.

---

# 11. Answer Reproducibility

AITF는 모든 답변을 재현할 수 있어야 한다.

답변 당시

- 파일
- 버전
- Chunk

를 확인할 수 있어야 한다.

파일이 수정되어도

과거 답변은 그대로 재현 가능해야 한다.

---

# 12. Security

LLM은

- NAS 접근
- 권한 확인
- 사용자 인증

을 수행하지 않는다.

LLM은 Backend가 전달한 Context만 이용한다.

---

# 13. Logging

다음 작업은 반드시 기록한다.

- Login

- Chat

- Search

- Sync

- Error

- AI Response

- Evidence

---

# 14. Design Principles

항상 다음 원칙을 유지한다.

Single Responsibility

Loose Coupling

Replaceable Provider

Backend First

Security First

Evidence First

Reproducibility First

---

# 15. Coding Rules

Business Logic → Service

External Access → Provider

Entity → SQLAlchemy Model

DTO → Pydantic Schema

API → FastAPI Router

Configuration → core/

공통 함수 → utils/

Parser → parsers/

---

# 16. Documentation Rules

새로운 기능은 반드시 다음 문서를 수정한다.

Project

Architecture

ERD

API

RAG

TODO

DevLog

문서를 수정하지 않는 기능 추가는 허용하지 않는다.

---

# 17. Future Expansion

향후 다음 기능을 추가하더라도

본 문서는 변경하지 않는다.

- OCR

- Agent

- Redis

- Teams

- Slack

- Outlook

- Multi LLM

- GPU Server

모든 기능은 본 규칙을 따른다.