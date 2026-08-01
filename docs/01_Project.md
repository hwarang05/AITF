# 01. Project

Project Name : AITF (AI Technology Framework)

Version : v1.0

Status : Designing

Author : 박기태

---

# 1. 프로젝트 소개

## 1.1 프로젝트 개요

AITF(AI Technology Framework)는 기업 내부 문서를 AI가 검색하고 분석하여 사용자의 질문에 답변하는 Enterprise AI Knowledge Platform이다.

AITF는 일반적인 ChatGPT 서비스가 아니다.

기업 환경에서 필요한 다음 요구사항을 만족하는 것을 목표로 한다.

- 기업 문서 검색
- 권한 기반 접근 제어
- AI 기반 질의응답
- 답변 근거(Evidence) 제공
- 답변 재현(Reproducibility)
- 감사(Audit)

---

## 1.2 프로젝트 목표

AITF는 다음 목표를 가진다.

### 1. 기업 문서 검색

사용자는 자연어 질문만으로 원하는 문서를 찾을 수 있어야 한다.

예시

"연계정보 암호화 기준이 뭐야?"

↓

관련 규정 검색

↓

AI 답변

---

### 2. 기업 지식 공유

문서를 직접 찾는 것이 아니라

문서를 이해한 AI가 답변한다.

---

### 3. 답변 신뢰성 확보

모든 AI 답변은 반드시 근거를 가진다.

사용자는

- 어떤 문서를 참고했는지
- 어떤 문단을 참고했는지

확인할 수 있어야 한다.

---

### 4. 답변 재현

동일한 질문에 대해

과거 AI가 어떤 문서를 읽고 답변했는지를 재현할 수 있어야 한다.

---

### 5. 유지보수성

LLM

Embedding

Vector DB

OCR

NAS

모든 외부 시스템은 교체 가능해야 한다.

---

# 2. 프로젝트 특징

AITF는 기존 RAG 프로젝트와 다음 차이점을 가진다.

## 2.1 Upload 기반이 아니다.

문서는 업로드하지 않는다.

모든 문서는 Synology NAS에 존재한다.

AITF는 검색(Index)만 수행한다.

---

## 2.2 NAS가 원본이다.

Source of Truth

↓

Synology NAS

AITF는

- Metadata
- Embedding
- Evidence

만 저장한다.

---

## 2.3 권한은 NAS를 따른다.

AITF는 자체 권한을 만들지 않는다.

모든 권한은 DSM 권한을 그대로 이용한다.

---

## 2.4 변경 파일만 Index

질문 시

선택한 범위만 Sync한다.

Hash가 동일하면

재색인을 수행하지 않는다.

---

## 2.5 답변 재현

파일이 수정되어도

과거 AI 답변은 복원 가능해야 한다.

이를 위해

File

↓

FileVersion

↓

Chunk

↓

Evidence

구조를 사용한다.

---

# 3. 개발 범위

## v1

포함 기능

- 사용자 로그인
- Synology DSM 인증
- NAS Tree 조회
- 폴더 선택
- 파일 선택
- 선택 범위 Sync
- 변경 파일 Index
- Vector Search
- AI Chat
- Conversation
- Evidence
- Version 관리
- Audit Log

---

제외 기능

- OCR
- 음성 입력
- Teams
- Slack
- Outlook
- AI Agent
- 모바일 앱

---

# 4. 시스템 구성

AITF는 다음 시스템으로 구성된다.

Frontend

↓

FastAPI

↓

SQLite

↓

ChromaDB

↓

Ollama

↓

Synology NAS

각 시스템의 역할은 Architecture.md에서 정의한다.

---

# 5. 핵심 개념

프로젝트에서 사용하는 용어를 정의한다.

## NAS

기업 문서가 저장되는 원본 저장소

---

## Sync

NAS 변경 내용을 감지하여

Index를 최신 상태로 만드는 작업

---

## Index

검색을 위해 생성되는

Chunk

Embedding

Metadata

---

## Chunk

검색 가능한 최소 문단

---

## FileVersion

파일의 특정 시점

Chunk는 FileVersion을 참조한다.

---

## Evidence

AI가 실제 답변에 사용한 근거

---

## SearchSession

질문 1회에 대한 검색 작업

---

## SearchResult

검색 결과 목록

LLM이 선택하지 않은 결과도 저장한다.

---

## Conversation

사용자의 채팅방

---

## Message

질문 또는 답변

---

# 6. 설계 원칙

AITF는 다음 원칙을 반드시 따른다.

- Backend First
- Security First
- Evidence First
- Reproducibility First
- Provider Pattern
- Loose Coupling
- Single Responsibility

세부 내용은 RULE.md를 따른다.

---

# 7. 기술 스택

Backend

- Python
- FastAPI
- SQLAlchemy

Database

- SQLite

Vector Database

- ChromaDB

Frontend

- React
- TypeScript

LLM

- Ollama

Storage

- Synology NAS

Container

- Docker

---

# 8. 개발 단계

Phase 1

프로젝트 설계

Architecture

ERD

API

---

Phase 2

Authentication

NAS 연동

Database

---

Phase 3

Sync

Embedding

RAG

Chat

Evidence

---

Phase 4

Frontend

History

관리자 기능

---

Phase 5

최적화

테스트

배포

---

# 9. 성공 기준

AITF v1이 완료되면 다음 조건을 만족해야 한다.

- DSM 계정으로 로그인 가능
- NAS 권한 유지
- 폴더 선택 가능
- 변경 파일만 Index
- AI 질의응답 가능
- 답변 근거 확인 가능
- 과거 답변 재현 가능

---

# 10. 향후 확장

향후 다음 기능을 추가할 수 있도록 설계한다.

- OCR
- Multi LLM
- Redis Cache
- Agent
- Teams
- Slack
- Outlook
- GPU Server
- SSO
- Collection
- Document Compare
- Version Diff
- AI Workflow

---

# 11. GPT Context

이 프로젝트는 일반적인 Upload 기반 RAG가 아니다.

새로운 기능을 추가할 때 반드시 다음 사항을 확인한다.

- NAS가 Source of Truth인가?
- Backend가 권한을 검사하는가?
- FileVersion 구조를 유지하는가?
- Evidence를 생성하는가?
- 답변이 재현 가능한가?

위 조건을 만족하지 않는 설계는 채택하지 않는다.