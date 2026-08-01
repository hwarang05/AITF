# 05. RAG

Project : AITF (AI Technology Framework)

Version : v1.0

Status : Designing

---

# 1. 목적

본 문서는 AITF의 RAG(Retrieval-Augmented Generation) 구조를 정의한다.

AITF는 일반적인 Upload 기반 RAG가 아니다.

AITF의 RAG는

- Synology NAS
- Permission
- Incremental Sync
- Version
- Evidence
- Reproducibility

를 중심으로 설계된다.

본 문서는 RAG 구현의 기준 문서(SSOT)이다.

---

# 2. RAG Overview

AITF의 RAG는 다음 순서로 동작한다.

Question

↓

NAS Sync

↓

Index

↓

Embedding

↓

Vector Search

↓

Prompt

↓

LLM

↓

Answer

↓

Evidence

기존 Upload 기반 RAG와 달리

문서를 업로드하지 않는다.

---

# 3. Source of Truth

AITF의 원본은

Synology NAS이다.

NAS

↓

AITF

AITF는

문서를 저장하지 않는다.

저장하는 것은

- Metadata
- Embedding
- Version
- Evidence

뿐이다.

---

# 4. Search Scope

사용자는

먼저

NAS Tree

를 조회한다.

그 후

Folder

또는

File

을 선택한다.

검색은

선택한 범위에서만 수행한다.

예시

☑ 공용

□ 인사

☑ 규정

↓

검색 범위

/공용

/공용/규정

전체 NAS 검색은 수행하지 않는다.

---

# 5. Incremental Sync

질문이 들어오면

선택한 범위만 Sync한다.

Flow

Folder

↓

NAS 조회

↓

Hash 비교

↓

동일

↓

Skip

----------------

Hash 변경

↓

새 FileVersion 생성

↓

Chunk 생성

↓

Embedding 생성

↓

Vector 저장

---

# 6. Version

File

↓

FileVersion

↓

Chunk

Chunk는

FileVersion을 참조한다.

Version은

Hash

Modified Time

Size

를 가진다.

Version이 변경되면

새로운 Chunk를 생성한다.

기존 Chunk는 삭제하지 않는다.

---

# 7. Chunk

Chunk는

검색 가능한 최소 단위이다.

Chunk는

- FileVersion
- Index
- Token Count

를 가진다.

Chunk는

Embedding 생성 대상이다.

---

Chunk 생성 예시

Document

↓

Chunk 1

Chunk 2

Chunk 3

Chunk 4

---

# 8. Embedding

Chunk 생성 후

Embedding을 수행한다.

Embedding Provider는

언제든 교체 가능하다.

현재

Ollama Embedding

사용

향후

OpenAI

BGE

E5

지원 가능

---

# 9. Vector Search

질문

↓

Embedding

↓

ChromaDB

↓

Top K

↓

SearchResult 저장

↓

Prompt 생성

---

SearchResult는

검색 결과 전체를 저장한다.

LLM이 선택하지 않은 Chunk도 저장한다.

---

# 10. Prompt

Prompt는

Backend에서 생성한다.

LLM은

Prompt를 그대로 이용한다.

Prompt 구성

System Prompt

↓

Retrieved Context

↓

Question

↓

Instruction

LLM은

Context 외의 문서를 참조하지 않는다.

---

# 11. LLM

LLM의 역할은

답변 생성뿐이다.

LLM은

- 권한 확인

- NAS 접근

- 문서 검색

을 수행하지 않는다.

현재

Ollama 사용

Provider Pattern을 이용한다.

---

# 12. Evidence

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

Evidence는

답변 당시 사용한 Chunk를 기록한다.

---

# 13. Reproducibility

AITF는

모든 답변을

재현할 수 있어야 한다.

필요한 정보

Question

↓

SearchResult

↓

Chunk

↓

FileVersion

↓

Evidence

↓

Answer

이를 통해

몇 년이 지나도

답변 당시 문서를 복원할 수 있다.

---

# 14. SearchSession

질문 하나마다

SearchSession을 생성한다.

SearchSession은

- 검색 범위

- 사용 모델

- Sync 결과

- 검색 시간

- SearchResult

를 관리한다.

---

# 15. SearchResult

Vector Search 결과

Top K를 저장한다.

예시

Rank

Score

Chunk

Selected

Selected=False인 결과도 저장한다.

이는

검색 품질 분석

RAG 튜닝

Top-K 실험

에 사용된다.

---

# 16. Sync Policy

Hash가 같으면

재색인하지 않는다.

Hash가 변경되면

새로운 Version을 생성한다.

Version은

referenced=False

이면 삭제 가능하다.

Evidence가 참조하는 Version은

삭제하지 않는다.

---

# 17. Prompt Policy

Prompt에는

허용된 Chunk만 포함한다.

Prompt 길이는

Model Context Window를 넘지 않는다.

Prompt 구성은

PromptBuilder에서 관리한다.

Service에서 직접 문자열을 만들지 않는다.

---

# 18. Error Policy

Embedding 실패

↓

재시도

↓

실패 기록

↓

검색 제외

----------------

Vector Search 실패

↓

에러 반환

----------------

LLM 실패

↓

답변 실패 기록

↓

Evidence 생성 안 함

---

# 19. Future Expansion

향후 지원

Hybrid Search

BM25

Keyword Search

Re-ranking

Cross Encoder

Redis Cache

Prompt Cache

Agent

Workflow

Collection

Document Compare

Version Diff

OCR

---

# 20. Design Decision

ADR-001

Upload 기반 RAG를 사용하지 않는다.

이유

NAS가 원본이기 때문이다.

---

ADR-002

질문 시 Incremental Sync를 수행한다.

이유

항상 최신 문서를 검색하기 위함이다.

---

ADR-003

Chunk는 FileVersion을 참조한다.

이유

답변 재현을 위해서이다.

---

ADR-004

SearchResult를 저장한다.

이유

검색 품질을 분석하기 위함이다.

---

ADR-005

Evidence는 필수이다.

근거 없는 AI 답변은 허용하지 않는다.

---

ADR-006

Prompt는 Backend에서 생성한다.

LLM은 Prompt를 수정하지 않는다.

---

# 21. GPT Context

새로운 GPT는 반드시 다음 사실을 기억한다.

AITF는 Upload 기반 RAG가 아니다.

NAS가 Source of Truth이다.

질문마다 Incremental Sync를 수행한다.

Chunk는 FileVersion을 참조한다.

SearchResult를 저장한다.

Evidence를 생성한다.

답변은 반드시 재현 가능해야 한다.

Prompt는 Backend가 생성한다.

LLM은 답변 생성만 담당한다.

Provider는 언제든 교체 가능하다.
