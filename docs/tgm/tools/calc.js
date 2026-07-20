//初始变量
let density = 0;
let grade = "";
let product = "";
let result = 0;
let kg = "Result";
let ton = "Result";
let g = "Result";
let kg2 = "Result";
let ton2 = "Result";
let g2 = "Result";
let swit = 0;
let swit2 = 0;
let click = new Event("click");
let position = 0;
let data = "";
let batch = false;
let data2 = [];
let go1 = false;
let go2 = false;
let bookmarkOut = 0;
let ctaState = 0;

//DOM元素
let matTitle = document.querySelector("#mat-title");
let proTitle = document.querySelector("#pro-title");
let matButton = document.querySelector("#mat-button");
let proButtonOuter = document.querySelector("#pro-button");
let gradeButton = document.querySelectorAll(".grade-button");
let proButton = document.querySelectorAll(".pro-button");
let calcFormInner = document.querySelectorAll(".calc-form");
let matSelect = document.querySelector("#mat-select");
let proSelect = document.querySelector("#pro-select");
let calcForm = document.querySelector("#calc-form");
let formInput = document.querySelectorAll(".form-input");
let confirmButton = document.querySelectorAll(".confirm-button");
let resultText = document.querySelectorAll(".result-text");
let batchButton = document.querySelector(".batch-button");
let batchFrame = document.querySelector("#batch-frame");
let backButton = document.querySelector("#back-button");
let confirmButton2 = document.querySelector(".confirm-button-2");
let dataInput = document.querySelector("#data-input");
let amountInput = document.querySelector("#amount-input");
let amountAll = document.querySelector("#amount-all");
let weightOutput = document.querySelector("#weight-output");
let weightAll = document.querySelector("#weight-all");
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

//批处理格式
data2[0] = `Please input the pipe dimensions.
Outside Diameter*Thickness*Length
e.g. (Default Unit: mm)
30*2*6000
30mm*2mm*6m
30x2x6000`;
data2[1] = `Please input the round bar dimensions.
Diameter*Length
e.g. (Default Unit: mm)
30*6000
30mm*6m
30x6000`;
data2[2] = `Please input the flat bar dimensions.
Width*Thickness*length
e.g. (Default Unit: mm)
10*3*6000
10mm*3mm*6m
10x3x6000`;
data2[3] = `Please input the hex bar dimensions.
Opposite Width*Length
e.g. (Default Unit: mm)
30*6000
30mm*6m
30x6000`;
data2[4] = `Please input the square bar dimensions.
Side Width*Length
e.g. (Default Unit: mm)
30*6000
30mm*6m
30x6000`;
data2[5] = `Please input the sheet dimensions.
Thickness*Width*Length
e.g. (Default Unit: mm)
3*2000*6000
3mm*2m*6m
3x2000x6000`;
dataInput.placeholder = data2[position];
amountInput.placeholder = `Amount
e.g.(Default Unit: PC)
2
20
200`;
weightOutput.innerHTML = "Result";

//开启批处理
batchButton.addEventListener("click", function(){
	batch = true;
	batchFrame.style.opacity = 1;
	batchFrame.style.pointerEvents = "inherit";
	backButton.style.background = "transparent";
	backButton.style.color = "#333";
	batchButton.style.background = "linear-gradient(105deg, #8653ea 0%, #7053ea 20%, #535aea 40%, #5385ea 60%, #4fabde 80%, #50aadc 100%)";
	batchButton.style.color = "#fff";
	for (let i = 0; i < calcFormInner.length; i++) {
		calcFormInner[i].style.opacity = 0;
		calcFormInner[i].style.pointerEvents = "none";
	}
});

//结束批处理
backButton.addEventListener("click", function(){
	batch = false;
	batchFrame.style.opacity = 0;
	batchFrame.style.pointerEvents = "none";
	calcFormInner[position].style.opacity = 1;
	calcFormInner[position].style.pointerEvents = "inherit";
	batchButton.style.background = "transparent";
	batchButton.style.color = "#333";
	backButton.style.background = "linear-gradient(105deg, #8653ea 0%, #7053ea 20%, #535aea 40%, #5385ea 60%, #4fabde 80%, #50aadc 100%)";
	backButton.style.color = "#fff";
});


//选定材质
for (let i = 0; i < gradeButton.length; i++) {
	gradeButton[i].addEventListener("click", function(){
		html.scrollTop = 0;
		density = parseFloat(this.querySelector(".grade-density").innerHTML);
		grade = this.querySelector(".grade-name").innerHTML;
		matSelect.style.opacity = 0;
		matSelect.style.pointerEvents = "none";
		matTitle.innerHTML = grade;
		if (product == "") {
			proSelect.style.opacity = 1;
			proSelect.style.pointerEvents = "inherit";
		}else{
			calcForm.style.opacity = 1;
			calcForm.style.pointerEvents = "inherit";			
		}
		amountAll.innerHTML = "Result";
		weightOutput.innerHTML = "Result";
		weightAll.innerHTML = "Result";
		resultText[0].innerHTML = "Result";
		resultText[1].innerHTML = "Result";
	});
}

//选定产品
for (let i = 0; i < proButton.length; i++) {
	proButton[i].addEventListener("click", function(){
		html.scrollTop = 0;
		kg = "Result";
		ton = "Result";
		g = "Result";
		for(let j = 0; j < resultText.length; j++) {
			resultText[j].innerHTML = "Result";
		}
		product = this.querySelector(".pro-name").innerHTML;
		proSelect.style.opacity = 0;
		proSelect.style.pointerEvents = "none";
		calcForm.style.opacity = 1;
		calcForm.style.pointerEvents = "inherit";
		proTitle.innerHTML = product;
		for (let j = 0; j < calcFormInner.length; j++) {
			calcFormInner[j].style.opacity = 0;
			calcFormInner[j].style.pointerEvents = "none";
		}
		if (batch == false) {
			calcFormInner[i].style.opacity = 1;
			calcFormInner[i].style.pointerEvents = "inherit";			
		}
		position = i;
		dataInput.placeholder = data2[position];
		amountAll.innerHTML = "Result";
		weightOutput.innerHTML = "Result";
		weightAll.innerHTML = "Result";
		resultText[0].innerHTML = "Result";
		resultText[1].innerHTML = "Result";
		console.log(position);
	});
}


//选择材质
matButton.addEventListener("click", function(){
	matSelect.style.opacity = 1;
	matSelect.style.pointerEvents = "inherit";
	proSelect.style.opacity = 0;
	proSelect.style.pointerEvents = "none";
	calcForm.style.opacity = 0;
	calcForm.style.pointerEvents = "none";
});

//选择产品
proButtonOuter.addEventListener("click", function(){
	if (density != 0) {
		matSelect.style.opacity = 0;
		matSelect.style.pointerEvents = "none";
		proSelect.style.opacity = 1;
		proSelect.style.pointerEvents = "inherit";
		calcForm.style.opacity = 0;
		calcForm.style.pointerEvents = "none";
	}		
});



//计算函数
function calc(mode, inputInner, pError){
	let err = true;
	if (mode == 0) {
		let oD = parseFloat(inputInner[0]);
		let wT = parseFloat(inputInner[1]);
		let l = parseFloat(inputInner[2]);
		let amount = parseFloat(inputInner[3]);
		if(oD > 3000 || oD < 0.4){
			pError.innerHTML = "The outer diameter must between 0.4mm and 3000mm!";
		}else if(wT > 400 || wT < 0.05){
			pError.innerHTML = "The wall thickness must between 0.05mm and 400mm!";
		}else if(wT >= oD/2){
			pError.innerHTML = "The wall thickness is incorrect!";
		}else{
			result = (oD - wT)*wT*l*density*amount*(Math.PI)/1000;
			err = false;
		}
	}else if(mode == 1){
		let d = parseFloat(inputInner[0]);
		let l = parseFloat(inputInner[1]);
		let amount = parseFloat(inputInner[2]);
		if(d > 2500 || d < 0.02){
			pError.innerHTML = "The diameter must between 0.02mm and 2500mm!";
		}else{
			result = d*d*l*density*amount*(Math.PI)/4000;
			err = false;
		}
	}else if(mode == 2){
		let w = parseFloat(inputInner[0]);
		let t = parseFloat(inputInner[1]);
		let l = parseFloat(inputInner[2]);
		let amount = parseFloat(inputInner[3]);
		if(t > 200 || t < 0.5){
			pError.innerHTML = "The thickness must between 0.5mm and 200mm!";
		}else if(w > 250 || w < 1.5){
			pError.innerHTML = "The width must between 1.5mm and 250mm!";
		}else{
			result = w*t*l*density*amount/1000;	
			err = false;
		}
	}else if(mode == 3){
		let d = parseFloat(inputInner[0]);
		let l = parseFloat(inputInner[1]);
		let amount = parseFloat(inputInner[2]);
		if(d > 180 || d < 3){
			pError.innerHTML = "The opposite side must between 3mm and 180mm!";
		}else{
			result = d*d*l*density*amount*(Math.sqrt(3))/2000;
			err = false;
		}		
	}else if(mode == 4){
		let w = parseFloat(inputInner[0]);
		let l = parseFloat(inputInner[1]);
		let amount = parseFloat(inputInner[2]);
		if(w > 200 || w < 2){
			pError.innerHTML = "The side width must between 2mm and 200mm!";
		}else{
			result = w*w*l*density*amount/1000;
			err = false;
		}
	}else if(mode == 5){
		let t = parseFloat(inputInner[0]);
		let w = parseFloat(inputInner[1]);
		let l = parseFloat(inputInner[2]);
		let amount = parseFloat(inputInner[3]);
		if(t > 500 || t < 0){
			pError.innerHTML = "The thickness must between 0mm and 500mm!";
		}else if(w > 3000 || w < 0){
			pError.innerHTML = "The width must between 0m and 3m!";
		}else{
			result = w*t*l*density*amount/1000000;
			err = false;
		}	
	}
	if (err) {
		return ["Result", "Result", "Result"];
	}else if(result > 99999999){
		pError.innerHTML = "The number is too large";
		return ["Error", "Error", "Error"];
	}else{
		let resultTon = result/1000;
		let resultG = result*1000;
		result = result.toFixed(2);
		resultTon = resultTon.toFixed(2);
		resultG = resultG.toFixed(2);
		return [result, resultTon, resultG];	
	}
}

//计算主体
for (let i = 0; i < 6; i++) {
	confirmButton[i].addEventListener("click", function(){
		go1 = true;
		let inputInnerOut = calcFormInner[i].querySelectorAll(".form-input");
		let inputInner = [];
		for (let j = 0; j < inputInnerOut.length; j++) {
			inputInner[j] = inputInnerOut[j].value;
		}
		let pError = calcFormInner[i].querySelector("p");
		let resultText = calcFormInner[i].querySelectorAll(".result-text");
		let mode = 1;
		//错误保护
		for (let j = 0; j < inputInner.length; j++) {
			if (isNaN(parseFloat(inputInner[j])) || inputInner[j] == "") {
				mode = 0;
			}
		}
		//计算事件
		if (mode == 0) {
			pError.innerHTML = "Please input the data!";
		} else {
			pError.innerHTML = "&emsp;";
			kg = calc(i, inputInner, pError)[0];
			ton = calc(i, inputInner, pError)[1];
			g = calc(i, inputInner, pError)[2];
			resultText[0].innerHTML = kg;
			resultText[1].innerHTML = swit?g:ton;
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
}
confirmButton2.addEventListener("click", function(){
	go2 = true;
	let column = dataInput.value.split(/[\n\r]/);
	let inputInner = [];
	let inputAmount = amountInput.value.split(/[\n\r]/);
	for (let i = 0; i < column.length; i++) {
		if (inputAmount.length > column.length) {
			column.push("");
		} else if (inputAmount.length < column.length) {
			inputAmount.push("");
		}
		inputInner[i] = column[i].split(/[*x×]/);
		inputInner[i].push(inputAmount[i]);
		for (let j = 0; j < inputInner[i].length; j++) {
			if (inputInner[i][j].indexOf("mm") != -1) {
				inputInner[i][j] = inputInner[i][j].replace("mm", "");
			} else if (inputInner[i][j].indexOf("cm") != -1) {
				inputInner[i][j] = parseFloat(inputInner[i][j].replace("cm", ""))*10;
			} else if (inputInner[i][j].indexOf("dm") != -1) {
				inputInner[i][j] = parseFloat(inputInner[i][j].replace("dm", ""))*100;
			} else if (inputInner[i][j].indexOf("m") != -1) {
				inputInner[i][j] = parseFloat(inputInner[i][j].replace("m", ""))*1000;
			}
			
		}
	}
	for (let i = inputInner.length - 1; i >= 0; i--) {
		if (inputInner[i].toString() == ",") {
			inputInner.splice(i, 1);
		}
	}
	let pError = batchFrame.querySelector("p");
	let mode = 1;
	//错误保护
	for (let j = 0; j < inputInner.length; j++) {
		if (
			(
				(position == 0 || position == 2 || position == 5) && 
				((inputInner[j].length != 4) ||
				(parseFloat(inputInner[j][0]) != inputInner[j][0] || parseFloat(inputInner[j][1]) != inputInner[j][1] || parseFloat(inputInner[j][2]) != inputInner[j][2] || parseFloat(inputInner[j][3]) != inputInner[j][3]))
			)
			||
			(			
				(position == 1 || position == 3 || position == 4) && 
				((inputInner[j].length != 3) ||
				(parseFloat(inputInner[j][0]) != inputInner[j][0] || parseFloat(inputInner[j][1]) != inputInner[j][1] || parseFloat(inputInner[j][2]) != inputInner[j][2]))
			)
		) {
			mode = 0;
		}
	}
	//计算事件
	if (mode == 0) {
		pError.innerHTML = "Please input the right data!";
		weightOutput.innerHTML = "Result";
		weightAll.innerHTML = "Result";
		amountAll.innerHTML = "Result";
	} else {
		pError.innerHTML = "&emsp;";
		kg2 = ""
		ton2 = ""
		g2 = ""
		let sumAmount = 0;
		let sumWeight = [0, 0, 0];
		let th = 1000;
		if (position == 5) {
			th = 1;
		}
		for (let i = 0; i < inputInner.length; i++) {
			kg2 = kg2 + parseFloat(calc(position, inputInner[i], pError)[0]/th).toFixed(2) + "<br>";
			ton2 = ton2 + parseFloat(calc(position, inputInner[i], pError)[1]/th).toFixed(2) + "<br>";
			g2 = g2 + parseFloat(calc(position, inputInner[i], pError)[2]/th).toFixed(2) + "<br>";
			sumWeight[0] += parseFloat((calc(position, inputInner[i], pError)[0]/th));
			sumWeight[1] += parseFloat((calc(position, inputInner[i], pError)[1]/th));
			sumWeight[2] += parseFloat((calc(position, inputInner[i], pError)[2]/th));
			sumAmount += parseInt(inputInner[i][inputInner[i].length - 1]);
		}
		if (swit2 == 0) {
			weightOutput.innerHTML = kg2;
			weightAll.innerHTML = sumWeight[0].toFixed(2);			
		} else if (swit2 == 1){
			weightOutput.innerHTML = ton2;
			weightAll.innerHTML = sumWeight[1].toFixed(2);				
		} else if (swit2 == 2){
			weightOutput.innerHTML = g2;
			weightAll.innerHTML = sumWeight[2].toFixed(2);				
		}
		amountAll.innerHTML = sumAmount;
	}
});

//切换单位
let resultTag = document.querySelectorAll(".result-ton");
for (let i = 0; i < resultTag.length; i++) {
	resultTag[i].querySelector('.switch').addEventListener("click", function(){
		let resultText = calcFormInner[i].querySelectorAll(".result-text");
		swit = swit?0:1;
		for (let j = 0; j < resultTag.length; j++){			
			resultTag[j].querySelector(".result-unit").innerHTML = swit?"g":"t";
		}
		resultText[1].innerHTML = swit?g:ton;
	});
}
let unitSwitch = document.querySelector("#unit-switch");
unitSwitch.addEventListener("click", function(){
	let wUnit = ["kg", "t", "g"]
	swit2 = swit2?((swit2 == 1)?2:0):1;
	unitSwitch.innerHTML = wUnit[swit2];
	confirmButton2.dispatchEvent(click);
});

//回车计算
document.addEventListener("keydown", function(e){
	if (e.keyCode == 13) {
		confirmButton[position].dispatchEvent(click);
	}
});

