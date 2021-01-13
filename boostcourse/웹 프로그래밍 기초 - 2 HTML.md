# 웹 프로그래밍 기초

> 1. web개발의 이해 - FE/BE
> 2. HTML - FE (이 파일)
> 3. CSS - FE
> 4. 개발환경 설정 - BE
> 5. Servlet - BE

## 2. HTML - FE

[html tag list](https://www.w3schools.com/tags/default.asp)

![](html태그 레이아웃.jpg)

이런 형태의 구성을 항상 생각하자! 다 div로 때울 생각하지말고

[이걸 참고해서 레이아웃 생각하자](https://gist.github.com/thomd/9220049)

id는 꼭 하나만 쓰도록 하자. 에러는 안나지만 매우 번거로울 것이다

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>boostcourse</title>
</head>
<body>
  
  <header>
    <h1>Company Name</h1>
    <img src="..." alt="logo">
  </header>
  <!-- 유일하니까 class 대신 id괜찮음-->
  <section class="nav-section">
    <nav>
      <ul>
        <li>Home</li>
        <li>Home</li>
        <li>About</li>
        <li>Map</li>
      </ul>
    </nav>
    
    <section class="roll-section">
      <button></button>
      <div><img src="" alt=""></div>
      <div><img src="" alt=""></div>
      <div><img src="" alt=""></div>
      <nutton></nutton>
    </section>
    
    <section>
      <ul>
        <li class="our_description">
          <h3>AboutUs</h3>
          <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro tempore, ad exercitationem nobis praesentium adipisci, assumenda placeat culpa saepe enim nihil explicabo sequi laborum inventore blanditiis eaque nisi eligendi! Iure.</div>
        </li>
        <li class="our_description">
          <h3>What we do</h3>
          <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt voluptatum hic, animi culpa, ex fugiat temporibus id enim ipsam. Explicabo dolorum fugiat, incidunt pariatur magni aperiam iusto exercitationem porro tempore.</div>
        </li>
        <li class="our_description">
          <h3>Contact us</h3>
          <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio sunt est sapiente nihil dolore omnis possimus qui culpa labore, doloremque cum ipsa beatae, quaerat voluptate corrupti error pariatur ea animi.</div>
        </li>
      </ul>
    </section>
  </section>
  
  <footer><span>Copyright @codesquad</span></footer>
</body>
</html>
```

