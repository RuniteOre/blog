//script to add a li element to ul
function addPost(usrinput){
	var nav = document.getElementById("main-nav");
	var li = document.createElement("li");
	var a = document.createElement("a");
	a.href = "javascript:void(0)";
	li.appendChild(a);
	nav.appendChild(li);
	//add onclick to li
