# 웹 앱 개발 3

> 1. UI Component module -FE
> 2. JavaScript Regular expression - FE
> 3. form 데이터 보내기 - FE
> 4. 상태유지기술 - BE
> 5. Spring 에서의 Session 사용법 - BE
> 6. 인터셉터 - BE
> 7. 아규먼트 리졸버 - BE

# 웹에서의 상태유지

## HTTP프로토콜은 상태 유지가 되지 않는 프로토콜이다.

- 이전에 무엇을 했고, 지금 무엇을 했는지에 대한 정보를 갖고 있지 않음
- 웹 브라우저 (클라이언트) 의 요청에 대한 응답을 하고 나면 해당 클라이언트와의 연결을 지속하지 않음
- 상태 유지를 위해 **Cookie**와 **Session**이 등장

## 쿠키와 세션

- 쿠키

  - 사용자 컴퓨터에 저장

  - 저장된 정보를 다른 사람 또는 시스템이 볼 수 있는 단점

  - 유효시간이 지나면 사라짐

  - [자바에서 쿠키란](https://tomcat.apache.org/tomcat-5.5-doc/servletapi/javax/servlet/http/Cookie.html)

  - [서블릿에서](https://www.javatpoint.com/cookies-in-servlet)

  - 로직

    - ![](C:\Users\USER\Desktop\study\studying\boostcourse\쿠키1.png)

      ![쿠키2](C:\Users\USER\Desktop\study\studying\boostcourse\쿠키2.png)

- 세션

  - 서버에 저장

  - 서버가 종료되거나 유효시간이 지나면 사라짐

  - [자바에서 세션이란](https://tomcat.apache.org/tomcat-5.5-doc/servletapi/javax/servlet/http/HttpSession.html)

  - [서블릿에서](https://www.javatpoint.com/http-session-in-session-tracking)

  - 로직

    - ![](C:\Users\USER\Desktop\study\studying\boostcourse\세션1.png)

      ![세션2](C:\Users\USER\Desktop\study\studying\boostcourse\세션2.png)

## 쿠키

- 정의
  - 클라이언트 단에 저장되는 작은 정보의 단위
  - 클라이언트에서 생성하고 저장될 수 있고, 서버단에서 전송한 쿠키가 클라이언트에 저장될 수 있다.
- 이용 방법
  - 서버에서 클라이언트의 브라우저로 전송되어 사용자의 컴퓨터에 저장
  - 저장된 쿠키는 다시 해당하는 웹 페이지에 접속 할 때. 브라우저에서 서버로 쿠리를 전송
  - 쿠키는 이름(name)과 값(value) 으로 구성된 자료를 저장
    - 이름과 값 외에도 주석(comment), 경로(path), 유효기간(maxage, expiry), 버전(version), 도메인(domain)과 같은 추가적인 정보를 저장
  - 쿠키는 그 수와 크기에 제한
    - 하나의 쿠키는 4K Byte 크기로 제한
    - 브라우저는 각각의 웹사이트 당 20개의 쿠키를 허용
    - 모든 웹 사이트를 합쳐 최대 300개를 허용
    - 그러므로클라이언트 당 쿠키의 최대 용량은 1.2M Byte

### 자바에서 쿠키 생성 방법

**서버에서 쿠키 생성, Reponse의 addCookie메소드를 이용해 클라이언트에게 전송**

```java
Cookie cookie = new Cookie(이름, 값);
response.addCookie(cookie);
```

- 쿠키는 (이름, 값)의 쌍 정보를 입력하여 생성합니다.
- 쿠키의 이름은 일반적으로 알파벳과 숫자, 언더바로 구성합니다. 정확한 정의를 알고 싶다면 RFC 6265(https://tools.ietf.org/html/rfc6265) 문서 [4.1.1 Syntax] 항목을 참조하세요.

**클라이언트가 보낸 쿠키 정보 읽기**

```java
Cookie[] cookies = request.getCookies();
```

- 쿠키 값이 없으면 null이 반환됩니다.
- Cookie가 가지고 있는 getName()과 getValue()메소드를 이용해서 원하는 쿠키정보를 찾아 사용합니다.

**클라이언트에게 쿠키 삭제 요청**

- 쿠키를 삭제하는 명령은 없고, maxAge가 0인 같은 이름의 쿠키를 전송합니다.

```java
Cookie cookie = new Cookie("이름", null);
cookie.setMaxAge(0);
response.addCookie(cookie);
```

**쿠키의 유효기간 설정**

- 메소드 setMaxAge()
  - 인자는 유효기간을 나타내는 초 단위의 정수형 (10분은 cookie.setMaxAge(10*60))
  - 만일 유효기간을 0으로 지정하면 쿠키의 삭제
  - 음수를 지정하면 브라우저가 종료될 때 쿠키가 삭제

**쿠키와 관련된 함수**

| 반환형 |        메소드 이름        |                         메소드 기능                          |
| :----: | :-----------------------: | :----------------------------------------------------------: |
|  int   |        getMaxAge()        | 쿠키의 최대 지속 시간을 초단위로 얻어냄<br /> -1 일 경우에는 브라우저가 종료되면 쿠키를 만료 |
| String |         getName()         |                쿠키의 이름을 스트링으로 반환                 |
| String |        getValue()         |                 쿠키의 값을 스트링으로 반환                  |
|  void  | setValue(String newValue) |              쿠키에 새로운 값을 설정할 때 사용               |

### Spring MVC에서의 Cookie사용

- @CookieValue 애노테이션 사용
- 컨트롤러 메소드의 파라미터에서 CookieValue애노테이션을 사용함으로써 원하는 쿠키정보를 파라미터 변수에 담아 사용할 수 있습니다.
- 컨트롤러메소드(@CookieValue(value="쿠키이름",required=false,defaultValue="기본값") String 변수명)

[쿠키 한계 관련](http://browsercookielimits.squawky.net/)

쿠키 실습 코드

```java
package kr.or.connect.guestbook.controller;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import kr.or.connect.guestbook.dto.Guestbook;
import kr.or.connect.guestbook.service.GuestbookService;

@Controller
public class GuestbookController {
	@Autowired
	GuestbookService guestbookService;

	@GetMapping(path="/list")
	public String list(@RequestParam(name="start", required=false, defaultValue="0") int start,
					   ModelMap model,
                       HttpServletRequest request,
					   HttpServletResponse response) {

        
		String value = null;
		boolean find = false;
		Cookie[] cookies = request.getCookies();
		if(cookies != null) {
			for(Cookie cookie : cookies) {
				if("count".equals(cookie.getName())) {
					find = true;
					value = cookie.getValue();
				}
			}
		}
		
      
		if(!find) {
			value = "1";
		}else { // 쿠키를 찾았다면.
			try {
				int i = Integer.parseInt(value);
				value = Integer.toString(++i);
			}catch(Exception ex) {
				value = "1";
			}
		}
		
   
		Cookie cookie = new Cookie("count", value);
		cookie.setMaxAge(60 * 60 * 24 * 365); // 1년 동안 유지.
		cookie.setPath("/"); // / 경로 이하에 모두 쿠키 적용. 
		response.addCookie(cookie);
		
		
		List<Guestbook> list = guestbookService.getGuestbooks(start);
		
		int count = guestbookService.getCount();
		int pageCount = count / GuestbookService.LIMIT;
		if(count % GuestbookService.LIMIT > 0)
			pageCount++;
		
		List<Integer> pageStartList = new ArrayList<>();
		for(int i = 0; i < pageCount; i++) {
			pageStartList.add(i * GuestbookService.LIMIT);
		}
		
		model.addAttribute("list", list);
		model.addAttribute("count", count);
		model.addAttribute("pageStartList", pageStartList);
		model.addAttribute("cookieCount", value); // jsp에게 전달하기 위해서 쿠키 값을 model에 담아 전송한다.
		
		return "list";
	}
	
	@PostMapping(path="/write")
	public String write(@ModelAttribute Guestbook guestbook,
						HttpServletRequest request) {
		String clientIp = request.getRemoteAddr();
		System.out.println("clientIp : " + clientIp);
		guestbookService.addGuestbook(guestbook, clientIp);
		return "redirect:list";
	}
}
```

위 코드를 애노테이션을 이용해여 수정해보자

```java
package kr.or.connect.guestbook.controller;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import kr.or.connect.guestbook.dto.Guestbook;
import kr.or.connect.guestbook.service.GuestbookService;

@Controller
public class GuestbookController {
	@Autowired
	GuestbookService guestbookService;

  	@GetMapping(path="/list")
	public String list(@RequestParam(name="start", required=false, defaultValue="0") int start,
					   ModelMap model, @CookieValue(value="count", defaultValue="1", required=true) String value,
					   HttpServletResponse response) {
		
        // 쿠키 값을 1증가 시킨다.
		try {
			int i = Integer.parseInt(value);
			value = Integer.toString(++i);
		}catch(Exception ex){
			value = "1";
		}
		
        // 쿠키를 전송한다.
		Cookie cookie = new Cookie("count", value);
		cookie.setMaxAge(60 * 60 * 24 * 365); // 1년 동안 유지.
		cookie.setPath("/"); // / 경로 이하에 모두 쿠키 적용. 
		response.addCookie(cookie);
		
		List<Guestbook> list = guestbookService.getGuestbooks(start);
		
		int count = guestbookService.getCount();
		int pageCount = count / GuestbookService.LIMIT;
		if(count % GuestbookService.LIMIT > 0)
			pageCount++;
		
		List<Integer> pageStartList = new ArrayList<>();
		for(int i = 0; i < pageCount; i++) {
			pageStartList.add(i * GuestbookService.LIMIT);
		}
		
		model.addAttribute("list", list);
		model.addAttribute("count", count);
		model.addAttribute("pageStartList", pageStartList);
		model.addAttribute("cookieCount", value); // 쿠키를 추가한다.
		
		return "list";
	}
	
	@PostMapping(path="/write")
	public String write(@ModelAttribute Guestbook guestbook,
						HttpServletRequest request) {
		String clientIp = request.getRemoteAddr();
		System.out.println("clientIp : " + clientIp);
		guestbookService.addGuestbook(guestbook, clientIp);
		return "redirect:list";
	}
}
```

## Session을 이용한 상태저장

**세션 정의**

**정의**

- 클라이언트 별로 서버에 저장되는 정보입니다.

**이용 방법**

- 웹 클라이언트가 서버측에 요청을 보내게 되면 서버는 클라이언트를 식별하는 session id를 생성합니다.
- 서버는 session id를 이용해서 key와 value를 이용한 저장소인 HttpSession을 생성합니다.
- 서버는 session id를 저장하고 있는 쿠키를 생성하여 클라이언트에 전송합니다.
- 클라이언트는 서버측에 요청을 보낼때 session id를 가지고 있는 쿠키를 전송합니다.
- 서버는 쿠키에 있는 session id를 이용해서 그 전 요청에서 생성한 HttpSession을 찾고 사용합니다.

**세션 생성 및 얻기**

```java
HttpSession session = request.getSession();
HttpSession session = request.getSession(true);
```

- request의 getSession()메소드는 서버에 생성된 세션이 있다면 세션을 반환하고 없다면 새롭게 세션을 생성하여 반환합니다.
- 새롭게 생성된 세션인지는 HttpSession이 가지고 있는 isNew()메소드를 통해 알 수 있습니다.

```java
HttpSession session = request.getSession(false);
```

- request의 getSession()메소드에 파라미터로 false를 전달하면, 이미 생성된 세션이 있다면 반환하고 없으면 null을 반환합니다.

**세션에 값 저장**

```java
setAttribute(String name, Object value)
```

- name과 value의 쌍으로 객체 Object를 저장하는 메소드입니다.
- 세션이 유지되는 동안 저장할 자료를 저장합니다.

```java
session.setAttribute(이름, 값)
```

**세션에 값 조회**

getAttribute(String name) 메소드

- 세션에 저장된 자료는 다시 getAttribute(String name) 메소드를 이용해 조회합니다.
- 반환 값은 Object 유형이므로 저장된 객체로 자료유형 변환이 필요합니다.
- 메소드 setAttribute()에 이용한 name인 “id”를 알고 있다면 바로 다음과 같이 바로 조회합니다.

```java
String value = (String) session.getAttribute("id");
```

**세션에 값 삭제**

- removeAttribute(String name) 메소드
  \- name값에 해당하는 세션 정보를 삭제합니다.
- invalidate() 메소드
  \- 모든 세션 정보를 삭제합니다.

**javax.servlet.http.HttpSession**

|   반환형    |               메소드이름                |                          메소드기능                          |
| :---------: | :-------------------------------------: | :----------------------------------------------------------: |
|    long     |            getCreationTime()            | 를 세션이 생성된 시간까지 지난 시간을 계산하여 밀리세컨드로 반환 |
|   String    |                 getId()                 |    세션에 할당된 유일한 식별자(ID)를 String 타입으로 반환    |
|     int     |        getMaxInactivelInterval()        | 현재 생성된 세션을 유지하기 위해 설정된 최대 시간ㅇ늘 초의 정수 형으로 반환, 지정하지 않으면 기본 값은 1800초, 즉 30분이며, 기본 값도 서버에서 설정 가능 |
|   Object    |        getAttribute(String name)        | name이란 이름에 해당되는 속성값을 Object타입으로 반환, 해당되는 이름이 없을 경우에는 null을 반환 |
| Enumeration |           getAttributeNames()           |          속성의 이름들을 Enumeration 타입으로 반환           |
|    void     |              invalidate()               |                현재 생성된 세션을 무효화 시킴                |
|    void     |      removeAttribute(String name)       |               name으로 지정한 속성의 값을 제거               |
|    void     | setAttribute(String name, Object value) |            name으로 지정한 이름에 value 값을 할당            |
|    void     |  setMaxInactiveInterval(int interval)   |            세션의 최대 유지 시간을 초 단위로 설정            |
|   boolean   |                 isNew()                 | 세션이 새로이 만들어졌으면 true, 이미 만들어진 세션이면 false를 반환 |

**javax.servlet.http.HttpSession**

**세션은 클라이언트가 서버에 접속하는 순간 생성**

- 특별히 지정하지 않으면 세션의 유지 시간은 기본 값으로 30분 설정합니다.
- 세션의 유지 시간이란 서버에 접속한 후 서버에 요청을 하지 않는 최대 시간입니다.
- 30분 이상 서버에 전혀 반응을 보이지 않으면 세션이 자동으로 끊어집니다.
- 이 세션 유지 시간은 web.xml파일에서 설정 가능합니다.

```xml
<session-config>
  <session-timeout>30</session-timeout>
</session-config>
```

1. 쿠키는 이름과 값이 모두 문자열이지만, 세션의 키값은 문자열이고 값은 객체로 저장할 수 있습니다. 왜 이런 차이가 있을까요?	
   - cookie는 클라이언트에서 데이터를 저장하기 위한 자료구조이고, session은 서버에서 데이터를 저장하기 위한 구조 입니다. cookie는 클라이언트에서 file에 저장하기 때문에 key=value 형태의 문자열로 저장을 하고, session은 서버의 memory에 데이터를 저장합니다. 이때 map(key=value) 형태의 자료구조를 사용하는데, key는 cookie에 저장된 sessionid값이 저장되고, value에는 Java Object를 상속받은 모든 객체를 저장할 수 있습니다. session 정보는 서버의 메모리에 저장되기 때문에 서버(was)가 shutdown되면 모두 사라집니다. 따라서 세션 정보가 영속성(persistance)을 가지려면 별도의 저장소(DB, File 등)에 세션 정보를 보관해야 합니다. 

### 실습코드

- /guess로 요청을 하면 컴퓨터가 1부터 100 사이의 임의의 값 중의 하나를 맞춰보라는 메시지가 출력합니다.
- 해당 값은 세션에 저장합니다.
- 사용자는 1부터 100 사이의 값을 입력합니다.
- 입력한 값이 세션 값보다 작으면, 입력한 값이 작다고 출력합니다.
- 입력한 값이 세션 값보다 크면, 입력한 값이 크다고 출력합니다.
- 입력한 값이 세션 값과 같다면 몇 번째에 맞췄다고 출력합니다.

GuessNumberController

```java
package kr.or.connect.guestbook.controller;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class GuessNumberController {

	@GetMapping("/guess")
	public String guess(@RequestParam(name="number", required=false) Integer number,
			HttpSession session,
			ModelMap model) {
		
		String message = null;

		// get방식으로 /guess 를 요청하는데 파라미터 number가 없을 경우에는 session에 count를 0으로 randomNumber엔 1부터 100사이의 값을 저장합니다.
		if(number == null) {
			session.setAttribute("count", 0);
			session.setAttribute("randomNumber", (int)(Math.random() * 100) + 1); // 1 ~ 100사이의 random값
			message = "내가 생각한 숫자를 맞춰보세요.";
		}else {

			// number파라미터가 있을 경우 세션에서 값을 읽어들인 후, number와 세션에 저장된 값을 비교합니다.
			// 값을 비교해서 작거나 크다면 카운트를 1증가시켜주고
			// 값이 같다면 세션 정보를 삭제합니다.
			// 각 상황에 맞는 메시지를 message변수에 저장을 한 후 jsp에게 전달하기 위해서 ModelMap의 addAttribute메소드를 통해 전달하게 됩니다.
			int count = (Integer)session.getAttribute("count");
			int randomNumber = (Integer)session.getAttribute("randomNumber");
		
			
			if(number < randomNumber) {
				message = "입력한 값은 내가 생각하고 있는 숫자보다 작습니다.";
				session.setAttribute("count", ++count);
			}else if(number > randomNumber) {
				message = "입력한 값은 내가 생각하고 있는 숫자보다 큽니다.";
				session.setAttribute("count", ++count);
			}else {
				message = "OK " + ++count + " 번째 맞췄습니다. 내가 생각한 숫자는 " + number + " 입니다.";
				session.removeAttribute("count");
				session.removeAttribute("randomNumber");
			}
		}
		
		model.addAttribute("message", message);
		
		return "guess";
	}
}
```

guess.jsp 

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>       
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>숫자 맞추기 게임</title>
</head>
<body>
<h1> 숫자 맞추기 게임.</h1>
<hr>
<h3>${message }</h3>

<c:if test="${sessionScope.count != null}">
<form method="get" action="guess">
1부터 100사이의 숫자로 맞춰주세요.<br>
<input type="text" name="number"><br>
<input type="submit" value="확인">
</form>
</c:if>

<a href="guess">게임 다시 시작하기.</a>
</body>
</html>
```

**@SessionAttributes & @ModelAttribute**

@SessionAttributes 파라미터로 지정된 이름과 같은 이름이 @ModelAttribute에 지정되어 있을 경우 메소드가 반환되는 값은 세션에 저장됩니다.

아래의 예제는 세션에 값을 초기화하는 목적으로 사용되었습니다.

```java
@SessionAttributes("user")
public class LoginController {
  @ModelAttribute("user")
  public User setUpUserForm() {
  return new User();
  }
}
```

@SessionAttributes의 파라미터와 같은 이름이 @ModelAttribute에 있을 경우 세션에 있는 객체를 가져온 후, 클라이언트로 전송받은 값을 설정합니다.

```java
@Controller
@SessionAttributes("user")
public class LoginController {
......
  @PostMapping("/dologin")
  public String doLogin(@ModelAttribute("user") User user, Model model) {
......
  }
}
```

**@SessionAttribute**

메소드에 @SessionAttribute가 있을 경우 파라미터로 지정된 이름으로 등록된 세션 정보를 읽어와서 변수에 할당합니다.

```java
@GetMapping("/info")
public String userInfo(@SessionAttribute("user") User user) {
//...
//...
return "user";
}
```

**SessionStatus**

SessionStatus 는 컨트롤러 메소드의 파라미터로 사용할 수 있는 스프링 내장 타입입니다.

이 오브젝트를 이용하면 현재 컨트롤러의 @SessionAttributes에 의해 저장된 오브젝트를 제거할 수 있습니다.

```java
@Controller
@SessionAttributes("user")
public class UserController {
...... 
    @RequestMapping(value = "/user/add", method = RequestMethod.POST)
    public String submit(@ModelAttribute("user") User user, SessionStatus sessionStatus) {
  ......
  sessionStatus.setComplete();
                                   ......

   }
 }
```

**Spring MVC - form tag 라이브러리**

modelAttribute속성으로 지정된 이름의 객체를 세션에서 읽어와서 form태그로 설정된 태그에 값을 설정합니다.

```html
<form:form action="login" method="post" modelAttribute="user">
Email : <form:input path="email" /><br>
Password : <form:password path="password" /><br>
<button type="submit">Login</button>
</form:form>
```

# 인터셉터

[공식 문서](https://www.baeldung.com/spring-mvc-handlerinterceptor) [참고자료](https://www.journaldev.com/2676/spring-mvc-interceptor-example-handlerinterceptor-handlerinterceptoradapter) [참고 자료 2](https://to-dy.tistory.com/21)

## 인터셉터란?

Interceptor는 Dispatcher serblet에서 Handler(Controller) 로 요청을 보낼 때, Handler에서 Dispatcher serblet으로 응답을 보낼 때 동작합니다.

![](C:\Users\USER\Desktop\study\studying\boostcourse\인터셉터.jpg)

### 인터셉터 작성법

1. org.springframework.web.servlet.HandlerInterceptor 인터페이스를 구현합니다
2. org.springframework.web.servlet.handler.HandlerInterceptorAdapter 클래스를 상속받는다
3. Java Config를 사용한다면, WebMvcConfigurerAdapter가 가지고 있는 addInterceptors 메소드를 오버라이딩하고 등록하는 과정을 거칩니다.
4. xml 설정을 사용한다면, `<mvc:interceptors>` 요소에 인터셉터를 등록합니다

### 인터셉터와 유사한 기능에 서블릿 필터가 있다. 서블릿 필터는 모든 요청을 받고 응답할 때 공통 처리를 위해 사용됩니다. 무슨 차이일까요?

서블릿 필터는 dispatcherServlet이 실행되기 이전에 발생하고 인터셉터는 dispatcherServlet 이후 handler로 넘어가기 전에 발생을 합니다.

LogInterceptor.java

```java
package kr.or.connect.guestbook.interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

public class LogInterceptor extends HandlerInterceptorAdapter{

	@Override
	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler,
			ModelAndView modelAndView) throws Exception {
		System.out.println(handler.toString() + " 가 종료되었습니다.  " + modelAndView.getViewName() + "을 view로 사용합니다.");
	}

	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		System.out.println(handler.toString() + " 를 호출했습니다.");
		return true;
	}

	
}
```

WebMvcContextConfiguration 에 addInterceptors()메소드를 추가합니다.

인자로 넘어온 InterceptorRegistry의 addInterceptor에 앞에서 만든 인터셉터 객체를 넣어주면 추가가 됩니다.

```java
@Override
	public void addInterceptors(InterceptorRegistry registry) {
    		registry.addInterceptor(new LogInterceptor());
	}
```

특정 req에서만 실행하는 interceptor은 `registry.addInterceptor(new GuestBookInterceptor()).addPathPatterns("/auth/**");` 을 이용하면 된다.

preHandle()이 boolean값으로 나오는 이유는 이것의 리턴값이 true인지 false인지에 따라 해당 인터셉터이후의 함수를 실행시킬지 말지 정하기 때문이다!

# 아규먼트 리졸브

## 아규먼트 리졸버란?

- 컨트로러의 메소드의 인자로 사용자가 임의의 값을 전달하는 방법을 제공하고자 할 때 사용됩니다.
- 예를 들어, 세션에 젖아되어 있는 값 중 특정 이름의 값을 메소드 인자로 전달합니다.

## 작성방법

1. org.springframework.web.method.support.HandlerMethodArgumentResolver를 구현한 클래스를 작성ㅎ바니다.

2. supportsParameter메소드를 오버라이딩 한 후, 원하는 타입의 인자가 있는지 검사한 후 있을 경우 true가 리턴되도록 합니다.

3. resolveArgument메소드를 오버라이딩 한 후, 메소드의 인자로 전달할 값을 리턴합니다.

4. Java Config에 설정하는 방법

   - WebMvcConfigurerAdapter를 상속받은 Java Config 파일에서 addArgumentResolvers 메소드를 오버라이딩 한 후 원하는 아규먼트 리졸버 클래스 객체를 등록합니다

5. xml 파일에 설정하는 방법

   - ```xml
        <mvc:annotation-driven>
             <mvc:argument-resolvers>
                 <bean class="아규먼트리졸버클래스"></bean>      
             </mvc:argument-resolvers>
         </mvc:annotation-driven>
     ```

**Spring MVC의 기본 ArgumentResolver들**

getDefaultArgumentResolvers()메소드를 보면 기본으로 설정되는 아규먼트 리졸버에 어떤 것이 있는지 알 수 있습니다.

Map객체나 Map을 상속받은 객체는 Spring에서 이미 선언한 아규먼트 리졸버가 처리하기 때문에 전달 할 수 없습니다.

Map객체를 전달하려면 Map을 필드로 가지고 있는 별도의 객체를 선언한 후 사용해야 합니다.

[참고 자료](https://github.com/spring-projects/spring-framework/blob/v5.0.0.RELEASE/spring-webmvc/src/main/java/org/springframework/web/servlet/mvc/method/annotation/RequestMappingHandlerAdapter.java)

HeaderInfo.java

```java
package kr.or.connect.guestbook.argumentresolver;

import java.util.HashMap;
import java.util.Map;

public class HeaderInfo {
	private Map<String, String> map;
	
	public HeaderInfo() {
		map = new HashMap<>();
	}

	public void put(String name, String value) {
		map.put(name,  value);
	}
	
	public String get(String name) {
		return map.get(name);
	}

}
```

HeaderMapArgumentResolver.java

```java
package kr.or.connect.guestbook.argumentresolver;

import java.util.Iterator;

import org.springframework.core.MethodParameter;
import org.springframework.web.bind.support.WebDataBinderFactory;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.method.support.HandlerMethodArgumentResolver;
import org.springframework.web.method.support.ModelAndViewContainer;

public class HeaderMapArgumentResolver implements HandlerMethodArgumentResolver {

	@Override
	public boolean supportsParameter(MethodParameter parameter) {
		return parameter.getParameterType() == HeaderInfo.class;
	}

	@Override
	public Object resolveArgument(MethodParameter parameter, ModelAndViewContainer mavContainer,
			NativeWebRequest webRequest, WebDataBinderFactory binderFactory) throws Exception {

		HeaderInfo headerInfo = new HeaderInfo();
		
		Iterator<String> headerNames = webRequest.getHeaderNames();
		while(headerNames.hasNext()) {
			String headerName = headerNames.next();
			String headerValue = webRequest.getHeader(headerName);
//			System.out.println(headerName + " , " + headerValue);
			headerInfo.put(headerName, headerValue);
		}
		
		return headerInfo;

	}

}
```

아규먼트 리졸버를 적용하려면 WebMvcContextConfiguration 클래스에 addArgumentResolvers메소드를 오버라이딩 하고, 인자로 넘어온 argumentResolvers에 앞에서 생성한 아규먼트 리졸버를 넘겨줘야 합니다.

```java
@Override
	public void addArgumentResolvers(List<HandlerMethodArgumentResolver> argumentResolvers) {
    		System.out.println("아규먼트 리졸버 등록..");
		argumentResolvers.add(new HeaderMapArgumentResolver());
	}
```

GuestbookController 의 메소드인 list메소드의 인자로 HeaderInfo headerInfo를 추가합니다.

콘솔에 headerInfo의 get메소드에 user-agent를 넘겨서 값이 잘 출력되는지 확인할 수 있도록 코드를 추가합니다.

```java
@GetMapping(path="/list")
	public String list(@RequestParam(name="start", required=false, defaultValue="0") int start,
					   ModelMap model, @CookieValue(value="count", defaultValue="1", required=true) String value,
					   HttpServletResponse response,
					   HeaderInfo headerInfo) {
		System.out.println("-----------------------------------------------------");
		System.out.println(headerInfo.get("user-agent"));
		System.out.println("-----------------------------------------------------");
```