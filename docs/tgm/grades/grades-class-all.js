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


//自动填充

function tagDel(x) {
  y = x.innerHTML.replace(/<[^<]+>/g, '').replace(/\s+/g, ' ').replace(/(\r\n|\n|\r)/gm, "").trim();
  return y;
}

let bigContactBtn = document.querySelector(".contactbutton");
let smallContactBtn = document.querySelectorAll(".contactbutton-2");
let mainTitle = document.querySelector(".grade-div-1 > h1");
let proTitle = document.querySelectorAll(".products-main > p");
let asideSubject = document.querySelector("#aside-subject");

bigContactBtn.addEventListener("click", () => {
  asideSubject.value = tagDel(mainTitle);
});
if (smallContactBtn !== null) {
  for (let i = 0; i < smallContactBtn.length; i++) {
    smallContactBtn[i].addEventListener("click", () => {
      asideSubject.value = tagDel(proTitle[i]);
    });
  }
}

let footerSubject = document.querySelector("#footer-subject");
footerSubject.value = tagDel(mainTitle);


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