# 01. Project

**Project Name** : AITF (AI Technology Framework)

**Version** : v0.1

**Status** : Designing

**Author** : 박기태

**Last Updated** : 2026-07-29

---

# 1. 프로젝트 개요

## 1.1 프로젝트 소개

AITF(AI Technology Framework)는 Synology NAS에 저장된 기업 문서를 AI 기반으로 검색하고 질의응답할 수 있는 Enterprise Knowledge Platform이다.

사용자는 자연어로 질문을 입력하면 AI가 관련 문서를 검색(RAG)하여 답변을 생성하며, 모든 문서 접근은 기존 Synology DSM 권한을 그대로 유지한다.

본 프로젝트는 개인 프로젝트로 시작하지만, 향후 사내 시스템으로 확장 가능한 구조를 목표로 개발한다.

---

## 1.2 프로젝트 목표

본 프로젝트의 목표는 다음과 같다.

- 기업 문서를 AI를 이용하여 효율적으로 검색할 수 있는 환경 구축
- Synology DSM 권한 체계를 그대로 활용
- Local LLM 기반 AI 서비스 구축
- 유지보수가 쉬운 모듈형 구조 설계
- 향후 기능 확장이 가능한 아키텍처 구축

---

# 2. 프로젝트 범위

## 포함 기능 (v1)

- 사용자 로그인
- Synology DSM 인증
- 문서 탐색
- 문서 색인(Indexing)
- RAG 기반 문서 검색
- AI 질의응답(Chat)
- 대화 저장
- 감사 로그(Audit Log)

---

## 제외 기능 (v1)

다음 기능은 현재 개발 범위에 포함하지 않는다.

- 모바일 앱
- 음성 입력
- Teams 연동
- Slack 연동
- Outlook 연동
- 다국어 지원
- ERP 연동

---

# 3. 프로젝트 핵심 기능

## Authentication

사용자는 Synology DSM 계정으로 로그인한다.

별도의 사용자 계정을 관리하지 않는다.

---

## Authorization

문서 접근 권한은 반드시 Synology DSM 권한을 따른다.

AITF는 자체 권한 시스템을 구현하지 않는다.

---

## Document Search

사용자의 질문과 관련된 문서를 검색한다.

검색은 Vector Database(Qdrant)를 이용한다.

---

## AI Chat

검색된 문서를 기반으로 AI가 답변을 생성한다.

LLM은 검색된 Context만 전달받는다.

---

## Conversation

사용자의 대화 내역을 저장한다.

향후 대화 이어하기 기능을 지원한다.

---

## Audit Log

다음 항목을 기록한다.

- 로그인
- 검색
- 질문
- 답변
- 문서 접근

---

# 4. 설계 원칙

AITF는 다음 원칙을 반드시 따른다.

## 1. Interface First

구현보다 인터페이스를 먼저 설계한다.

---

## 2. Backend First

모든 Business Logic은 Backend에서 수행한다.

Frontend는 화면 표시 역할만 담당한다.

---

## 3. LLM은 권한을 판단하지 않는다.

LLM은

- 권한 확인
- 문서 검색
- 사용자 인증

을 수행하지 않는다.

LLM은 Backend가 전달한 Context만 이용하여 답변을 생성한다.

---

## 4. Security First

권한 검사는 반드시 Backend에서 수행한다.

허용되지 않은 문서는 LLM으로 전달하지 않는다.

---

## 5. Loose Coupling

각 기능은 서로 독립적으로 동작해야 한다.

특정 구현체에 의존하지 않는다.

---

## 6. Replaceable Provider

다음 Provider는 언제든 교체 가능해야 한다.

- LLM
- Embedding
- OCR
- Vector Database

---

# 5. 기술 스택

## Backend

- Python
- FastAPI

## Frontend

- React
- TypeScript

## Database

- PostgreSQL

## Vector Database

- Qdrant

## LLM

- Ollama

## Container

- Docker Compose

## Storage

- Synology NAS

---

# 6. 디렉터리 구조

```
AITF/

backend/
frontend/
docs/
docker/
scripts/
tests/
assets/
config/
```

---

# 7. 개발 철학

AITF는 단순한 AI 챗봇이 아니다.

기업에서 장기간 운영 가능한 Knowledge Platform을 목표로 한다.

코드의 양보다 구조를 우선하며, 구현보다 설계를 먼저 진행한다.

유지보수성과 확장성을 최우선 가치로 한다.

---

# 8. 향후 확장 계획

향후 다음 기능을 추가할 수 있도록 설계한다.

- GPU 기반 AI 서버
- 다중 LLM 지원
- 음성 인터페이스
- OCR 자동화
- Webhook
- Teams 연동
- Slack 연동
- Outlook 연동
- 모바일 지원

---

# 9. 개발 단계

Phase 1

- 프로젝트 설계
- 아키텍처 설계
- 인터페이스 설계

Phase 2

- Backend 개발
- Database 구축
- Synology 연동

Phase 3

- RAG 구축
- LLM 연동

Phase 4

- Frontend 개발
- 관리자 기능

Phase 5

- 테스트
- 성능 개선
- 운영 준비