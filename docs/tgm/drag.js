class Drag {
	constructor(query){
		let self = this;
		this.item = document.querySelector(query);
		this.item.addEventListener("mousedown", function(e) {
			self.fnDown(e);
			return false;
		});	
		this.item.addEventListener("touchstart", function(e) {
			self.fnStart(e);
			return false;
		});	
	}
	fnDown(e) {
		let self = this;
		this.left = e.pageX - this.item.offsetLeft;
		this.top = e.pageY - this.item.offsetTop;
		document.onmousemove = function(e){
			self.fnMove(e);
		}	
		document.onmouseup = function(){
			self.fnUp();
		}
	}
	fnStart(e) {
		let self = this;
		let touch = e.touches[0];
		this.left = touch.pageX - this.item.offsetLeft;
		this.top = touch.pageY - this.item.offsetTop;
		document.addEventListener("touchmove", function(e) {
			self.fnMoveT(e);
		});	
		document.addEventListener("touchend", function(e) {
			self.fnEnd();
		});	
	}
	fnMove(e) {
		this.item.style.left = e.pageX - this.left + 'px';	
		this.item.style.top = e.pageY - this.top + 'px';
	}
	fnUp (e) {
		document.onmousemove = null;	
		document.onmouseup = null;	
	}
	fnMoveT(e) {
		let touch = e.touches[0];
		this.item.style.left = touch.pageX - this.left + 'px';	
		this.item.style.top = touch.pageY - this.top + 'px';
	}
	fnEnd (e) {
		document.addEventListener("touchmove", null);	
		document.addEventListener("touchend", null);	
	}
}