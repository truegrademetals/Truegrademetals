class XDrag extends Drag {
	constructor(item, ...args){
		super(item);
		this.items = [];
		this.attr = [];
		this.leftAttr = [];
		this.num = [];
		this.plus = [];
		this.rightAttr = [];
		for (let i = 0; i < args.length; i++) {
			this.items[i] = document.querySelector(args[i][0]);
			this.attr[i] = args[i][1];
			this.leftAttr[i] = args[i][2];
			this.num[i] = args[i][3];
			this.plus[i] = args[i][4];
			this.rightAttr[i] = args[i][5];
		}
	}
	fnMove(e) {
		let l = e.pageX - this.left;
		let r = this.item.parentNode.offsetWidth - this.item.offsetWidth;
		if (l < 0) {
			l = 0;
		}else if (l > r) {
			l = r;
		}else{
			this.item.style.left = l + 'px';			
		}
		if (l/r < 0.08) {
			for (let i = 0; i < this.items.length; i++) {
				this.items[i].setAttribute(this.attr[i], this.leftAttr[i]+(1250*l/r-7812.5*Math.pow(l/r, 2)+this.plus[i])+this.rightAttr[i]);
			}
		}else if (l/r > 0.8) {
			for (let i = 0; i < this.items.length; i++) {
				this.items[i].setAttribute(this.attr[i], this.leftAttr[i]+(2000*Math.pow(l/r, 2)-3200*l/r+1350+this.plus[i])+this.rightAttr[i]);
			}
		}else {
			for (let i = 0; i < this.items.length; i++) {
				this.items[i].setAttribute(this.attr[i], this.leftAttr[i]+(27.78*l/r+47.78+this.plus[i])+this.rightAttr[i]);
			}
		}
	}
	fnMoveT(e) {
		let touch = e.touches[0];
		let l = touch.pageX - this.left;
		let r = this.item.parentNode.offsetWidth - this.item.offsetWidth;
		if (l < 0) {
			l = 0;
		}else if (l > r) {
			l = r;
		}else{
			this.item.style.left = l + 'px';			
		}
		if (l/r < 0.08) {
			for (let i = 0; i < this.items.length; i++) {
				this.items[i].setAttribute(this.attr[i], this.leftAttr[i]+(1250*l/r-7812.5*Math.pow(l/r, 2)+this.plus[i])+this.rightAttr[i]);
			}
		}else if (l/r > 0.8) {
			for (let i = 0; i < this.items.length; i++) {
				this.items[i].setAttribute(this.attr[i], this.leftAttr[i]+(2000*Math.pow(l/r, 2)-3200*l/r+1350+this.plus[i])+this.rightAttr[i]);
			}
		}else {
			for (let i = 0; i < this.items.length; i++) {
				this.items[i].setAttribute(this.attr[i], this.leftAttr[i]+(27.78*l/r+47.78+this.plus[i])+this.rightAttr[i]);
			}
		}
	}
}

new XDrag(
    '#drag',
    ['.cls-1', 'points', '139.9 156.71 470.94 ', 150, 156.71, ' 801.99 156.71'],
    ['.cls-2', 'transform', 'translate(310.15 ', 150, -362.96, ') rotate(45)'],
);


