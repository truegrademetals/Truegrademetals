let btn = document.querySelectorAll(".time");
let square = document.querySelectorAll(".G-price");
let circle = document.querySelectorAll(".circle-0");
let circleRec = document.querySelectorAll(".circle > div");
let valueRec = document.querySelectorAll(".value > div > div");
let backWord = document.querySelector("#back-word");
let backWordArr = ["12 Months", "6 Months", "30 Days", "8 Days", "2 Years"];
for (let i = 0; i < btn.length; i++) {
    btn[i].addEventListener("click", function(){
        for (let j = 0; j < btn.length; j++) {
            btn[j].setAttribute("style", "background-color: #aaa;");
            square[j].setAttribute("style", "pointer-events: none; opacity: 0;");
            circle[j].setAttribute("style", "pointer-events: none; opacity: 0;");
        }
        btn[i].setAttribute("style", "background-color: #32558e;");
        square[i].setAttribute("style", "pointer-events: inherit; opacity: 1;");
        circle[i].setAttribute("style", "pointer-events: inherit; opacity: 1;");
        backWord.innerHTML = backWordArr[i];
    });
}
for (let i = 0; i < circleRec.length; i++) {
    circleRec[i].addEventListener("mouseenter", function(){
        valueRec[i].style.width = "10vw";
    });
    circleRec[i].addEventListener("mouseleave", function(){
        valueRec[i].style.width = "1.8vw";
    });
}
