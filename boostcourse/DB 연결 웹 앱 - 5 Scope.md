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

# Scope - BE

4가지 Scope

- Application: 웹 어플리케이션이 시작되고 종료될 때까지 변수가 유지되는 경우 사용
- Session: 웹 브라우저 별로 변수가 관리되는 경우 사용
- Request: http요청을 WAS가 받아서 웹 브라우저에게 응답할 때까지 변수가 유지되는 경우 사용
- Page: 페이지 내에서 지역변수처럼 사용
- [참고자료](http://www.javajee.com/application-request-session-and-page-scopes-in-servlets-and-jsps)

## Page Scope

- PageContext 추상 클래스를 사용한다.
- JSP 페이지에서 pageContext라는 내장 객체로 사용 가능 하다.
- forward가 될 경우 해당 Page scope에 지정된 변수는 사용할 수 없다.
- 사용방법은 Application scope나 Session scope, request scope와 같다.
- 마치 지역변수처럼 사용된다는 것이 다른 Scope들과 다릅니다.
- jsp에서 pageScope에 값을 저장한 후 해당 값을 EL표기법 등에서 사용할 때 사용됩니다.
- 지역 변수처럼 해당 jsp나 서블릿이 실행되는 동안에만 정보를 유지하고자 할 때 사용됩니다.

## Request scope

- http 요청을 WAS가 받아서 웹 브라우저에게 응답할 때까지 변수값을 유지하고자 할 경우 사용한다.
- HttpServletRequest 객체를 사용한다.
- JSP에서는 request 내장 변수를 사용한다.
- 서블릿에서는 HttpServletRequest 객체를 사용한다.
- 값을 저장할 때는 request 객체의 setAttribute()메소드를 사용한다.
- 값을 읽어 들일 때는 request 객체의 getAttribute()메소드를 사용한다.
- forward 시 값을 유지하고자 사용한다.
- 앞에서 forward에 대하여 배울 때 forward 하기 전에 request 객체의 setAttribute() 메소드로 값을 설정한 후, 서블릿이나 jsp에게 결과를 전달하여 값을 출력하도록 하였는데 이렇게 포워드 되는 동안 값이 유지되는 것이 Request scope를 이용했다고 합니다.

## Session scope

- 웹 브라우저별로 변수를 관리하고자 할 경우 사용한다.
- 웹 브라우저간의 탭 간에는 세션정보가 공유되기 때문에, 각각의 탭에서는 같은 세션정보를 사용할 수 있다.
- HttpSession 인터페이스를 구현한 객체를 사용한다.
- JSP에서는 session 내장 변수를 사용한다.
- 서블릿에서는 HttpServletRequest의 getSession()메소드를 이용하여 session 객체를 얻는다.
- 값을 저장할 때는 session 객체의 setAttribute()메소드를 사용한다.
- 값을 읽어 들일 때는 session 객체의 getAttribute()메소드를 사용한다.
- 장바구니처럼 사용자별로 유지가 되어야 할 정보가 있을 때 사용한다.

## Application scope

- 웹 어플리케이션이 시작되고 종료될 때까지 변수를 사용할 수 있다.
- ServletContext 인터페이스를 구현한 객체를 사용한다.
- jsp에서는 application 내장 객체를 이용한다.
- 서블릿의 경우는 getServletContext()메소드를 이용하여 application객체를 이용한다.
- 웹 어플리케이션 하나당 하나의 application객체가 사용된다.
- 값을 저장할 때는 application객체의 setAttribute()메소드를 사용한다.
- 값을 읽어 들일 때는 application객체의 getAttribute()메소드를 사용한다.
- 모든 클라이언트가 공통으로 사용해야 할 값들이 있을 때 사용한다.
- [참고자료](https://www.pearsonitcertification.com/articles/article.aspx?p=30082&seqNum=6)

예제

```java
// applicationscope1.java
package examples;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ApplicationScope01
 */
@WebServlet("/ApplicationScope01")
public class ApplicationScope01 extends HttpServlet {
    private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ApplicationScope01() {
        super();
        // TODO Auto-generated constructor stub
    }

    /**
     * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html; charset=UTF-8");
        
        PrintWriter out = response.getWriter();
        
        
        ServletContext application = getServletContext();
        int value = 1;
        application.setAttribute("value", value);
        
        
        out.println("<h1>value : " + value + "</h1>");
        
    }

}

// applicationscope02.java
package examples;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ApplicationScope01
 */
@WebServlet("/ApplicationScope02")
public class ApplicationScope02 extends HttpServlet {
    private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ApplicationScope02() {
        super();
        // TODO Auto-generated constructor stub
    }

    /**
     * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html; charset=UTF-8");
        
        PrintWriter out = response.getWriter();
        
        ServletContext application = getServletContext();
        
        
        try {
            int value = (int)application.getAttribute("value");
            value++;
            application.setAttribute("value", value);
            out.println("<h1>value : " + value + "</h1>");
        }catch(NullPointerException ex) {
            out.println("value가 설정되지 않습니다.");
        }
        
        
    }

}
```

```jsp
<!-- applicationscope01.jsp -->
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
    try{
        int value = (int)application.getAttribute("value");
        value = value + 2;
        application.setAttribute("value", value);
%>
        <h1><%=value %></h1>
<%        
    }catch(NullPointerException ex){
%>
        <h1>설정된 값이 없습니다.</h1>
<%        
    }
%>

</body>
</html>
```

01이 먼저 실행되지 않을시 에러가 일어난다! 왜냐! value가 저장되어있지 않기 때문에!