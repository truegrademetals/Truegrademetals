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

let proCard = document.querySelectorAll(".products-card");
let proDetail = document.querySelectorAll(".products-detail");
let proPage = document.querySelector("#products-page");



for (let i = 0; i < proCard.length; i++) {
  proCard[i].addEventListener("mouseenter", function(){
    proPage.className = "products-page-2";
    for (let j = 0; j < proDetail.length; j++) {
      proDetail[j].style = "opacity: 0; pointer-events: none;";
    }
    proDetail[i].style = "opacity: 1; pointer-events: inherit;";
  });
}


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