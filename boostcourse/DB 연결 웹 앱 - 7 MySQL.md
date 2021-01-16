# DB 연결 웹 앱

> 1. JavaScript - FE
> 2. WEB UI 개발 - FE
> 3. JSP - BE
> 4. redirect & forward - BE
> 5. scope - BE
> 6. JSTL & EL - BE
> 7. MySQL - BE
> 8. SQL - BE
> 9. Maven - BE
> 10. JDBC - BE
> 11. WEB API - BE

# MySQL

## DBMS

특징

- 실시간 접근성(Real-time Accessability)
  \- 사용자의 요구를 즉시 처리할 수 있다.

- 계속적인 변화(Continuous Evolution)
  \- 정확한 값을 유지하려고 삽입·삭제·수정 작업 등을 이용해 데이터를 지속적으로 갱신할 수 있다.

- 동시 공유성(Concurrent Sharing)
  \- 사용자마다 서로 다른 목적으로 사용하므로 동시에 여러 사람이 동일한 데이터에 접근하고 이용할 수 있다.

- 내용 참조(Content Reference)
  \- 저장한 데이터 레코드의 위치나 주소가 아닌 사용자가 요구하는 데이터의 내용, 즉 데이터 값에 따라 참조할 수 있어야 한다.

시스템

- 데이터베이스를 관리하는 소프트웨어
- 여러 응용 소프트웨어(프로그램) 또는 시스템이 동시에 데이터베이스에 접근하여 사용할 수 있게 한다
- 필수 3기능
  \- 정의기능 :  데이터 베이스의 논리적, 물리적 구조를 정의
  \- 조작기능 : 데이터를 검색, 삭제, 갱신, 삽입, 삭제하는 기능
  \- 제어기능 :  데이터베이스의 내용 정확성과 안전성을 유지하도록 제어하는 기능
- Oracle, SQL Server, MySQL, DB2 등의 상용 또는 공개 DBMS가 있다.

# SQL

[sql이란](https://www.ciokorea.com/news/35385)

sql에 접속해서 원하는 데이터베이스를 볼려면 use db이름; 을 이용하자

1. select

   - select 컬럼 from table;

   - 컬럼을 순차적으로 `,`를 붙여서 더 볼 수 있다

   - 또한 명시적으로 확인하고 싶을 경우 `컬럼 as 명시적` 이런식으로 나열하면 된다

   - concat 문자열 결합 함수 

     - 예) `select concat(empno,'-',deptno) as '사번-부서번호' from employee;`

   - where 조건식

   - FLOOR(x) : x보다 크지 않은 가장 큰 정수를 반환합니다. BIGINT로 자동 변환합니다.

   - CEILING(x) : x보다 작지 않은 가장 작은 정수를 반환합니다.

   - ROUND(x) : x에 가장 근접한 정수를 반환합니다.

   - POW(x,y) POWER(x,y) : x의 y 제곱 승을 반환합니다.

   - GREATEST(x,y,...) : 가장 큰 값을 반환합니다.

   - LEAST(x,y,...) : 가장 작은 값을 반환합니다.

   - CURDATE(),CURRENT_DATE : 오늘 날짜를 YYYY-MM-DD나 YYYYMMDD 형식으로 반환합니다.

   - CURTIME(), CURRENT_TIME : 현재 시각을 HH:MM:SS나 HHMMSS 형식으로 반환합니다.

   - NOW(), SYSDATE() , CURRENT_TIMESTAMP : 오늘 현시각을 YYYY-MM-DD HH:MM:SS나 YYYYMMDDHHMMSS 형식으로 반환합니다. 

   - DATE_FORMAT(date,format) : 입력된 date를 format 형식으로 반환합니다.

   - PERIOD_DIFF(p1,p2) : YYMM이나 YYYYMM으로 표기되는 p1과 p2의 차이 개월을 반환합니다.

   - TRIM, LTRIM, RTRIM : 공백제거

   - 그룹함수

     ![](15.png)

2. insert

   - `INSERT INTO 테이블명(컬럼1, 컬럼2,.....) VALUES (컬럼1번 값, 2번값....)`
   - `INSERT INTO 체이블명 VALUES (컬럼1의 값, 2의 값,.....)`
   - row를 하나 생성하고자 할때

3. update

   - UPDATE 테이블명
   - SET 필드1=필드1의값, 필드2=필드2의값,......
   - WHERE 조건식
   - 조건식에 맞는 것을 수정할때

4. delete

   - DELETE
   - FROM 테이블명
   - WHERE 조건식
   - 테이블에서 조건에 맞는 것을 삭제

5. join

   - [설명문](http://www.sql-join.com/)
   - [한국어](http://www.sqlprogram.com/Basics/sql-join.aspx)
   - [W3 설명](https://www.w3schools.com/sql/sql_join.asp)

