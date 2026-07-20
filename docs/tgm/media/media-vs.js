let contentButton2 = document.querySelectorAll("#content-button-2 > div");


function getPageTop(){  
  let pageTop = [];
  let section = document.querySelectorAll("article h2");
  for (let i = 0; i < section.length; i++) {
    pageTop.push(section[i].offsetTop);
  }
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

for (let i = 0; i < contentButton2.length; i++) {
  pageScroll(contentButton2[i], i, -50);
}

document.addEventListener("mousewheel", function(){
  clearInterval(navTimer);
});