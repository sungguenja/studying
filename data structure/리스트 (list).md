# 리스트 (list)

리스트 매우 선형적인 자료다 C에서는 아래와 같이 구현하고 파이썬은 그 다음처럼 구현할 것이다

```c
int A[5] = {1,2,3,4,5};
```

```python
A = [1,2,3,4,5]
```

C언어는 아쉽게도 배열의 크기를 늘릴수가 없다. 그러니 배열을 동적으로 할당해주는 것이 좋다. 참고로 C는 배열의 크기를 변수로 정해줄 수가 없으니 메모리할당하는 명령어를 잘 이용해야한다.

하지만 파이썬은 쉽게 배열의 크기를 바꿔 줄 수가 있다. (하지만 이것은 생각보다 속도가 꽤나 느리다 조심히 이용할 수록 좋다) `append`이것으로 쉽게 이용할 수가 있다.

## 파이썬 리스트는 동적으로 구현되었다.

파이썬의 리스트는 미리 메모리를 크게 할당을 해둔다. 대충 이런식이다.

- A = [1,2,3] 을 정의했다.
- 리스트의 크기는 3이지만 저장할 수 있는 용량은 **10**으로 크게 잡힌다
- `append`를 이용시 이미 비어있기 때문에 쉽게 삽입이 되는 것이다.

그런데 이런 경우 최대 용량에 도달했지만 또 삽입을 하고 싶은 경우는 어떻게 되는 것인가? 이것은 다음과 같이 진행된다.

1. 용량을 확장한 새로운 배열 할당
2. 기존의 배열을 새로운 배열에 복사
3. 그리고 새 항목을 삽입
4. 기존 배열 해제, 리스트로 새 배열 사용

이런 방식으로 메모리가 진행되기 때문에 메모리의 낭비를 감수해야한다. 그래서 이런 면을 생각하면 튜플이 용량을 변경할 수 없기 때문에 메모리측면에서 더 효율적이다

## 파이썬 리스트 시간 복잡도

- append연산의 시간 복잡도
  - 아직 미리 할당된 메모리에 여유가 있다면 메모리만 찾아서 바로 넣어주는 것이기 때문에 `O(1)`이 걸린다.
  - 하지만 메모리를 넘어갈 경우 모든 항목을 복사해야하기때문에 최소한 `O(n)` 이 걸린다!

`append`에서 시간복잡도가 상황마다 위와 같다는 것을 알게 되었다. 그렇다면 다른 연산마다 시간 복잡도는 어떻게 될까? 생각하는 그대로이다! 한번 적어보자!

- insert연산의 시간 복잡도
  - 맨 앞에 넣는 다고 생각하자. 그렇다면 뒤에 모든 원소들을 뒤로 옮기는 과정을 하게 된다. 즉, 위치마다 다르겠지만 최악의 경우는 `O(n)`이 될 것이다
- pop연산의 시간 복잡도
  - 이것도 상황마다 다르겠지만 맨 앞을 빼는 것이 제일 안좋은 상황이다. 맨 앞을 빼고 뒤의 모든 원소들을 앞으로 한칸씩 옮겨야 할 것이다. 즉 `insert`와 마찬가지로 `O(n)`이 걸릴 것이다.

## 그렇다면 클래스로 한번 나만의 리스트를 구현해보자

```python
class ArrayList:
    def __init__(self):
        self.items = []
    def insert(self, position, element):
        self.items.insert(position,element)
    def delete(self,position):
        return self.items.pop(position)
    def isEmpty(self):
        return len(self.items) == 0
    def getElement(self,position):
        return self.items[position]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def find(self,item):
        return self.items.index(item)
    def replace(self,position,item):
        self.items[position] = item
    def sort(self):
        self.items.sort()
    def merge(self,array):
        self.items.extend(array)
    def display(self,message="ArrayList : "):
        print(message, self.size(), self.items)
```

그렇다면 이것으로 라인 편집기를 이용해보자. myLineEditor.py를 참고하자

## 다른 언어에서의 배열

파이썬과는 좀 다르다. 일단 동적인 자료구조가 아니다. 유한하고 고정된 수의 원소로 이루어진다. 일부만 사용하더라도 크기만큼 메모리를 써야한다.

### C/C++

C와 C++은 여러 면에서 꽤 다르지만 배열을 다루는 방식에서는 매우 비슷하다. 이 두 언어는 배열의 크기는 신경쓰지 않고 위치만 신경쓴다. 배열 크기는 전적으로 프로그래머의 책임이다.

이 것이 꽤나 골때린다. 원소가 열개인 배열에 스무번째 원소에 뭔갈 저장시켜도 컴파일 에러가 안난다. 프로그래머가 잘 해줘야한다. 그런데 이것은 동적으로 배열을 할려면 조금 귀찮은 면이 있긴하다. `int A[n] = {}`이런식으로 저장 못한다. 직접 메모리할당해주는 방식을 해야한다.

### 자바

C의 배열과 다르다. 배열에 저장되는 데이터 유형과는 별개의 객체로 정의되어 있다. 따라서 배열에 대한 레퍼런스와 배열의 원소에 대한 레퍼런스가 같지 않다.

자바 배열은 정적이며 언어 자체에서 각 배열의 크기를 추적해주기 때문에 배열에 내장된 `length` 데이터 멤버를 통해 크기를 알아낼 수 있다. 단순한 대입만으로 배열의 원소를 복사할 수 없는 것은 C와 마찬가지다.

```java
byte[] arrayA = new byte[10];
byte[] arrayB = new byte[10];
arrayA = arrayB; // 복사는 이런식으로 진행이 되어야 한다
```

자바의 특이한 점은 배열을 선언할 때는 객체를 생성하지않는다! 다음 코드를 참고하면 이해가 적당히는 된다.

```java
Button myButtons[] = new Button[3]; // 아직 Button 객체 생성안됨
for (int i=0; i< myButtons.length; i++) {
    myButtons[i] = new Button(); // Button 객체 생성
}
// 모든 Button 객체가 생성됨
```

아니면 아래처럼 바로 생성이 가능하다

```java
Button myButtons[] = {new Button(),new Button(),new Button()};
```

### C#

