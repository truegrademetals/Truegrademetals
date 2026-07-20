let shareBtn = document.querySelectorAll(".share-btn");
for (let i = 0; i < shareBtn.length; i++) {
	shareBtn[i].addEventListener("click", function () {
		window.open(shareBtn[i].href, "new", "width=800, height=500");
	});
}

let mainBody = document.querySelector("#main-body");
let mainPage = document.querySelector("#media-page").offsetTop;



let navTimer;
function pageScroll(btn, page, num=0) {
  btn.addEventListener("click", function(){
    let navTime = 0.02;
    navTimer = setInterval(function(){
      html.scrollTop += (page - html.scrollTop + num)*navTime;
      navTime += 0.01;
      if (html.scrollTop >= page + num - 1 && html.scrollTop <= page + num + 1) {
        clearInterval(navTimer);
      }
    }, 10);
  });
}

pageScroll(mainBody, mainPage, -50);

document.addEventListener("mousewheel", function(){
  clearInterval(navTimer);
});


let tableContainer = document.querySelectorAll(".table-container");
let fold01 = document.querySelectorAll(".fold01");

for (let i = 0; i < fold01.length; i++) {
  fold01[i].addEventListener("click", ()=>{
    tableContainer[i].className = "table-container fold2";
    fold01[i].style.opacity = 0;
    fold01[i].style.pointerEvents = "none";
  })
}