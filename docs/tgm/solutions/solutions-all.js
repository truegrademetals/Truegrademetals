let proCard = document.querySelectorAll(".products-card");
let proDetail = document.querySelectorAll(".products-detail");
let proPage = document.querySelector("#products-page");
let gradeBtn = document.querySelectorAll("#grade-title > div");
let gradePage = document.querySelectorAll("#grade-section > div");
let titleMore = document.querySelector("#title-more");
let descriptionSection = document.querySelector("#description-section").offsetTop;
let productBtn = document.querySelectorAll("#product-title > div");
let productsPage = document.querySelector("#products-page").offsetTop;
navMode = 1;

for (let i = 0; i < proCard.length; i++) {
  proCard[i].addEventListener("mouseenter", function(){
    proPage.className = "products-page-2";
    for (let j = 0; j < proDetail.length; j++) {
      proDetail[j].style = "opacity: 0; pointer-events: none;"
    }
    proDetail[i].style = "opacity: 1; pointer-events: inherit;"
  });
  proCard[i].addEventListener("mouseleave", function(){
    proPage.className = "products-page-1";
    for (let j = 0; j < proDetail.length; j++) {
      proDetail[j].style = "opacity: 0; pointer-events: none;";
    }
  });
}

let pageTop = [];
for (let i = 0; i < gradePage.length; i++) {
  pageTop.push(gradePage[i].offsetTop);
}

let navTimer;
function pageScroll(btn, page, num=0) {
  btn.addEventListener("click", function(){
    let navTime = 0.02;
    navTimer = setInterval(function(){
      html.scrollTop += (page - html.scrollTop + num)*navTime;
      navTime += 0.01;
      if (html.scrollTop == page + num) {
        clearInterval(navTimer);
      }
    }, 10);
  });
}
for (let i = 0; i < gradeBtn.length; i++) {
  pageScroll(gradeBtn[i], pageTop[i], -100);
}
for (let i = 0; i < productBtn.length; i++) {
  pageScroll(productBtn[i], productsPage, -100);
  productBtn[i].addEventListener("click", function(){
    proPage.style.height = "65vw";
    for (let j = 0; j < proDetail.length; j++) {
      proDetail[j].style = "opacity: 0; pointer-events: none;";
    }
    proDetail[i].style = "opacity: 1; pointer-events: inherit;";
  });
}
pageScroll(titleMore, descriptionSection);
document.addEventListener("mousewheel", function(){
  clearInterval(navTimer);
});