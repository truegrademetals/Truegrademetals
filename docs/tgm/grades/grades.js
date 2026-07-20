let learnButton = document.querySelector("#learn-button-1");
let learnButton2 = document.querySelectorAll("#learn-button-2 > div");


function getPageTop(){  
  let pageTop = [];
  let section = document.querySelectorAll("main > section");
  for (let i = 0; i < section.length; i++) {
    pageTop.push(section[i].offsetTop);
  }
  pageTop.splice(0, 1);
  pageTop.splice(pageTop.length-1, 1);  
  pageTop[0] -= 50;
  return pageTop;
}

let navTimer;
function pageScroll(btn, page, num=0) {
  btn.addEventListener("click", function(){
    let navTime = 0.02;
    navTimer = setInterval(function(){
      html.scrollTop += (getPageTop()[page] - html.scrollTop + num)*navTime;
      navTime += 0.01;
      if (html.scrollTop >= getPageTop()[page] + num - 1 & html.scrollTop <= getPageTop()[page] + num + 1) {
        clearInterval(navTimer);
      }
    }, 10);
  });
}

for (let i = 0; i < learnButton2.length; i++) {
  pageScroll(learnButton2[i], i, -50);
}
pageScroll(learnButton, 1, -50);

document.addEventListener("mousewheel", function(){
  clearInterval(navTimer);
});



let fold = document.querySelector("#fold");
let fold2 = document.querySelector("#fold2");
let dataSheet = document.querySelector("#data-sheet");

let fold3 = document.querySelector("#fold3");
let fold4 = document.querySelector("#fold4");
let mediaPage = document.querySelector("#media-page");

let fold5 = document.querySelector("#fold5");
let fold6 = document.querySelector("#fold6");
let introPage = document.querySelector("#intro-page");


if(fold != null && fold2 != null){
  fold.addEventListener("click", function(){
    dataSheet.className = "fold2";
    fold.style.opacity = "0";
    fold.style.pointerEvents = "none";
  });
  fold2.addEventListener("click", function(){
    dataSheet.className = "fold2";
    fold2.style.opacity = "0";
    fold2.style.pointerEvents = "none";
  });  
}

if(fold3 != null && fold4 != null){
  fold3.addEventListener("click", function(){
    mediaPage.className = "fold4";
    fold3.style.opacity = "0";
    fold3.style.pointerEvents = "none";
  });
  fold4.addEventListener("click", function(){
    mediaPage.className = "fold4";
    fold4.style.opacity = "0";
    fold4.style.pointerEvents = "none";
  });
}

if(fold5 != null && fold6 != null){
  fold5.addEventListener("click", function(){
    introPage.className = "fold6";
    fold5.style.opacity = "0";
    fold5.style.pointerEvents = "none";
  });
  fold6.addEventListener("click", function(){
    introPage.className = "fold6";
    fold6.style.opacity = "0";
    fold6.style.pointerEvents = "none";
  });
}



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
  proCard[i].addEventListener("mouseleave", function(){
    proPage.className = "products-page-1";
    for (let j = 0; j < proDetail.length; j++) {
      proDetail[j].style = "opacity: 0; pointer-events: none;";
    }
  });
}



//自动填充

function tagDel(x) {
  y = x.innerHTML.replace(/<[^<]+>/g, '').replace(/\s+/g, ' ').replace(/(\r\n|\n|\r)/gm, "").trim();
  return y;
}

let bigContactBtn = document.querySelector("#contactbutton");
let smallContactBtn = document.querySelectorAll(".contactbutton-2");
let mainTitle = document.querySelector("#main-title > h1");
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


let qFrame = document.querySelectorAll(".q-frame");
let faqFrame = document.querySelectorAll(".faq-frame");

for (let i = 0; i < qFrame.length; i++) {
  qFrame[i].addEventListener("click", () => {
    faqFrame[i].className = (faqFrame[i].className == "faq-frame faq-v")?"faq-frame faq-u":"faq-frame faq-v";
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