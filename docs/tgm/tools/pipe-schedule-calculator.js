let nps1 = document.querySelectorAll(".NPS-1");//NPS按钮
let nps2 = document.querySelectorAll(".NPS-2");//NPS选择
let dn1 = document.querySelectorAll(".DN-1");//DN按钮
let dn2 = document.querySelectorAll(".DN-2");//DN选择
let sch1 = document.querySelectorAll(".SCH-1");//SCH按钮
let sch2 = document.querySelectorAll(".SCH-2");//SCH选择
let pipeResult = document.querySelectorAll(".pipe-result");//结果
let mode = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]];
let dn0 = ["", "", "", ""];
let sch0 = ["", "", "", ""];
let mainSection = document.querySelector("#main-section");//整个计算区域
let calcSection = document.querySelector(".calc-section").cloneNode(true);//行
let plusButton = document.querySelector("#plus-button");//增加行
let bookmarkOut = 0;
let ctaState = 0;
let bookmark = document.querySelector("#bookmark");
let calcCTA = document.querySelector("#calc-cta");
let calcContactCross = document.querySelector("#calc-contact-cross");

//书签
bookmark.addEventListener("mouseenter", () => {
	bookmark.style.opacity = 0;
	bookmark.style.pointerEvents = "none";
	bookmarkOut = 1;
});
calcContactCross.addEventListener("click", () => {
	calcCTA.style.opacity = 0;
	calcCTA.style.pointerEvents = "none";
	calcCTA.style.transform = "translate(0, 10vw)";
	ctaState = 1;
});

let schedule = {
	0:["OD", "5", "5S", "10", "10S", "20", "30", "40", "40S", "60", "80", "80S", "100", "120", "140", "160", "XS", "XXS", "STD"], 
	6:[10.3, "-", "-", 1.24, 1.24, "-", 1.45, 1.73, 1.73, "-", 2.41, 2.41, "-", "-", "-", 3.15, 2.41, 4.83, 1.73], 
	8:[13.7, "-", "-", 1.65, 1.65, "-", 1.85, 2.24, 2.24, "-", 3.02, 3.02, "-", "-", "-", 3.68, 3.02, 6.05, 2.24], 
	10:[17.1, "-", "-", 1.65, 1.65, "-", 1.85, 2.31, 2.31, "-", 3.2, 3.2, "-", "-", "-", 4.01, 3.2, 6.4, 2.31], 
	15:[21.3, 1.65, 1.65, 2.11, 2.11, "-", 2.41, 2.77, 2.77, "-", 3.73, 3.73, "-", "-", "-", 4.78, 3.73, 7.47, 2.77], 
	20:[26.7, 1.65, 1.65, 2.11, 2.11, "-", 2.41, 2.87, 2.87, "-", 3.91, 3.91, "-", "-", "-", 5.56, 3.91, 7.82, 2.87], 
	25:[33.4, 1.65, 1.65, 2.77, 2.77, "-", 2.9, 3.38, 3.38, "-", 4.55, 4.55, "-", "-", "-", 6.35, 4.55, 9.09, 3.38], 
	32:[42.2, 1.65, 1.65, 2.77, 2.77, "-", 2.97, 3.56, 3.56, "-", 4.85, 4.85, "-", "-", "-", 6.35, 4.85, 9.7, 3.56], 
	40:[48.3, 1.65, 1.65, 2.77, 2.77, "-", 3.18, 3.68, 3.68, "-", 5.08, 5.08, "-", "-", "-", 7.14, 5.08, 10.15, 3.68], 
	50:[60.3, 1.65, 1.65, 2.77, 2.77, "-", 3.18, 3.91, 3.91, "-", 5.54, 5.54, "-", "-", "-", 8.74, 5.54, 11.07, 3.91], 
	65:[73, 2.11, 2.11, 3.05, 3.05, "-", 4.78, 5.16, 5.16, "-", 7.01, 7.01, "-", "-", "-", 9.53, 7.01, 14.02, 5.16], 
	80:[88.9, 2.11, 2.11, 3.05, 3.05, "-", 4.78, 5.49, 5.49, "-", 7.62, 7.62, "-", "-", "-", 11.13, 7.62, 15.24, 5.49], 
	90:[101.6, 2.11, 2.11, 3.05, 3.05, "-", 4.78, 5.74, 5.74, "-", 8.08, 8.08, "-", "-", "-", "-", 8.08, "-", 5.74], 
	100:[114.3, 2.11, 2.11, 3.05, 3.05, "-", 4.78, 6.02, 6.02, "-", 8.56, 8.56, "-", 11.13, "-", 13.49, 8.56, 17.12, 6.02], 
	125:[141.3, 2.77, 2.77, 3.4, 3.4, "-", "-", 6.55, 6.55, "-", 9.53, 9.53, "-", 12.7, "-", 15.88, 9.53, 19.05, 6.55], 
	150:[168.3, 2.77, 2.77, 3.4, 3.4, "-", "-", 7.11, 7.11, "-", 10.97, 10.97, "-", 14.27, "-", 18.26, 10.97, 21.95, 7.11], 
	200:[219.1, 2.77, 2.77, 3.76, 3.76, 6.35, 7.04, 8.18, 8.18, 10.31, 12.7, 12.7, 15.09, 18.26, 20.62, 23.01, 12.7, 22.23, 8.18], 
	250:[273.1, 3.4, 3.4, 4.19, 4.19, 6.35, 7.8, 9.27, 9.27, 12.7, 15.09, 12.7, 18.26, 21.44, 25.4, 28.58, 12.7, 25.4, 9.27], 
	300:[323.9, 3.96, 3.96, 4.57, 4.57, 6.35, 8.38, 10.31, 9.53, 14.27, 17.48, 12.7, 21.44, 25.4, 28.58, 33.32, 12.7, 25.4, 9.53], 
	350:[355.6, 3.96, 3.96, 6.35, 4.78, 7.92, 9.53, 11.13, 9.53, 15.09, 19.05, 12.7, 23.83, 27.79, 31.75, 35.71, 12.7, "-", 9.53], 
	400:[406.4, 4.19, 4.19, 6.35, 4.78, 7.92, 9.53, 12.7, 9.53, 16.66, 21.44, 12.7, 26.19, 30.96, 36.53, 40.49, 12.7, "-", 9.53], 
	450:[457.2, 4.19, 4.19, 6.35, 4.78, 7.92, 11.13, 14.27, 9.53, 19.05, 23.83, 12.7, 29.36, 34.93, 39.67, 45.24, 12.7, "-", 9.53], 
	500:[508, 4.78, 4.78, 6.35, 5.54, 9.53, 12.7, 15.09, 9.53, 20.62, 26.19, 12.7, 32.54, 38.1, 44.45, 50.01, 12.7, "-", 9.53], 
	550:[559, 4.78, 4.78, 6.35, 5.54, 9.53, 12.7, "-", 9.53, 22.23, 28.58, 12.7, 34.93, 41.28, 47.63, 53.98, 12.7, "-", 9.53], 
	600:[610, 5.54, 5.54, 6.35, 6.35, 9.53, 14.27, 17.48, 9.53, 24.61, 30.96, 12.7, 38.89, 46.02, 52.37, 59.54, 12.7, "-", 9.53], 
	650:[660, "-", "-", 7.92, "-", 12.7, "-", "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	700:[711, "-", "-", 7.92, "-", 12.7, 15.88, "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	750:[762, 6.35, 6.35, 7.92, 7.92, 12.7, 15.88, "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	800:[813, "-", "-", 7.92, "-", 12.7, 15.88, 17.48, 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	850:[864, "-", "-", 7.92, "-", 12.7, 15.88, 17.48, 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	900:[914, "-", "-", 7.92, "-", 12.7, 15.88, 19.05, 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	950:[965, "-", "-", "-", "-", "-", "-", "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	1000:[1016, "-", "-", "-", "-", "-", "-", "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	1050:[1067, "-", "-", "-", "-", "-", "-", "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	1100:[1118, "-", "-", "-", "-", "-", "-", "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	1150:[1168, "-", "-", "-", "-", "-", "-", "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53], 
	1200:[1219, "-", "-", "-", "-", "-", "-", "-", 9.53, "-", "-", 12.7, "-", "-", "-", "-", 12.7, "-", 9.53],  
};

function indexInArr(arr, str) {
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] == str) {
			return i;
		}
	}
}//查找数组中某一个值的索引
function mainButtonClick(arr1, arr2, str1, str2) {
	arr1.addEventListener("click", function () {
		for (let j = 0; j < nps1.length; j++) {
			nps2[j].className = "NPS-2 invisible";
			dn2[j].className = "DN-2 invisible";
			sch2[j].className = "SCH-2 invisible";
		}
		arr2.className = (arr2.className == str2)?str1:str2;
	});
}//点击按钮弹出选择框
function smallButtonClick(arr1, i, j, button3, swt) {//当前小按钮，当前行，当前小按钮的索引，当前行的所有小按钮，外径或壁厚
	arr1.addEventListener("click", function () {
		for (let k = 0; k < nps1.length; k++) {
			nps2[k].className = "NPS-2 invisible";
			dn2[k].className = "DN-2 invisible";
			sch2[k].className = "SCH-2 invisible";
		}//选择框隐藏
		if (swt == 0) {//点击nps或dn
			nps1[i].innerHTML = "NPS " + button3[0][j].innerHTML;//填充对应按钮
			dn1[i].innerHTML = "DN " + button3[1][j].innerHTML;//填充对应按钮
			dn0[i] = button3[1][j].innerHTML;//存储当前小按钮对应的dn值
			nps1[i].style.color = "#32558e";//修改大按钮颜色
			dn1[i].style.color = "#32558e";//修改大按钮颜色
			mode[i][0] = 1;//当前行的外径已选择
		} else {//点击sch
			sch1[i].innerHTML = "SCH " + button3[2][j].innerHTML;//填充对应按钮
			sch0[i] = button3[2][j].innerHTML;//存储当前小按钮对应的sch值
			sch1[i].style.color = "#32558e";//修改大按钮颜色
			mode[i][1] = 1;//当前行的壁厚已选择
		}
		if (mode[i][0] == 1 && mode[i][1] == 1) {
			let ODFinal = schedule[dn0[i]][0];
			let THKFinal = schedule[dn0[i]][indexInArr(schedule[0], sch0[i])];
			pipeResult[i].innerHTML = ODFinal + "×" + THKFinal;
			pipeResult[i].style.color = "#32558e";
			
			setTimeout(() => {
				if (bookmarkOut == 0) {
					bookmark.style.opacity = 1;
					bookmark.style.pointerEvents = "inherit";
				}
			}, 10000);
			setTimeout(() => {
				if (ctaState == 0) {
					calcCTA.style.opacity = 1;
					calcCTA.style.pointerEvents = "inherit";
					calcCTA.style.transform = "translate(0, 0)";
				}
			}, 5000);
		}
	});
}//点击小按钮

//主函数
for (let i = 0; i < nps1.length; i++) {
	mainButtonClick(nps1[i], nps2[i], "NPS-2 visible", "NPS-2 invisible");//点击nps大按钮
	mainButtonClick(dn1[i], dn2[i], "DN-2 visible", "DN-2 invisible");//点击dn大按钮
	mainButtonClick(sch1[i], sch2[i], "SCH-2 visible", "SCH-2 invisible");//点击sch大按钮
	let nps3 = nps2[i].querySelectorAll("div");//当前行的所有nps小按钮
	let dn3 = dn2[i].querySelectorAll("div");//当前行的所有dn小按钮
	let sch3 = sch2[i].querySelectorAll("div");//当前行的所有sch小按钮
	let button3 = [nps3, dn3, sch3];//当前行的所有小按钮
	for (let j = 0; j < nps3.length; j++) {
		smallButtonClick(nps3[j], i, j, button3, 0);
		smallButtonClick(dn3[j], i, j, button3, 0);
	}
	for (let j = 0; j < sch3.length; j++) {
		smallButtonClick(sch3[j], i, j, button3, 1);
	}
}

//添加新行
plusButton.addEventListener("click", function () {
	mainSection.appendChild(calcSection);
	calcSection = document.querySelector(".calc-section").cloneNode(true);
	nps1 = document.querySelectorAll(".NPS-1");
	nps2 = document.querySelectorAll(".NPS-2");
	dn1 = document.querySelectorAll(".DN-1");
	dn2 = document.querySelectorAll(".DN-2");
	sch1 = document.querySelectorAll(".SCH-1");
	sch2 = document.querySelectorAll(".SCH-2");
	pipeResult = document.querySelectorAll(".pipe-result");
	mode.push([0, 0]);
	for (let i = 0; i < nps1.length; i++) {
		mainButtonClick(nps1[i], nps2[i], "NPS-2 visible", "NPS-2 invisible");
		mainButtonClick(dn1[i], dn2[i], "DN-2 visible", "DN-2 invisible");
		mainButtonClick(sch1[i], sch2[i], "SCH-2 visible", "SCH-2 invisible");
		let nps3 = nps2[i].querySelectorAll("div");
		let dn3 = dn2[i].querySelectorAll("div");
		let sch3 = sch2[i].querySelectorAll("div");
		let button3 = [nps3, dn3, sch3];
		for (let j = 0; j < nps3.length; j++) {
			smallButtonClick(nps3[j], i, j, button3, 0);
			smallButtonClick(dn3[j], i, j, button3, 0);
		}
		for (let j = 0; j < sch3.length; j++) {
			smallButtonClick(sch3[j], i, j, button3, 1);
		}
	}
});

