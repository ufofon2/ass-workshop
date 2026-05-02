<!--
Sync Impact Report
Version change: [UNKNOWN] -> 1.0.0
Modified principles:
- [PRINCIPLE_1_NAME] -> 레이어 분리
- [PRINCIPLE_2_NAME] -> 테스트 우선
- [PRINCIPLE_3_NAME] -> 최소 의존성
- [PRINCIPLE_4_NAME] -> 단순함 우선
- [PRINCIPLE_5_NAME] -> CLI 도구 구현
Added sections: None
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending (review and emphasise CLI-only project type; remove web-app options)
- .specify/templates/spec-template.md: ⚠ pending (clarify input constraints: CLI-only, no REST/GUIs)
- .specify/templates/tasks-template.md: ⚠ pending (ensure "테스트 우선" 항목이 반영되어야 함)
Follow-up TODOs:
- TODO(RATIFICATION_DATE): Ratification date 미정 — 실무팀에서 확정 필요
-->

# Project Constitution: CLI 기반 ToDo 관리 앱

## Core Principles

### 1. 레이어 분리
비즈니스 로직은 사용자 인터페이스와 분리된 독립 레이어에서 구현되어야 한다. CLI 입력/출력은 인터페이스 계층에 한정하고, 서비스·도메인·데이터 접근은 별도의 레이어로 캡슐화해야 한다. 이 원칙은 모듈화, 테스트 용이성, 교체 용이성을 위해 반드시 지켜져야 한다.

### 2. 테스트 우선 (NON-NEGOTIABLE)
모든 구현은 테스트 코드가 먼저 작성된 상태에서 시작한다.테스트 없는 구현 코드는 허용되지 않으며, 기능을 추가할 때는 관련 단위 테스트(unit test)와 필요한 통합 테스트(integration test)를 먼저 작성하고 실패 상태를 확인한 뒤 구현한다.테스트는 자동화되어야 한다.

### 3. 최소 의존성
외부 패키지(특히 웹 관련 패키지)는 설치 전에 반드시 필요성을 검토해야 한다.REST API나 GUI 관련 라이브러리는 본 프로젝트 범위 밖이며, 불필요한 의존성은 추가하지 않는다.의존성 추가 시 비용(보안, 빌드복잡도, 유지보수)을 문서화해야 한다.

### 4. 단순함 우선
지금 당장 필요하지 않은 추상화 레이어는 만들지 않는다.명확하고 직접적인 구현을 우선으로 하며, YAGNI(You Aren't Gonna Need It) 원칙을 따른다.향후 필요성이 명확해질 때에만 추상화를 도입한다.

### 5. CLI 도구 구현 범위(스코프)
이 프로젝트는 터미널에서 사용하는 CLI 기반 생산성 도구로서 ToDo 관리 기능을 제공한다.REST API 서버나 GUI 웹 인터페이스는 이 프로젝트의 범위에 포함되지 않으며, 향후 별도 프로젝트로 분리된다.

## Constraints & Project Scope
- 프로젝트 타입: CLI 애플리케이션 (터미널 중심)
- 네트워크 인터페이스: 로컬 파일 또는 필요 시 경량 스토리지(예: 파일, 로컬 DB) 허용. 원격 REST API 연동은 범위 외.
- 사용자 인터페이스: 표준 입출력(stdin/stdout) 및 명령행 인자 기반으로 동작.
- 의존성 정책: 모든 신규 의존성은 PR에서 적절한 이유와 대체재 검토를 포함해야 함.

## Development Workflow
- 브랜치 전략: 기능 단위 브랜치 생성 후 PR 제출
- 테스트: 모든 PR은 자동화된 테스트 파이프라인을 통과해야 함(단위 테스트 최소 포함)
- 코드 리뷰: 레이어 분리, 테스트 우선, 최소 의존성 준수 여부를 검토 항목에 포함

## Governance
헌법 변경 절차: 헌법 변경(수정, 원칙 추가/삭제)은 문서화된 제안서(변경 사유, 영향 분석, 마이그레이션 계획)를 통해 리뷰를 거쳐 승인을 받아야 한다.중대한(비호환) 변경은 MAJOR 버전 증가를 요구한다.

버전 규칙:
- MAJOR: 거버넌스 또는 원칙의 호환성 파괴적 변경
- MINOR: 원칙 추가 또는 중요 항목의 확장
- PATCH: 문구 수정, 오탈자, 비기능적 규정의 정리

승인 관련 날짜 및 버전:
**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): 실무팀에서 확정 필요 | **Last Amended**: 2026-05-02

<!-- End of constitution -->
