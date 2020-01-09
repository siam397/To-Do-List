$("body").on("click","span",function(){
	$(this).parent().fadeOut("medium",function(){
		$(this).remove( );
	})
})
$("body").on("keypress","input",function(event){
	if(event.which===13)
	{
		var str=$(this).val()
		$(this).val("")
		$("ul").append("<li><span><i class='far fa-trash-alt'></i></span>"+str+"</li>")
	}
})
$("i").on("click",function(){
	$("input").fadeToggle("slow")
})
