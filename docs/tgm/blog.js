let mode = 60000;
let rightButton = document.querySelector("#right-arrow");
let leftButton = document.querySelector("#left-arrow");
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

rightButton.addEventListener("click", function () {
  mode += 1;
  mediaClassSwitch(mode, "right");
});
leftButton.addEventListener("click", function () {
  mode -= 1;
  mediaClassSwitch(mode, "left");
});





let index2 = 0;
let screenWidth = window.screen.availWidth;
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

