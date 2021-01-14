# 웹 프로그래밍 기초

> 1. web개발의 이해 - FE/BE
> 2. HTML - FE 
> 3. CSS - FE (이 파일)
> 4. 개발환경 설정 - BE
> 5. Servlet - BE

## 3. CSS - FE

구성: `선택자 {property : value;}`

style을 적용시키는 세가지 방법

1. html 태그 안에 넣는 것 inline

   `<span style="color:red;">`

2. style 태그로 지정하기 internal

   `<style>span{color:red;}</span>`

3. 외부파일로 지정하기 external

   `<link rel="stylesheet" type="text/css" href="main.css" />`

[css 우선순위](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

### cascading

css는 여러가지 스타일정보를 기반으로 최종적으로 **경쟁**에 의해서 적절한 스타일이 반영된다.

inline > internal = external 

같은 우선순위면 나중에 적용되는 것이 적용된다

구체적으로 된 것이 더 우선적으로 적용됨 ex) `body > span` > `span`

id > class > element 순으로 우선순위

### css selector

[참고자료](https://gist.github.com/magicznyleszek/809a69dd05e1d5f12d01)

tag로 지정하기 그냥 css쓰는대로 쓰면 된다

id로 지정하기 `#id이름`을 쓰면 된다

class 로 지정하기 `.class이름`을 쓰면 된다

p:nth-child(숫자) 자식요소로 부를 때 이것으로 특정 위치의 해당 태그자식만 꾸미기 가능

샐럭터를 이용해도 자식관계를 찾아갈 수 있다

em은 기본적용된거의 배수를 말한다. (font-size를 예로 들면 div에 적용된 폰트 사이즈의 배수로 적용이 된다는 소리)



### 엘리멘트 배치

#### 블록으로 쌓이는 display block

빈 공간이 생겨도 채우질 않는다

#### 옆으로 흐르는 display inline

크기를 지정해도 반영이 되질 않는다!

#### 다르게 배치시키기

**position**

1. 기본 값은 static 그냥 순서대로 배치
2. absolute 기준점에 따라서 특별한 위치에 위치합니다. top/left/right/bottom. 상위 엘리먼트중 position이 static이 아닌 엘리먼트가 기준점이 된다
3. relative는 자신이 위치해야 할 곳을 기준으로 top/left/right/bottom으로 이동시키기가 가능
4. fixed 화면에 고정된 위치

참고 코드

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JS Bin</title>
</head>
<body>

  <div class="wrap">
    <div class="static">static(default)</div>
    <div class="relative">relative(left:10px)</div>
    <div class="absolute">absolute(left:130px;top:30px)</div>
    <div class="fixed">fixed(top:250px)</div>
  </div>
  
</body>
</html>
```

```css

.wrap {
  position:relative;
}

.wrap > div {
  width:150px;
  height:100px;
  border:1px solid gray;
  font-size:0.7em;
  text-align:center;
  line-height:100px;
}

.relative {
  position:relative;
  left:10px;
  1top:10px;
}

.absolute {
  position:absolute;
  left:130px;
  top:30px;
}

.fixed {
  position:fixed;
  top:250px;
}
```



### float 기본 배치에서 벗어나서 떠있기

float속성은 원래 flow에서 벗어날 수 있다. float는 float끼리 영향을 준다

반대로 일반적인 애들은 float가 없는 것으로 인식

clear을 이용하여 방향별 float를 무시하게 하는 것이 가능

overflow로 부모가 자식의 float를 인식하게 하는 것이 가능



### 하나의 블록엘리먼트는 box model이다

element간의 간격 margin

element의 테두리 두깨 border

element안에서 테두리사이의 거리 padding -> box-sizing을 border-box로 해줘야 padding에 의해서 요소 크기가 변하는 상황을 막을 수가 있다.

[margin border padding](https://www.w3schools.com/css/css_boxmodel.asp)



### 그래서, layout 구현 방법은?

- 전체 레이아웃은 float를 잘 사용해서 2단, 3단 컬럼 배치를 구현합니다. 최근에는 css-grid나 flex속성 등 layout을 위한 속성을 사용하기 시작했으며 브라우저 지원범위를 확인해서 사용하도록 합니다.
- 특별한 위치에 배치하기위해서는 absolute를 사용하고, 기준점을 relative로 설정합니다.
- 네비게이션과 같은 엘리먼트는 block 엘리먼트를 inline-block으로 변경해서 가로로 배치하기도 합니다.
- 엘리먼트안의 텍스트의 간격과, 다른 엘리먼트간의 간격은 padding과 margin속성을 잘 활용해서 위치시킵니다.