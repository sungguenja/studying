<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Insert title here</title>
    <link rel="stylesheet" type="text/css" href="main.css" />
  </head>
  <body>
    <header>
      <button onclick="location.href='./add.html'">새로운 TODO 등록</button>
    </header>
    
    <section>
      <article>
        <div class="title">
          <h2>TODO</h2>
        </div>
        <div id="Todo"></div>
      </article>
      <article>
        <div class="title">
          <h2>DOING</h2>
        </div>
        <div id="Doing"></div>
      </article>
      <article>
        <div class="title">
          <h2>DONE</h2>
        </div>
        <div id="Done"></div>
      </article>
    </section>
  </body>
  <script src="./main.js"></script>
</html>