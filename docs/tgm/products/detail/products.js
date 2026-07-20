let elementsContent = document.querySelectorAll(".chemicalc > div");
let elements = document.querySelectorAll(".chemicalc > div > div");
for (var i = 0; i < elements.length; i++) {
  if(elements[i].offsetWidth == 0){
    elementsContent[i].style.display = "none";
  }
}


let alloyPage = document.querySelector("#alloypage");
let se = document.querySelectorAll(".s-e-1, .s-e-2");
let floatcontact = document.querySelector(".floatcontact1");
let position = 0;



let index3 = 0;
let screenWidth = window.screen.availWidth;
let proWidth = screenWidth*1.04;
let proDot = document.querySelectorAll("#pro-dot > div");
let chooseDiv = document.querySelector("#choose-div");


chooseDiv.addEventListener("touchstart", function (e) {
  startX = e.targetTouches[0].clientX;
  startY = e.targetTouches[0].clientY;
});
chooseDiv.addEventListener("touchmove", function (e) {
  moveX = e.targetTouches[0].clientX;
  distanceX = moveX - startX;
  moveY = e.targetTouches[0].clientY;
  distanceY = moveY - startY;
  if (Math.abs(distanceY) < Math.abs(distanceX)) {    
    e.preventDefault();
    chooseDiv.style.transition = "none";
    chooseDiv.style.left = -proWidth*index3 - screenWidth*1.08 + distanceX + "px";
  }
});
chooseDiv.addEventListener("touchend", function (e) {
  chooseDiv.style.transition = "left .2s ease-in-out";
  if (distanceX < -screenWidth*0.2 && index3 < proDot.length-1) {
    index3 += 1;
  }else if (distanceX >= screenWidth*0.2 && index3 > 0) {
    index3 -= 1;
  }
  chooseDiv.style.left = -proWidth*index3 - screenWidth*1.08 + "px";
  for (let i = 0; i < proDot.length; i++) {
    proDot[i].style.opacity = "0.5";
  }
  proDot[index3].style.opacity = "1";
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