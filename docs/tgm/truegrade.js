let proChoose = document.querySelectorAll("#pro-choose > div");
let frameFrame = document.querySelectorAll(".frame-frame");
for (let i = 0; i < proChoose.length; i++) {
  proChoose[i].addEventListener("click", function(){
    for (let j = 0; j < proChoose.length; j++) {
      proChoose[j].style.opacity = "0.6";
      frameFrame[j].style.opacity = "0";
      frameFrame[j].style.pointerEvents = "none";
    }
    proChoose[i].style.opacity = "1";
    frameFrame[i].style.opacity = "1";
    frameFrame[i].style.pointerEvents = "inherit";
  });
}


let rightButton = document.querySelector("#rightbutton1");
let leftButton = document.querySelector("#leftbutton1");
let alloyPage = document.querySelector("#alloypage");
let contactButton = document.querySelector("#contactbutton");
let floatcontact = document.querySelector(".floatcontact1");
let position = 0;

rightButton.addEventListener("click", function(){
  if (position > -335) {
    position -= 84;
    alloypage.style.transform = "translate(" + position + "vw, 0)";
  }
});
leftButton.addEventListener("click", function(){
  if (position < 0) {
    position += 84;
    alloypage.style.transform = "translate(" + position + "vw, 0)";
  }
});


let rightPopular = document.querySelector("#popular-products-right");
let leftPopular = document.querySelector("#popular-products-left");
let popularProductsPart = document.querySelector("#popular-products-part");
let position2 = 6.5;

rightPopular.addEventListener("click", function(){
  if (position2 > -283.5) {
    position2 -= 29;
    popularProductsPart.style.transform = "translate(" + position2 + "vw, 0)";
  }
  leftPopular.style.pointerEvents = "inherit";
  leftPopular.style.opacity = 1;
  rightPopular.style.pointerEvents = "inherit";
  rightPopular.style.opacity = 1;
  if (position2 == -283.5) {
    rightPopular.style.pointerEvents = "none";
    rightPopular.style.opacity = 0;
  }
  if (position2 == 6.5) {
    leftPopular.style.pointerEvents = "none";
    leftPopular.style.opacity = 0;
  }
});
leftPopular.addEventListener("click", function(){
  if (position2 < 6.5) {
    position2 += 29;
    popularProductsPart.style.transform = "translate(" + position2 + "vw, 0)";
  }
  leftPopular.style.pointerEvents = "inherit";
  leftPopular.style.opacity = 1;
  rightPopular.style.pointerEvents = "inherit";
  rightPopular.style.opacity = 1;
  if (position2 == -283.5) {
    rightPopular.style.pointerEvents = "none";
    rightPopular.style.opacity = 0;
  }
  if (position2 == 6.5) {
    leftPopular.style.pointerEvents = "none";
    leftPopular.style.opacity = 0;
  }
});


let mode = 60000;
let rightButton2 = document.querySelector("#right-arrow");
let leftButton2 = document.querySelector("#left-arrow");
let mediaClass = document.querySelectorAll("#class-middle > a");

function mediaClassSwitch(mode, direction) {
  mediaClass[(mode + 0)%6].style = "opacity: 1; pointer-events: inherit; transform: translate(0, 0) skew(-15deg); z-index: 1;"
  mediaClass[(mode + 1)%6].style = "opacity: 1; pointer-events: none; transform: translate(77vw, 0) skew(-15deg); z-index: 0;"
  if (direction == "left") {
    mediaClass[(mode + 2)%6].style = "opacity: 0; pointer-events: none; transform: translate(154vw, 0) skew(-15deg); z-index: 0;"
    mediaClass[(mode + 3)%6].style = "opacity: 0; pointer-events: none; transform: translate(-154vw, 0) skew(-15deg); z-index: 0;"
    mediaClass[(mode + 4)%6].style = "opacity: 0; pointer-events: none; transform: translate(-154vw, 0) skew(-15deg); z-index: 0;"
  }else{
    mediaClass[(mode + 2)%6].style = "opacity: 0; pointer-events: none; transform: translate(154vw, 0) skew(-15deg); z-index: 0;"
    mediaClass[(mode + 3)%6].style = "opacity: 0; pointer-events: none; transform: translate(154vw, 0) skew(-15deg); z-index: 0;"
    mediaClass[(mode + 4)%6].style = "opacity: 0; pointer-events: none; transform: translate(-154vw, 0) skew(-15deg); z-index: 0;"

  }
  mediaClass[(mode + 5)%6].style = "opacity: 1; pointer-events: none; transform: translate(-77vw, 0) skew(-15deg); z-index: 0;"
}

rightButton2.addEventListener("click", function () {
  mode += 1;
  mediaClassSwitch(mode, "right");
});
leftButton2.addEventListener("click", function () {
  mode -= 1;
  mediaClassSwitch(mode, "left");
});


let btn = document.querySelectorAll(".time");
let square = document.querySelectorAll(".G-price");
for (let i = 0; i < btn.length; i++) {
    btn[i].addEventListener("click", function(){
        for (let j = 0; j < btn.length; j++) {
            btn[j].setAttribute("style", "background-color: #aaa;");
            square[j].setAttribute("style", "pointer-events: none; opacity: 0;");
        }
        btn[i].setAttribute("style", "background-color: #32558e;");
        square[i].setAttribute("style", "pointer-events: inherit; opacity: 1;");
    });
}


let compare = document.querySelectorAll(".compare");
let calculator = document.querySelectorAll(".calculator");
for (let i = 0; i < compare.length; i++) {
  compare[i].addEventListener("click", function(){
    press = 1;
    calcPage.style.transform = "translate(0, 0)";
    calcPage.style.pointerEvents = "inherit";
    calcPage.querySelector("iframe").src = "tools/nickel-alloy-grades-comparison.html";
    loadingCircle.style.opacity = "1";
    loadingCircle.style.pointerEvents = "inherit";
    setTimeout(function(){
      html.style.overflow = "hidden";
      html.style.height = "100%";
      loadingCircle.style.opacity = "0";
      loadingCircle.style.pointerEvents = "none";
    }, 3000);
  });
}
for (let i = 0; i < calculator.length; i++) {
  calculator[i].addEventListener("click", function(){
    press = 1;
    calcPage.style.transform = "translate(0, 0)";
    calcPage.style.pointerEvents = "inherit";
    calcPage.querySelector("iframe").src = "tools/nickel-alloy-weight-calculator.html";  
    loadingCircle.style.opacity = "1";
    loadingCircle.style.pointerEvents = "inherit";
    setTimeout(function(){
      html.style.overflow = "hidden";
      html.style.height = "100%";
      loadingCircle.style.opacity = "0";
      loadingCircle.style.pointerEvents = "none";
    }, 3000);
  });
}



let index = 0;
let screenWidth = window.screen.availWidth;
let proWidth = screenWidth*0.89;
let dotDiv = document.querySelectorAll("#dot-div > div");
let indexProductPage = document.querySelector("#index-product-page > div");


indexProductPage.addEventListener("touchstart", function (e) {
  startX = e.targetTouches[0].clientX;
  startY = e.targetTouches[0].clientY;
});
indexProductPage.addEventListener("touchmove", function (e) {
  moveX = e.targetTouches[0].clientX;
  distanceX = moveX - startX;
  moveY = e.targetTouches[0].clientY;
  distanceY = moveY - startY;
  if (Math.abs(distanceY) < Math.abs(distanceX)) {    
    e.preventDefault();
    indexProductPage.style.transition = "none";
    indexProductPage.style.left = -proWidth*index + screenWidth*0.075 + distanceX + "px";
  }
});
indexProductPage.addEventListener("touchend", function (e) {
  indexProductPage.style.transition = "left .2s ease-in-out";
  if (distanceX < -screenWidth*0.2 && index < 4) {
    index += 1;
  }else if (distanceX >= screenWidth*0.2 && index > 0) {
    index -= 1;
  }
  indexProductPage.style.left = -proWidth*index + screenWidth*0.075 + "px";
  for (let i = 0; i < dotDiv.length; i++) {
    dotDiv[i].style.opacity = "0.5";
  }
  dotDiv[index].style.opacity = "1";
});



let index2 = 0;
let classWidth = screenWidth*1.04;
let classDot = document.querySelectorAll("#class-dot > div");
let classMiddle = document.querySelector("#class-middle");


classMiddle.addEventListener("touchstart", function (e) {
  startX = e.targetTouches[0].clientX;
  startY = e.targetTouches[0].clientY;
});
classMiddle.addEventListener("touchmove", function (e) {
  moveX = e.targetTouches[0].clientX;
  distanceX = moveX - startX;
  moveY = e.targetTouches[0].clientY;
  distanceY = moveY - startY;
  if (Math.abs(distanceY) < Math.abs(distanceX)) {    
    e.preventDefault();
    classMiddle.style.transition = "none";
    classMiddle.style.left = -classWidth*index2 - screenWidth*1.04 + distanceX + "px";
  }
});
classMiddle.addEventListener("touchend", function (e) {
  classMiddle.style.transition = "left .2s ease-in-out";
  if (distanceX < -screenWidth*0.2 && index2 < 5) {
    index2 += 1;
  }else if (distanceX >= screenWidth*0.2 && index2 > 0) {
    index2 -= 1;
  }
  classMiddle.style.left = -classWidth*index2 - screenWidth*1.04 + "px";
  for (let i = 0; i < classDot.length; i++) {
    classDot[i].style.opacity = "0.5";
  }
  classDot[index2].style.opacity = "1";
});


let qFrame = document.querySelectorAll(".q-frame");
let faqFrame = document.querySelectorAll(".faq-frame");

for (let i = 0; i < qFrame.length; i++) {
  qFrame[i].addEventListener("click", () => {
    faqFrame[i].className = (faqFrame[i].className == "faq-frame faq-v")?"faq-frame faq-u":"faq-frame faq-v";
  });
}