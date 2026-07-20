html = document.querySelector("html");
let vw = document.body.clientWidth/100;
let vh = document.body.clientHeight/100;
let domArr = [
	"#mission",
	"#vision",
	"#values",
	"#wcu-head",
	"#raw",
	"#stock",
	"#process",
	"#finish",
	"#quality",
	"#package",
	"#story-head",
	"#story-1",
	"#story-2",
	"#story-3",
]

function getElementTop(elem){
　　let elemTop = elem.offsetTop;
　　elem = elem.offsetParent;
　　while(elem != null){
　　　　elemTop += elem.offsetTop;
　　　　elem = elem.offsetParent;
　　}
　　return elemTop;
}
function scrollTranslate(p1, p2, n1, n2, y) {
  document.addEventListener("mousewheel", () => {
    if (html.scrollTop >= p1 && html.scrollTop <= p2) {
      y.style.transform = "translate(" + n1*(html.scrollTop - p2)/(p1 - p2) + "vw, " + n2*(html.scrollTop - p2)/(p1 - p2) + "vw)";
    }else if (html.scrollTop <= p1) {
      y.style.transform = "translate(" + n1 + "vw, " + n2 + "vw)";
    }else if (html.scrollTop >= p2) {
      y.style.transform = "translate(" + 0 + "vw, " + 0 + "vw)";
    }
  });
}
function scrollOpacity(p1, p2, n1, n2, y) {
  document.addEventListener("mousewheel", () => {
    if (html.scrollTop >= p1 && html.scrollTop <= p2) {
      y.style.opacity = ((n1 - n2)*html.scrollTop - n1*p2 + n2*p1)/(p1 - p2);
    }else if (html.scrollTop <= p1) {
      y.style.opacity = n1;
    }else if (html.scrollTop >= p2) {
      y.style.opacity = n2;
    }
  });
}



if (window.SIZE == 'Sm'){
  for (let i = 0; i < domArr.length; i++) {
    let floatTop = getElementTop(document.querySelector(domArr[i]));
    scrollTranslate(floatTop-206*vw, floatTop-84*vw, 0, 10, document.querySelector(domArr[i]));
    scrollOpacity(floatTop-182*vw, floatTop-84*vw, 0, 1, document.querySelector(domArr[i]));
  }
}else{
  for (let i = 0; i < domArr.length; i++) {
    let floatTop = getElementTop(document.querySelector(domArr[i]));
    scrollTranslate(floatTop-62*vw, floatTop-28*vw, 0, 10, document.querySelector(domArr[i]));
    scrollOpacity(floatTop-54*vw, floatTop-28*vw, 0, 1, document.querySelector(domArr[i]));
  }
}
