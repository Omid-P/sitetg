$(document).ready( function() {
	$("#about-btn").click( function() {
        var currencyFrom = $("#c1").val();
        var currencyTo = $("#c2").val();
        var amount = $("#amount").val();
        $.getJSON('/currency/calculate', {currencyFrom: currencyFrom, currencyTo: currencyTo, amount: amount}, function(data) {
            //alert(amount+" "+currencyFrom+" = "+ data['res']+" "+currencyTo)
            $("#result").val(data['res'])
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
