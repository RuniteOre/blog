##I hate how to add a post to here
so my first goal is to make a button entry.

Yeah, it's probably taking me more time to make that than to just add the element yourself

I started with

	//script to add a li element to ul
	function addPost(usrinput){
	var nav = document.getElementById("main-nav");
	var li = document.createElement("li");
	var a = document.createElement("a");
	a.href = "javascript:void(0)";
	li.appendChild(a);
	nav.appendChild(li);
	//add onclick to li

And went with it, adding

	<input type="text" id="usrinput" placeholder="Add a post..."><button id="submit" onclick="addPost()">Add</button>

to the html.

Keep getting a ReferenceError:can't find variable AddPost, I don't know how to fix it at this moment, I need to keep doing research.

**Published: 8/2/2022**