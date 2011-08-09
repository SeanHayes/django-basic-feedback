var feedbackToggle;

(function($){

feedbackToggle = function(){
	$('#feedback_tab, #feedback_panel').toggle();
}

$(document).ready(function(){
	$('#feedback_tab button, #feedback_panel button').click(feedbackToggle);
	
	$('#feedback_form').submit(function(e){
		e.preventDefault();
		var action = this.action;
		//TODO: disable submit button until submit succeeds
		$.ajax(action, {
			'type': 'POST',
			'data': $(this).serialize(),
			'success': function(data, textStatus, jqXHR){
				alert("Your feedback has been successfully submitted, thank you.");
				$("#feedback_panel form textarea").val("");
				feedbackToggle();
			},
			'error': function(jqXHR, textStatus, errorThrown){
				if (jqXHR.status == 400)
				{
					var errors = "The following field error(s) ocurred: \n";
					errors += jqXHR.responseText;
					alert(errors);
				}
				else if(jqXHR.responseText != ''){
					alert("The following error ocurred: \n"+jqXHR.responseText);
				}
				else{
					alert('An unknown error occurred.');
				}
			}
		});
	});
});

})(jQuery);
