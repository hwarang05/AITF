# 04. ERD

Project : AITF (AI Technology Framework)

Version : v1.0

Status : Designing

---

# 1. 목적

본 문서는 AITF의 데이터베이스 구조를 정의한다.

ERD는 단순한 테이블 정의가 아니라

- Entity의 역할
- 관계(Relationship)
- 생명주기(Lifecycle)
- 설계 이유(Design Decision)

까지 포함한다.

모든 SQLAlchemy Model은 본 문서를 기준으로 구현한다.

---

# 2. ERD Overview

User
 │
 └──────────────┐
                │
         Conversation
                │
                ▼
         SearchSession
                │
      ┌─────────┴──────────┐
      ▼                    ▼
 SearchResult          Message
      │                    │
      ▼                    ▼
    Chunk ─────────────► Evidence
      │
      ▼
 FileVersion
      │
      ▼
    File

---

# 3. Entity

====================================================

User

====================================================

## Purpose

AITF 사용자

Authentication 정보를 가진다.

현재는 DSM Login을 사용하지만
향후 SSO로 변경 가능하다.

---

Columns

id

username

display_name

created_at

updated_at

---

Relationship

User

↓

Conversation

(1:N)

====================================================

Conversation

====================================================

Purpose

채팅방

사용자의 여러 질문을 하나의 주제로 관리한다.

---

Columns

id

user_id

title

created_at

updated_at

---

Relationship

Conversation

↓

SearchSession

(1:N)

====================================================

SearchSession

====================================================

Purpose

질문 1회에 대한 검색 작업

검색 범위

Sync 결과

검색 성능

검색 시간을 관리한다.

---

Columns

id

conversation_id

question

selected_folders

selected_files

model

embedding_model

sync_file_count

searched_chunk_count

started_at

finished_at

created_at

---

Relationship

Conversation

↓

SearchSession

SearchSession

↓

SearchResult

SearchSession

↓

Message

---

Lifecycle

질문

↓

SearchSession 생성

↓

Sync

↓

Vector Search

↓

LLM

↓

Message 저장

====================================================

SearchResult

====================================================

Purpose

Vector Search 결과

LLM이 사용하지 않은 결과도 저장한다.

RAG 품질 분석에 이용된다.

---

Columns

id

search_session_id

chunk_id

score

rank

selected

created_at

---

selected

True

↓

Prompt 포함

False

↓

검색만 됨

====================================================

Message

====================================================

Purpose

채팅 메시지

질문 또는 답변

---

Columns

id

conversation_id

search_session_id

role

content

created_at

---

role

USER

ASSISTANT

SYSTEM

---

Relationship

Message

↓

Evidence

====================================================

Evidence

====================================================

Purpose

AI 답변의 근거

답변 당시 사용한 Chunk를 기록한다.

Evidence가 없는 답변은 허용하지 않는다.

---

Columns

id

message_id

chunk_id

citation_order

created_at

---

Relationship

Message

↓

Evidence

Evidence

↓

Chunk

====================================================

File

====================================================

Purpose

NAS 파일

논리적인 파일(Entity)

내용은 저장하지 않는다.

---

Columns

id

nas_path

folder_path

filename

extension

created_at

updated_at

---

Relationship

File

↓

FileVersion

====================================================

FileVersion

====================================================

Purpose

파일의 특정 시점

Version 관리

답변 재현

Audit

---

Columns

id

file_id

version

hash

size

modified_time

referenced

created_at

---

referenced

False

↓

삭제 가능

True

↓

삭제 금지

---

Relationship

FileVersion

↓

Chunk

====================================================

Chunk

====================================================

Purpose

검색 가능한 최소 단위

Embedding 생성 대상

---

Columns

id

file_version_id

chunk_index

content

token_count

embedding_id

created_at

---

Relationship

Chunk

↓

Evidence

Chunk

↓

SearchResult

---

# 4. Lifecycle

Question

↓

SearchSession 생성

↓

NAS Sync

↓

Hash 비교

↓

Version 생성

↓

Chunk 생성

↓

Embedding 생성

↓

Vector 저장

↓

Vector Search

↓

SearchResult 저장

↓

Prompt 생성

↓

LLM

↓

Message 저장

↓

Evidence 저장

---

# 5. Version Policy

File은 삭제하지 않는다.

Version은 다음 규칙을 따른다.

referenced=False

↓

삭제 가능

referenced=True

↓

영구 보관

---

# 6. Search Policy

검색은

선택한 Folder/File

범위에서만 수행한다.

전체 NAS 검색은 수행하지 않는다.

---

# 7. Evidence Policy

모든 답변은 Evidence를 가진다.

Evidence는

Chunk

↓

FileVersion

↓

File

을 항상 따라갈 수 있어야 한다.

---

# 8. Design Decision

ADR-001

File과 FileVersion을 분리한다.

이유

답변 재현

Version 관리

Audit

---

ADR-002

Chunk는 File이 아니라

FileVersion을 참조한다.

이유

과거 답변 복원

---

ADR-003

SearchResult를 별도 관리한다.

이유

검색 품질 분석

Top-K 실험

RAG 튜닝

---

ADR-004

Evidence는 답변에 사용된 Chunk만 저장한다.

검색 결과 전체는 SearchResult가 관리한다.

---

ADR-005

SearchSession을 독립 Entity로 둔다.

이유

검색 범위

검색 성능

Sync 결과

추적 가능

---

# 9. Future Expansion

향후 다음 Entity를 추가할 수 있다.

Collection

DocumentCompare

AuditLog

Workflow

PromptTemplate

ModelHistory

OCRJob

AgentTask

---

# 10. GPT Context

새로운 GPT는 반드시 다음 내용을 따른다.

ERD는 프로젝트의 기준이다.

SQLAlchemy Model은 본 문서를 따른다.

Relationship은 변경하지 않는다.

FileVersion 구조를 유지한다.

Evidence를 제거하지 않는다.

SearchSession을 제거하지 않는다.

SearchResult를 제거하지 않는다.

Chunk는 FileVersion을 참조한다.

답변은 반드시 재현 가능해야 한다.