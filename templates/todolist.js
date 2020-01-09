$("span").on("click",function(){
	$(this).parent().fadeOut(2000,function(){
		$(this).remove();
	})
})


$("i").on("click",function(){
	$("input").fadeToggle("slow")
})
