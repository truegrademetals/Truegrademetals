let body = document.querySelector("body");
let arrowUp = document.querySelector("#arrowup");
let floatButton = document.querySelectorAll(".click-event");
let floatCross = document.querySelector("#floatcross");
let floatBack = document.querySelector("#float-back");
let floatContact = document.querySelector("#floatcontact");
let html = document.querySelector("html");
let errorMessage2 = document.getElementById('errorMessage2');
let email2 = document.getElementById('aside-email');
let errorMessage3 = document.getElementById('errorMessage3');
let email3 = document.getElementById('footer-email');
let emailTrue = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.]){1,2}[A-Za-z\d]{2,5}$/;
let copyButton = document.querySelectorAll(".copy-button");
let inputCopy = document.querySelector("#input-copy > input");
let copyText = document.querySelectorAll(".copy-text");
let vw = document.body.clientWidth/100;
let vh = document.body.clientHeight/100;
let vh2 = window.screen.height/100;



(function(doc, win) {
  let screenWidth = 0, size = 'M', root = doc.documentElement;
  if (window.screen && screen.width) {
      screenWidth = screen.width;
      if (screenWidth > 1920) {
          size = 'L';
      } else if (screenWidth < 600) {
          size = 'Sm';
      }
  }
  root.className = size;
  win.SIZE = size;
})(document, window);


for (let i = 0; i < copyButton.length; i++) {
  copyButton[i].addEventListener("click", function () {
    inputCopy.select();
    document.execCommand("copy");
    copyText[i].style = "opacity: 1; pointer-events: inherit;"
  });
}

arrowUp.addEventListener("click", function () {
  let scTime = 0.05;
  let timer;
  timer = setInterval(function(){
    if (html.scrollTop <= 0) {
      clearInterval(timer);
    }
    html.scrollTop -= html.scrollTop*scTime;
    scTime += 0.01;
  }, 1);
});

for (var i = 0; i < floatButton.length; i++) {
  floatButton[i].addEventListener("click", () => {
    floatContact.className = (floatContact.className == "floatcontact1")?"floatcontact2":"floatcontact1";
  });
}

floatCross.addEventListener("click", () => {
  floatContact.className = (floatContact.className == "floatcontact1")?"floatcontact2":"floatcontact1";
});
floatBack.addEventListener("click", () => {
  floatContact.className = (floatContact.className == "floatcontact1")?"floatcontact2":"floatcontact1";
});

let navButton = document.querySelector("#nav-btn");
let nav = document.querySelector("nav");
navButton.addEventListener("click", () => {
  nav.className = (nav.className == "nav-1")?"nav-2":"nav-1";
});
// if (window.SIZE != 'Sm'){
//   window.addEventListener("scroll", () => {
//     let bodyScrollTop = html.scrollTop;
//     if (bodyScrollTop >= 3.5*vw) {
//       nav.style.position = 'fixed';
//       nav.style.top = '0';
//     } else {
//       nav.style.position = 'absolute';
//       nav.style.top = '3.5vw';
//     }
//   });
//   window.addEventListener("load", () => {
//     let bodyScrollTop = html.scrollTop;
//     if (bodyScrollTop >= 3.5*vw) {
//       nav.style.position = 'fixed';
//       nav.style.top = '0';
//     } else {
//       nav.style.position = 'absolute';
//       nav.style.top = '3.5vw';
//     }
//   });
// }



document.getElementById('floatform').onsubmit=function(){
  if(email2.value=="" || email2.value=="info@truegrademetals.com" || email2.value=="info@truegrademetals.com"){
    errorMessage2.innerHTML="Please input your E-mail";
    return false;
  }else if(!emailTrue.test(email2.value)){
    errorMessage2.innerHTML="Please input the right E-mail";
    return false;
  }else{
    errorMessage2.innerHTML="&emsp;";
    return true;
    feedback();
  };
};

document.getElementById('footer-form').onsubmit=function(){
  if(email3.value=="" || email3.value=="info@truegrademetals.com" || email3.value=="info@truegrademetals.com"){
    errorMessage3.innerHTML="Please input your E-mail";
    return false;
  }else if(!emailTrue.test(email3.value)){
    errorMessage3.innerHTML="Please input the right E-mail";
    return false;
  }else{
    errorMessage3.innerHTML="&emsp;";
    return true;
    feedback();
  };
};


let sendData = document.querySelector("#send-data");
for (let i = 0; i < floatButton.length; i++) {
  floatButton[i].addEventListener("mouseenter", () => {
    sendData.style.opacity = 0;
    sendData.style.pointerEvents = "none";
    bookmarkOut = 1;
  });
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "send-data.html", true);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.send("");
}