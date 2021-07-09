document.addEventListener("DOMContentLoaded", () => {
    const my_btn = document.getElementById("customBtn");
    const my_div = document.getElementById("customDiv");
    const my_event = new CustomEvent("myEvent", {
        detail: {
            message: "hi"
        }
    });
    
    my_div.addEventListener("myEvent", function(e) {
        console.log(e);
        const tmp = document.createElement("h1");
        tmp.innerText = e.detail.message;
        my_div.appendChild(tmp);
    })
    
    my_btn.addEventListener("click", function(e) {
        console.log(e,my_event);
        my_div.dispatchEvent(my_event);
    })
    console.log(my_btn,my_div);
})