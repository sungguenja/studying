function f2() {
    console.log('f2 start');
    throw '에러';
    console.log('f2 end');
}

function f1() {
    console.log('f1 start');
    try {
        f2();
    } catch (e) {
        console.log(e);
    }
    console.log('f1 end');
}

f1()