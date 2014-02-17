$("body").on("click", ".video", function(event){
	event.preventDefault();
	var clickedButton = $(event.target);
	this.append("<img></img>");
});
