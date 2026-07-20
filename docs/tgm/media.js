let mediaButton = document.querySelectorAll("#media-btn > a");
let mediaButtonBig = document.querySelector("#media-btn");
let mediaBG = document.querySelectorAll("#media-bg > div");
let mainTag = document.querySelector("main");
let titleText = ["BLOG", "TOOLS", "GALLERY"];

for (let i = 0; i < mediaButton.length; i++) {
  mediaButton[i].addEventListener("mouseenter", function () {
    mediaBG[i].style = "opacity: 1;";
    mainTag.style = "color: #eee;";
    mainTag.dataset.bg = titleText[i];
  });
  mediaButton[i].addEventListener("mouseleave", function () {
    mediaBG[i].style = "opacity: 0;";
    mainTag.style = "color: #333;";
  });
}
mediaButtonBig.addEventListener("mouseleave", function () {
  mainTag.dataset.bg = "MEDIA";
});