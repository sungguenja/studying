const slideList       = document.querySelector(".slide_list")
const slideItems      = document.querySelectorAll(".slide_item")
const slideNextButton = document.querySelector(".slide_btn_next")
const slidePrevButton = document.querySelector(".slide_btn_prev")
const pagenation      = document.querySelector(".slide_pagination")
const slideLen        = slideItems.length
const slideWidth      = 500
const slideHeight     = 500
const slideSpeed      = 300

slideList.style.width = slideWidth * (slideLen + 2) + "px"

let slideIdx = 1

// cloneNode라는 것이 있다. 말그대로 해당 노드를 복사한다 이거 꽤 유용한듯
const firstItem = slideList.firstElementChild
const lastItem  = slideList.lastElementChild
const cloneFirst = firstItem.cloneNode(true)
const cloneLast  = lastItem.cloneNode(true)

slideList.appendChild(cloneFirst)
slideList.insertBefore(cloneLast,slideList.firstElementChild)


slideList.style.transform = "translate3d(-" + (slideWidth * 1) + "px, 0px, 0px)"

slideNextButton.addEventListener("click", () => {
    slideIdx += 1
    slideList.style.transition = slideSpeed + "ms"
    slideList.style.transform  = `translate3d(-${slideWidth*slideIdx}px,0px,0px)`
    if(slideIdx >= slideLen) {
        slideIdx = 0
        setTimeout(() => {
            slideList.style.transition = "0ms"
            slideList.style.transform  = `translate3d(-${slideWidth*slideIdx}px,0px,0px)`
        },slideSpeed)
    }
})

slidePrevButton.addEventListener("click", () => {
    slideIdx -= 1
    slideList.style.transition = slideSpeed + "ms"
    slideList.style.transform  = `translate3d(-${slideWidth*slideIdx}px,0px,0px)`
    if(slideIdx <= 0) {
        slideIdx = slideLen
        setTimeout(() => {
            slideList.style.transition = "0ms"
            slideList.style.transform  = `translate3d(-${slideWidth*slideIdx}px,0px,0px)`
        },slideSpeed)
    }
})