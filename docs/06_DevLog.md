## 2026-07-30

### AI Framework 설계

- Provider 패턴을 적용하여 LLM 교체가 가능하도록 설계
- API는 Provider를 직접 호출하지 않고 Service를 통해 접근
- 향후 OpenAI, Ollama, Gemini, Claude를 동일한 인터페이스로 지원 예정

## 2026-07-30

### Authentication API 생성

- User Entity 생성
- Authentication Router 추가
- LoginRequest / LoginResponse Schema 생성
- Swagger Login API 연동
- 프로젝트 API 구조 정리