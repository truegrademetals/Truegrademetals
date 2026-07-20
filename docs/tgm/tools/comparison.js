//初始变量
let num = 0;
let grade = "";
let start = 0;

//DOM元素
let grPlus = document.querySelectorAll(".gr-plus");
let gradeButton = document.querySelectorAll(".grade-button");
let matSelect = document.querySelector("#mat-select");
let compPage = document.querySelector("#comp-page");
let grTable = document.querySelector("#gr-table");
let chemical = document.querySelectorAll(".chemical");
let loading = document.querySelector("#loading");
let mouse = document.querySelector("#mouse");
let tips = document.querySelector("#tips");

//最大化函数
function maximum(arr) {
	let max = 0;
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] > max) {
			max = arr[i]
		}		
	}
	return max;
}

//滚动函数
function scrollColumn(item, mode) {
	let scrollL = item.scrollLeft;
	if (mode < 0) {
		for (var i = 1; i < 201; i++) {
			setTimeout(function(){
				item.scrollLeft += 1;
			}, i);
		}		
	}else if (mode > 0) {
		for (var i = 1; i < 201; i++) {
			setTimeout(function(){
				item.scrollLeft -= 1;
			}, i);
		}		
	}
}

//布局函数
function rank() {
	let elementWidth = [];
	let elementWidthReverse = [];
	let elementWidthMax = [];
	for (let i = 0; i < chemical.length; i++) {
		let element = chemical[i].querySelectorAll(".element");
		for (let j = 0; j < element.length; j++) {
			element[j].querySelector(".chemeicalp").style.color = "#fff";
		}
	}
	for (let i = 0; i < chemical.length; i++) {
		elementWidth.push([]);
		let element = chemical[i].querySelectorAll(".element");
		for (let j = 0; j < element.length; j++) {
			elementWidth[i].push(element[j].offsetWidth);
			if (element[j].offsetWidth == 0) {
				element[j].querySelector(".chemeicalp").style.color = "transparent";
			}
		}
	}
	for (let i = 0; i < elementWidth.length; i++) {
		for (let j = 0; j < elementWidth[i].length; j++) {
			if (i == 0) {
				elementWidthReverse.push([]);
			}
			elementWidthReverse[j].push(elementWidth[i][j]);
		}
	}
	for (let i = 0; i < elementWidthReverse.length; i++) {
		elementWidthMax.push(maximum(elementWidthReverse[i]));
	}
	for (let i = 0; i < chemical.length; i++) {
		let bar = chemical[i].querySelectorAll(".ele-frame");
		for (let j = 0; j < bar.length; j++) {
			if (elementWidthMax[j] == 0) {
				bar[j].style.padding = 0;
				bar[j].style.overflow = "hidden";
				bar[j].style.width = 0 + "px";
			}else{				
				bar[j].style.padding = "0 0 0 10vw";
				bar[j].style.overflow = "inherit";
				bar[j].style.width = elementWidthMax[j] + 10 + "px";
			}
		}
		bar[bar.length - 1].style.overflow = "hidden";
		bar[bar.length - 2].style.overflow = "hidden";
		bar[bar.length - 3].style.overflow = "hidden";
		bar[bar.length - 4].style.overflow = "hidden";
	}
	console.log(elementWidth);
}

//布局
rank();

//选择材质
for (let i = 0; i < grPlus.length; i++) {
	grPlus[i].addEventListener("click", function(){
		num = i;
		matSelect.style.opacity = "1";
		matSelect.style.pointerEvents = "inherit";
		compPage.style.opacity = "0";
		compPage.style.pointerEvents = "none";
		tips.style.opacity = "0";
		tips.style.pointerEvents = "none";
	});
}

//选定材质
for (let i = 0; i < gradeButton.length; i++) {
	gradeButton[i].addEventListener("click", function(){
		grade = gradeButton[i].querySelector("div").innerHTML;
		grPlus[num].innerHTML = grade;
		chemical[num].id = "G" + grade;
		loading.style.opacity = "1";
		setTimeout(function(){
			if (start == 0) {
				start = 1;
				mouse.style.opacity = 1;
			}
			matSelect.style.opacity = "0";
			matSelect.style.pointerEvents = "none";
			compPage.style.opacity = "1";
			compPage.style.pointerEvents = "inherit";
			rank();
		}, 300);
		setTimeout(function(){
			loading.style.opacity = "0";
		}, 500);
		html.scrollTop = 0;
	});
}

//鼠标滚动
grTable.addEventListener("mousewheel", function (e) {
	mouse.style.opacity = 0;
	if (e.wheelDelta < 0) {
		scrollColumn(grTable, -1);
	}else if (e.wheelDelta > 0) {
		scrollColumn(grTable, 1);
	}
	e.preventDefault();
});