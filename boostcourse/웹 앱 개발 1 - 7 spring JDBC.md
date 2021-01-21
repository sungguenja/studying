# 웹 앱 개발 1/4

> 1. JavaScript 배열 - FE
> 2. DOM API 활용 - FE
> 3. Ajax - FE
> 4. Web Animation - FE
> 5. WEB UI - FE
> 6. Tab UI - FE
> 7. Spring Core - BE
> 8. Spring JDBC - BE
> 9. Spring MVC - BE
> 10. 레이어드 아키텍처 - BE
> 11. Controller - BE

# Spring JDBC

- JDBC 프로그래밍을 보면 반복되는 개발 요소가 있다.
- 이러한 반복적인 요소는 개발자를 지루하게 만든다.
- 개발하기 지루한 JDBC의 모든 저수준 세부사항을 스프링 프레임워크가 처리해준다.
- 개발자는 필요한 부분만 개발하면 된다

그렇다면 **Spring JDBC** 개발자가 해야할 일은?

![](18.png)

Spring JDBC 패키지

- org.springframework.jdbc.core
  - jdbc 템플릿 클래스와 콜백 인터페이스 포함
- org.springframework.jdbc.datasource
  - 데이터소스에 접근을 쉽게 해주는 유틸리티클래스와 JAVA EE에서 수정되지 않은 코드와 테스트에서 사용가능한 코드들을 포함
- org.springframework.jdbc.object
  - rdbms 조회하고 재사용 가능한 클래스 포함
- org.springframework.jdbc.support
  - sql injection 클래스들을 포함

## JDBC Template

[jdbc sql관련 참고 자료](https://docs.spring.io/spring-framework/docs/current/reference/html/data-access.html#jdbc)

- org.sprinframework.jdbc.core에서 가장 중요한 클래스
- 리소스 생성, 해지를 처리해서 연결을 닫는 것을 잊어 발생하는 문제등을 피할 수 있도록 한다.
- 스테이먼트(statement)의 생성과 실행을 처리한다.
- SQL조회, 업데이트, 저장 프로시저 호출, ResultSet 반복 호출 등을 실행한다.
- JDBC예외가 발생할 경우 org.springframework.dao패키지에 정의되어 있는 일반적인 예외로 변환시킨다.

#### jdbc template select예제

row수 카운팅 하기

```java
int rowCount = this.jdbcTemplate.quertForInt("select count(*) from t_actor");
```

변수 바인딩

```java
int countOfActorsNamedJoe = this.jdbcTemplate.queryForInt("select count(*) from t_actor where first_name = ?","Joe");
```

String값으로 결과 받기

```java
String lastName = this.jdbcTemplate.queryForObject("select last_name from t_actor where id = ?", new Object[]{1212L}, String.class); 
```

한 건 조회하기

```java
Actor actor = this.jdbcTemplate.queryForObject(
  "select first_name, last_name from t_actor where id = ?",
  new Object[]{1212L},
  new RowMapper<Actor>() {
    public Actor mapRow(ResultSet rs, int rowNum) throws SQLException {
      Actor actor = new Actor();
      actor.setFirstName(rs.getString("first_name"));
      actor.setLastName(rs.getString("last_name"));
      return actor;
    }
  });
```

여러 건 조회하기

```java
List<Actor> actors = this.jdbcTemplate.query(
  "select first_name, last_name from t_actor",
  new RowMapper<Actor>() {
    public Actor mapRow(ResultSet rs, int rowNum) throws SQLException {
      Actor actor = new Actor();
      actor.setFirstName(rs.getString("first_name"));
      actor.setLastName(rs.getString("last_name"));
      return actor;
    }
  });
```

중복 코드 제거 (1건 구하기와 여러 건 구하기가 같은 코드에 있을 경우)

```java
public List<Actor> findAllActors() {
  return this.jdbcTemplate.query( "select first_name, last_name from t_actor", new ActorMapper());
}
private static final class ActorMapper implements RowMapper<Actor> {
  public Actor mapRow(ResultSet rs, int rowNum) throws SQLException {
    Actor actor = new Actor();
    actor.setFirstName(rs.getString("first_name"));
    actor.setLastName(rs.getString("last_name"));
    return actor;
  }
}
```

update, delete

```java
this.jdbcTemplate.update("update t_actor set = ? where id = ?",  "Banjo", 5276L);

this.jdbcTemplate.update("delete from actor where id = ?", Long.valueOf(actorId));
```

### JdbcTemplate외의 접근 방법

- NamedParameterJdbcTemplate
  - JdbcTemplate에서 JDBC statement 인자를 ?를 사용하는 대신 파라미터명을 사용하여 작성하는 것을 지원
  - [NamedParameterJdbcTemplate 예제](https://docs.spring.io/spring/docs/current/spring-framework-reference/data-access.html#jdbc-NamedParameterJdbcTemplate)
- SimpleJdbcTemplate
  - JdbcTemplate과 NamedParameterJdbcTemplate 합쳐 놓은 템플릿 클래스
  - 이제 JdbcTemplate과 NamedParameterJdbcTemplate에 모든 기능을 제공하기 때문에 삭제 예정될 예정(deprecated)
  - [SimpleJdbcTemplate 예제](https://www.concretepage.com/spring/simplejdbctemplate-spring-example)
- SimpleJdbcInsert
  - 테이블에 쉽게 데이터 insert 기능을 제공
  - [SimpleJdbcInsert 예제](https://www.tutorialspoint.com/springjdbc/springjdbc_simplejdbcinsert.htm)