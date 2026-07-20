let main = document.querySelector("main");

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
main.addEventListener("mousewheel", function (e) {
	e.preventDefault();
	if (e.wheelDelta < 0) {
		scrollColumn(main, -1);
	}else if (e.wheelDelta > 0) {
		scrollColumn(main, 1);
	}
});