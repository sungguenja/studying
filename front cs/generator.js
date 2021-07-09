function* sayHiGenerator(params) {
    yield params;
    yield 'hello';
    yield 'world';
    yield 'this is';
    return 'javascript';
}

const result_value = sayHiGenerator('??');

console.log(result_value);
console.log(result_value.next());
console.log(result_value.next());
console.log(result_value.next());
console.log(result_value.next());
console.log(result_value.next());