(function($) {
    "use strict";
		  $("#defualt" ).on('click',function(){
			  $("#color" ).attr("href", "css/colors/defualt.css");
			  return false;
		  });
		  
		 
		  $("#red" ).on('click',function(){
			  $("#color" ).attr("href", "css/colors/red.css");
			  return false;
		  });
		  
		   $("#green" ).on('click',function(){
			
			  $("#color" ).attr("href", "css/colors/green.css");
			  return false;
		  });
		  
		  
		  $("#purple" ).on('click',function(){
			  $("#color" ).attr("href", "css/colors/purple.css");
			  return false;
		  });
		  
		  $("#yellow" ).on('click',function(){
			  $("#color" ).attr("href", "css/colors/yellow.css");
			  return false;
		  });
		  
		  $("#cyan" ).on('click',function(){
			  $("#color" ).attr("href", "css/colors/cyan.css");
			  return false;
		  });
		  
		  $("#coraltree" ).on('click',function(){
			  $("#color" ).attr("href", "css/colors/coraltree.css");
			  return false;
		  });
		  
		  $("#orange" ).on('click',function(){
			  $("#color" ).attr("href", "css/colors/orange.css");
			  return false;
		  });
		  
	
		  // picker buttton
		  $(".picker_close").click(function(){
			  	$("#choose_color").toggleClass("position");
			  
		   });
		  
})(jQuery);