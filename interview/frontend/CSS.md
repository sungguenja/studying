# CSS

1. css 선택자의 특정성

   css 규칙의 특정성에 따라 요소에 표시할 스타일을 결정 `a,b,c,d` 이렇게 표현하고 다음과 같은 규칙을 가진다

   1. `a`: 인라인 스타일이 사용되고 있는지 여부. 인라인이면 1 아니면 0
   2. `b`: ID 셀렉터의 수
   3. `c`: 클래스, 속성, 가상 클래스 선택자의 수
   4. `d`: 태그, 가상 요소 선택자 수

   그리고 우선순위는 앞에 값이 우선순위 된다 (금,은,동메달로 생각하면 된다)

   이 모든 것을 무시하는 최고는 `!importat`로 우선순위 최고이다
   
2. `Resetting`과 `Normalizing` CSS의 차이

   - `Resetting` - resetting은 요소의 모든 기본 브라우저 스타일을 제거하기 위한 것 (margin, padding, font-size를 같은 값으로 재할당함)
   - `Normalizing` - '모든 스타일을 제거'하는 것이 아니라 유용한 기본 스타일을 보존. 일반적인 브라우저 종속성에 대한 버그 수정

3. `float`작동 방식

   float는 css위치지정 속성. 흐름의 일부가 되도록 하는 것. `position: absolute`와 달리 다른 요소의 위치에 영향을 줌.

   부모에 float가 있으면 그 높이는 무시가 된다.

4. `z-index`와 스택 컨텍스트가 어떻게 형성되는지

   `z-index` 속성은 겹치는 요소의 쌓임 순서를 제거한다. `z-index`는 `position`이 `static`이 아닌것에만 영향을 끼친다.

   `z-index`가 없다면 DOM에 나타나는 순서대로 요소가 쌓인다.

   스택 컨텍스트는 레이어들을 포함하는 요소이다. 지역 스택 컨텍스트 내에서, 자식의 `z-index` 값은 문서 루트가 아닌 해당 요소를 기준으로 작동. 외부 레이어와는 다르게 움직인다.

5. BFC (Block Formatting Context)와 그 작동 방식을 설명하세요

   BFC는 블록 박스가 배치된 웹 페이지의 시각적 CSS렌더링의 일부입니다. `overflow`가 있는 요소들이 새로운 Block Formatting Context를 만듭니다. 아래와 같은 조건 중 하나 이상을 충족 시켜야 한다

   - `float`가 None이 아님
   - `position`의 값이 `static`도 아니고 `relative`도 아님
   - `display`값이 `table-cell`, `table-caption`, `inline-block`, `flex`, `inline-flex`임
   - `overflow`의 값이 `visible`이 아님

   [참고 자료](https://www.smashingmagazine.com/2017/12/understanding-css-layout-block-formatting-context/)

6. `clear`

   - 빈 div방법: `<div style='clear:both;'></div>`

   - Clearfix 방법

     ```css
     .clearfix:after {
       content: ' ';
       visibility: hidden;
       display: block;
       height: 0;
       clear: both;
     }
     ```

   - `overflow:auto` or `overflow:hidden` 방법 - 부모는 새로운 BFC를 설정하고, 확장된 자식을 포함하도록 한다

7. CSS 스프라이트?

   css스프라이트는 여러 이미지를 하나의 큰 이미지로 결합하는 것. 일반적으로 아이콘에 사용되는 기술

   1. 스프라이트 생성기를 사용하여 여러 이미지를 하나로 묶어 적절한 CSS를 생성
   2. 각 이미지는 `background-image`, `background-position`, `background-size`속성이 정의된 해당 css 클래스를 갖습니다.
   3. 해당 이미지를 사용하기 위해, 요소에 해당 클래스를 추가합니다.

   장점

   - 여러 이미지에 대한 HTTP 요청수를 줄인다. 그러나 HTTP2를 사용하면 여러 이미지를 로드하는 것은 더이상 중요하진 않다
   - :hover 의 상태에서만 나타나는 이미지가 필요할 떄, 다운로드 되지 않는 이미지를 미리 다운로드하여 깜박임이 보이지 않는다.

   [참고 자료](https://css-tricks.com/css-sprites/)

8. 브라우저별 문제 이슈 해결

   1. 문제가 일어난 브라우저와 문제를 식별, 해당 브라우저가 사용 중일 때만 로드되는 별도의 스타일 시트 사용
   2. 이것을 범용성 있게 해결해주는 라이브러리 사용(Bootstrap)
   3. `autoprefixer`를 사용하여 벤더 프리픽스를 코드에 자동으로 추가
   4. Reset CSS 또는 Normalize CSS를 사용

9. 기능이 제한된 브라우저의 처리

   - 퇴보 - 최신 브라우저를 위한 어플보다 구형에 맞춰서 작동하도록 한다
   - 점진적 향상 - 브라우저가 지원하는 경우 기능을 강화
   - 기능 지원 확인은 필수
   - Autoprefixer 사용
   - Modernizr를 사용하여 감지

10. 콘텐츠를 시각적으로 숨기는 방법

    - `width: 0; hight:0;`
    - `position: absolute; left:-999999999999999px;`
    - `text-indent: -9999px`
    - 메타데이터를 이용
    - WAI-ARIA

11. 그리드

    ~~존나 사랑합니다~~ bootstrap을 이용하여도 괜찮고 기본 css의 그리드를 이용할 수도 있다

12. 미디어 쿼리나 모바일 만을 위한 css

    css를 기기별 크기로 나눠서 작동시켜도 좋다

    이것은 bootstrap을 통해서 쉽게 이용할 수도 있다

13. SVG

    [모질라](https://developer.mozilla.org/ko/docs/Web/SVG/Tutorial/Getting_Started)

    [참고자료](https://superfelix.tistory.com/604)

14. @media 속성

    - all - 모든 미디어 기기 장치

    - print - 프린

    - speech - 화면을 크게 읽는 스크린 리더

    - screen - 컴퓨터 스크린 등등

      ```css
      @media print {
          body {
              color: red;
          }
      }
      ```

15. css 전처리기

    [참고자료](https://kdydesign.github.io/2019/05/12/css-preprocessor/)

    [모질라](https://developer.mozilla.org/ko/docs/Glossary/CSS_preprocessor)

    - 장점
      - css의 유지보수성 향상
      - 중첩 선택자 작성이 쉬워짐
      - 일관된 테마를 위한 변수 사용, 여러 프로젝트에 걸쳐 테마파일을 공유
      - 반복되는 css를 위한 mixins생성
      - 코드를 여러 파일로 나눕니다.
        - css파일도 나눌수는 있따. 하지만 그러기 위해서는 각 css파일을 다운로드 하기위해 개별적인 http요청이 필요해진다
    - 단점
      - 전처리기를 위한 도구가 필요
        - 이로 인해 다시 컴파일 하는데에 시간이 증가할 수가 있다

16. css 선택자에 일치하는 요소를 어떻게 결정하는가?

    css를 오른쪽부터 왼쪽으로 일치 시킨다. 즉, 짧을 수록 검사 시간에는 빠르다.

    예를 들어 `p span`의 경우 모든 span요소를 찾는다 그리고 그 부모가 p요소인지 확인을 한다.

17. Pseudo-elements

    [참고자료](https://css-tricks.com/almanac/selectors/a/after-and-before/)

    선택자에 추가되는 키워드로 선택한 요소의 특정 부분을 스타일링 할 수 있습니다. 마크업을 수정하지 않고 텍스트 데코레이션을 위해 사용하거나 마크업에 요소를 추가할 수가 있다.

    - `:first-line`과 `:first-letter`는 텍스트를 데코레이션하는데 사용될 수 있다
    - 툴팁의 삼각 화살표는 `:before`과 `:after`를 사용한다. 삼각형이 실제로 DOM이 아닌 스타일의 일부로 간주되기 때문에 분리하는 것이 좋다

18. 박스 모델

    css 박스 모델은 문서 트리의 요소에 의해 생성

    다음을 계산한다

    - 블록 요소가 공간을 얼마나 차지하는지
    - 테두리 또는 여백이 겹치거나 충돌하는가
    - 박스의 크기

    규칙

    - 블록 요소의 크기는 `width`, `height`, `padding`, `border`, `margin`에 의해 계산된다
    - `height`가 지정되어 있지 않으면 내용물을 포함해서 높이를 가지고 padding을 더함
    - `width`가 지정되지 않으면 `float`가 아닌 내부 요소에 맞게 확장
    - padding과 margin은 요소의 width, hjeight에 포함되지 않는다

19. `box-sizing: border-box;`

    - 기본적으로 `box-sizing: content-box`
    - `box-sizing: border-box` 는 요소의 width와 height가 어떻게 계산되는지를 변경한다. border과 padding도 계산에 포함
    - height = height + 수직 padding + 수직 border
    - width = width + 수평 padding + 수평 border
    - padding과 border를 박스 모델의 일부분으로 생각하면, 디자이너가 실제로 생각하는 것과 잘 들어 맞는다

20. 반응형 디자인

    [모질라](https://developer.mozilla.org/en-US/docs/Archive/Apps/Design/UI_layout_basics/Responsive_design_versus_adaptive_design)



