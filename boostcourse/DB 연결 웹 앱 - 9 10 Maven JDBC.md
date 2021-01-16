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

# Maven

```xml
pom.xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>kr.or.connect</groupId>
    <artifactId>examples</artifactId>
    <packaging>jar</packaging>
    <version>1.0-SNAPSHOT</version>
    <name>mysample</name>
    <url>http://maven.apache.org</url>
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>3.8.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

위를 참고하자

- **project** : pom.xml 파일의 최상위 루트 엘리먼트(Root Element)입니다.
- **modelVersion** : POM model의 버전입니다. 
- **groupId** : 프로젝트를 생성하는 조직의 고유 아이디를 결정합니다. 일반적으로 도메인 이름을 거꾸로 적습니다.
- **artifactId** : 해당 프로젝트에 의하여 생성되는 artifact의 고유 아이디를 결정합니다. Maven을 이용하여 pom.xml을 빌드할 경우 다음과 같은 규칙으로 artifact가 생성됩니다. artifactid-version.packaging. 위 예의 경우 빌드할 경우 examples-1.0-SNAPSHOT.jar 파일이 생성됩니다.
- **packaging** : 해당 프로젝트를 어떤 형태로 packaging 할 것인지 결정합니다. jar, war, ear 등이 해당됩니다.
- **version** : 프로젝트의 현재 버전. 추후 살펴보겠지만 프로젝트가 개발 중일 때는 SNAPSHOT을 접미사로 사용합니다. Maven의 버전 관리 기능은 라이브러리 관리를 편하게 합니다.
- **name** : 프로젝트의 이름입니다.
- **url** : 프로젝트 사이트가 있다면 사이트 URL을 등록하는 것이 가능합니다.

프로젝트 생성시 메이븐 프로젝트를 선택한다

쭉 Next를 누르다보면 아키타입을 선택 할 수가 있다.(아키타입이란 일종의 프로젝트 템플릿이라고 할 수 있다. 어떤 것을 선택했느냐에 따라서 자동으로, 여러 가지 파일들을 생성하거나 라이브러리를 셋팅해주거나 등의 일을 해준다.)

Maven을 이용하여 웹 어플리케이션을 개발하기 위해서 maven-archetype-webapp을 선택해야한다

group id는 보통 프로젝트를 진행하는 회사나 팀의 도메인 이름을 거꾸로 적는다

artifact id는 해당 프로젝트의 이름을 적는다

package이름은 group id와 Artifact Id가 조합된 이름이 됩니다.

Group Id를 kr.or.connect이고 Artifact Id가 mavenweb으로 설정했기 때문에 package이름은 kr.or.connect.mavenweb이 됩니다.



# JDBC

## jdbc 사용하기

1. import java.sql.*;
2. 드라이버를 로드
3. Connection 객체 생성
4. Statement 객체 생성 및 질의 수행
5. SQL문에 결과문이 있다면 ResultSet 객체를 생성
6. 모든 객체를 닫는다

유저 비밀번호 변경시 꼭 alter 쓸것 [참고자료](http://blog.naver.com/PostView.nhn?blogId=heops79&logNo=221482180594&parentCategoryNo=&categoryNo=38&viewDate=&isShowPopularPosts=true&from=search)