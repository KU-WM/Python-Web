# Python-Web
-------------------
### myproject
#### 파이썬 웹 기초 제작
1. publisher / book 두개의 테이블 생성
2. 각각 CRUD가 가능하도록 기능 구성
#### 발생 오휴 및 해결과정
1. 자식 테이블 book 생성 후 부모 테이블 publisher 생성시 migration오류 발생
2. migration 및 database schema 삭제 후 전체 재생성으로 오류해결
-------------------
## myproject_final
#### myproject의 migration오류 해결
1. table 생성시 부모 table publisher 먼저 생성
2. publisher에 테스트 데이터 3개 정도 생성
3. 자식 table book 생성
---------------------
## ch99
#### Django admin설정 및 bookmark관리 시스템 구축
1. admin을 생성하여 관리자 페이지 생성 및 DB제어
2. ListView, DetailView를 사용하여 Django의 기본 연결 이해하기
3. bookmark_ view, detail페이지를 만들어 동작 확인하기
----------------------
## Django_project
#### 시스템 요구사항
1. DB: mysql
2. Backend: Django
3. 크롤러 개발
4. 시각화(단순 통계) => bootstrap 테마(데시보드)
5. 데이터 분석 => 추후 작업

#### 과제 요구사항
1. 잡코리아(취업 사이트 등)에서 S/W 개발 관련 취업 정보를 크롤링 한다.
2. 회사명, 구인광고 명, 경력사항, 학력, 정규직 여부, 주소 데이터 저장
3. 급여, 시간, 직급, 직책, 상세요강, 전형절차, 모집분야, 모집인원, 인사담당자, 부서명, 연락처
4. 가능하다면 지원자통계, 기업 정보