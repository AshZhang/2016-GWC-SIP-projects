function onMouseenter(elem){
	elem.parentNode.style.backgroundColor = "#A9FCFB";
	elem.width *= 1.05;
	elem.height *= 1.05;
}

function onMouseleave(elem){
	elem.parentNode.style.backgroundColor = "#D1F4FF";
	elem.width /= 1.05;
	elem.height /= 1.05;
}

function mailMouseenter(elem){
	elem.style.textDecoration = "underline";
}

function mailMouseleave(elem){
	elem.style.textDecoration = "none";
}

function mailto(){
	window.location.href = "mailto:ashley.w.zhang@gmail.com";
}

function gotoEA(){
	window.open("http://www.ea.com");
}

function gotoGWC(){
	window.open("https://girlswhocode.com/");
}