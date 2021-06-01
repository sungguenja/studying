var btns = [
    document.getElementById('btn0'),
    document.getElementById('btn1'),
    document.getElementById('btn2')
]

function setClick() {
    for (var i = 0; i < 3; i++) {
        btns[i].addEventListener('click',function(j){
            return (function(){
                console.log(j)
            })
        }(i));
    }
}

setClick();