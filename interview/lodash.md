# lodash

- 번들 사이즈를 도와주는 라이브러리
  - import _ from 'lodash' 를 이용하는 간단한 방법
  - _.each를 이용해보고 빌드를 해보면 오히려 더 길어진 것을 볼 수가 있다.



lodash의 모든 기능을 이용한다면 이게 좋지만 그럴 가능성은 거의 없다

즉, 필요한 것만 import해오는 것이 가장 좋은 방식이며 용량을 줄이는대에 매우 도움이 된다

근데 사실상 이것도 용량을 줄이는데에 그렇게 좋지는 않다.

## 줄이는데에 가장 도움되는 방식은 이와 같은 방식이다 `import each from 'lodash/each'`이것이 무난하게 가장 괜찮은 방법이다

아예 loads-es를 이용하는 방법도 있다. 이것도 줄이는대에 매우 도움이 된다. `import each from 'lodash-es/each'`

- tree shaking을 검색해서 더 공부 해보자.
  - lodash-es는 그냥 저런 방식 말고 필요한 것만 import 해오는 방식도 용량을 줄이는데에 아주 큰 역할을 한다. `import each from lodash-es`