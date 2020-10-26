function Person(name) {
    // 생성자 함수 코드 실행 전 -------- 1
    this.name = name;  // --------- 2
    // 생성된 함수 반환 -------------- 3
}

var me = new Person('Lee');
console.log(me.name);

var foo = {
name: 'foo',
gender: 'male'
}

console.dir(foo);

// 생성자 함수 방식
function Person(name, gender) {
this.name = name;
this.gender = gender;
}

var me2  = new Person('Lee', 'male');
console.dir(me2);

var you = new Person('Kim', 'female');
console.dir(you);