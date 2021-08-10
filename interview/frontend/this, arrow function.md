# this, arrow function

## arrow function

~~일단 전역을 본다. 상위 객체를 보는줄 알았는데 전역을 보는걸로 확인되었다. 강의에서도 그럼~~

```javascript
const testObj = {
    name: "john",
    test1() {
        console.log(this,this.name);
    },
    test2: function () {
        console.log(this,this.name);
    },
    test3: () => {
        console.log(this,this.name);
    },
    innerObj: {
        name: "malkobichi",
        test1() {
            console.log(this,this.name);
        },
        test2: function () {
            console.log(this,this.name);
        },
        test3: () => {
            console.log(this,this.name);
        }
    }
}
```

~~위에 실행시켜보면 arrow function은 모두 전역을 보는것을 확인할 수 있음~~

상위 객체가 아니라 정확히는 상위 스코프를 보는 것
