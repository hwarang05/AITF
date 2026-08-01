## 2026-08-01

### 완료 작업
- Authentication API 구현
- User 모델 생성

### 설계 결정(ADR)
- Repository Pattern을 사용하지 않기로 확정
- SearchSession 엔티티 추가

### 이유
- Service 중심 구조 유지
- 검색 이력과 RAG 튜닝 지원

### 다음 작업
- SQLAlchemy 모델 구현