$(document).ready( function() {
	$("#about-btn").click( function() {
        var currencyFrom = $("#c1").val();
        var currencyTo = $("#c2").val();
        var amount = $("#amount").val();
        $.getJSON('/currency/calculate',
            {currencyFrom: currencyFrom, currencyTo: currencyTo, amount: amount},
            function(data) {
            //alert(amount+" "+currencyFrom+" = "+ data['res']+" "+currencyTo)
            $("#result").val(data['res'])
            });
	});


    $("#rvw-submit").click( function(){
        var revName = $("#revName").val();
        var rating = $("#rating").val();
        var revText = $("#revText").val();
        var title = $("#revTitle").val();
        $.post( "/currency/submit_review/",
            {revName: revName, rating: rating, revText: revText, title: title},
            function(data){alert("Thanks, your review has been submitted")
            });
    });


	$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/currency/suggest_currency/', {suggestion: query}, function(data){
         $('#cats').html(data['Abc']);
        });
    });


});

/*function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
*/