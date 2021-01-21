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

# Tab UI

뭐 딱히 적을만한게.... Ajax 잘 생각하자

# Spring Core

**Spring Framework란?**

- 엔터프라이즈급 어플리케이션을 구축할 수 있는 가벼운 솔루션이자, 원스-스탑-숍(One-Stop-Shop)
- 원하는 부분만 가져다 사용할 수 있도록 모듈화가 잘 되어 있습니다.
- IoC 컨테이너입니다.
- 선언적으로 트랜잭션을 관리할 수 있습니다.
- 완전한 기능을 갖춘 MVC Framework를 제공합니다.
- AOP 지원합니다.
- 스프링은 도메인 논리 코드와 쉽게 분리될 수 있는 구조로 되어 있습니다.

**프레임 워크 모듈**

- 스프링 프레임워크는 약 20개의 모듈로 구성되어 있습니다.
- 필요한 모듈만 가져다 사용할 수 있습니다.

**AOP 와 인스트루멘테이션 (Instrumentation)**

- spring-AOP : AOP 얼라이언스(Alliance)와 호환되는 방법으로 AOP를 지원합니다.
- spring-aspects : AspectJ와의 통합을 제공합니다.
- spring-instrument : 인스트루멘테이션을 지원하는 클래스와 특정 WAS에서 사용하는 클래스로 더 구현체를 제공합니다. 참고로 BCI(Byte Code Instrumentations)은 런타임이나 로드(Load) 때 클래스의 바이트 코드에 변경을 가하는 방법을 말합니다.

 

**메시징(Messaging)**

- spring-messaging : 스프링 프레임워크 4는 메시지 기반 어플리케이션을 작성할 수 있는 Message, MessageChannel, MessageHandler 등을 제공합니다. 또한, 해당 모듈에는 메소드에 메시지를 맵핑하기 위한 어노테이션도 포함되어 있으며, Spring MVC 어노테이션과 유사합니다.

 

**데이터 엑서스(Data Access) / 통합(Integration)**

- 데이터 엑세스/통합 계층은 JDBC, ORM, OXM, JMS 및 트랜잭션 모듈로 구성되어 있다.
- **spring-jdbc** : 자바 JDBC프로그래밍을 쉽게 할 수 있도록 기능을 제공합니다.
- **spring-tx** : 선언적 트랜잭션 관리를 할 수 있는 기능을 제공합니다.
- spring-orm : JPA, JDO및 Hibernate를 포함한 ORM API를 위한 통합 레이어를 제공합니다.
- spring-oxm : JAXB, Castor, XMLBeans, JiBX 및 XStream과 같은 Object/XML 맵핑을 지원합니다.
- spring-jms : 메시지 생성(producing) 및 사용(consuming)을 위한 기능을 제공, Spring Framework 4.1부터 spring-messaging모듈과의 통합을 제공합니다.

 

**웹(Web)**

- 웹 계층은 spring-web, spring-webmvc, spring-websocket, spring-webmvc-portlet 모듈로 구성됩니다.
- **spring-web** : 멀티 파트 파일 업로드, 서블릿 리스너 등 웹 지향 통합 기능을 제공한다. HTTP클라이언트와 Spring의 원격 지원을 위한 웹 관련 부분을 제공합니다.
- **spring-webmvc** : Web-Servlet 모듈이라고도 불리며, Spring MVC 및 REST 웹 서비스 구현을 포함합니다.
- spring-websocket : 웹 소켓을 지원합니다.
- spring-webmvc-portlet : 포틀릿 환경에서 사용할 MVC 구현을 제공합니다.

 ## 컨테이너란?

- 컨테이너는 인스턴스의 생명주기를 관리한다
- 생성된 인스턴스들에게 추가적인 기능을 제공한다

## IoC란?

- Inversion of Contorl의 약어. inversion은 사전적 의미로 도치,역전이다. 보통 IoCㅇ를 제어의 역전이라고 버녁한다
- 개발자는 프로그램의 흐름을 제어하는 코드를 작성한다. 그런데, 이 흐름의 제어를 개발자가 하는 것이 아니라 다른 프로그램이 그 흐름을 제어하는 것을 IoC라고 말한다.

## DI란?

- DI는 Dependency Injection의 약자로 의존성 주입이란 뜻을 가지고 있다
- DI는 클래스 사이의 의존 관계를 빈(Bean) 설정 정보를 바탕으로 컨테이너가 자동으로 연결해주는 것을 말한다.

**Spring에서 제공하는 IoC/DI 컨테이너**

- BeanFactory : IoC/DI에 대한 기본 기능을 가지고 있습니다.
- ApplicationContext : BeanFactory의 모든 기능을 포함하며, 일반적으로 BeanFactory보다 추천됩니다. 트랜잭션처리, AOP등에 대한 처리를 할 수 있습니다. BeanPostProcessor, BeanFactoryPostProcessor등을 자동으로 등록하고, 국제화 처리, 어플리케이션 이벤트 등을 처리할 수 습니다.

- BeanPostProcessor : 컨테이너의 기본로직을 오버라이딩하여 인스턴스화 와 의존성 처리 로직 등을 개발자가 원하는 대로 구현 할 수 있도록 합니다.
- BeanFactoryPostProcessor : 설정된 메타 데이터를 커스터마이징 할 수 있습니다.

test 방법을 알아서 익혀라.... (~~존나 무성의하네~~)

이클립스의 경우 getter와 setter을 source탭에서 자동으로 생성할 수 있는 메뉴가 있다

이 방법으로 같은 인스턴스를 계속 가져와봤자 같은 인스턴스가 된다(같은 메모리주소를 향함). 하나만 생성해서 운영할 수 있도록 하자

### 의존성 주입 DI

Car.java Engine.java ApplicationContextExam02.java applicationContext.xml참고하면서 이해해보자

**Java config를 이용한 설정을 위한 어노테이션**

**@Configuration**

- 스프링 설정 클래스를 선언하는 어노테이션

**@Bean**

- bean을 정의하는 어노테이션
- @Configuration 은 스프링 설정 클래스라는 의미를 가집니다.
- JavaConfig로 설정을 할 클래스 위에는 @Configuration가 붙어 있어야 합니다.
- ApplicationContext중에서 AnnotationConfigApplicationContext는 JavaConfig클래스를 읽어들여 IoC와 DI를 적용하게 됩니다.
- 이때 설정파일 중에 @Bean이 붙어 있는 메소드들을 AnnotationConfigApplicationContext는 자동으로 실행하여 그 결과로 리턴하는 객체들을 기본적으로 싱글턴으로 관리를 하게 됩니다.

**@ComponentScan**

- @Controller, @Service, @Repository, @Component 어노테이션이 붙은 클래스를 찾아 컨테이너에 등록
- @ComponentScan어노테이션은 파라미터로 들어온 패키지 이하에서 @Controller, @Service, @Repository, @Component 어노테이션이 붙어 있는 클래스를 찾아 메모리에 몽땅 올려줍니다.
- 기존의 Car클래스와 Engine클래스 위에 @Component를 붙이도록 하겠습니다.

**@Component**

- 컴포넌트 스캔의 대상이 되는 애노테이션 중 하나로써 주로 유틸, 기타 지원 클래스에 붙이는 어노테이션

**@Autowired**

- 주입 대상이되는 bean을 컨테이너에 찾아 주입하는 어노테이션