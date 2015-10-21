$(document).ready( function() {
	    $("#compare").click( function(){
        var currencyFrom = $("#c1").val();
        var currencyTo = $("#c2").val();
        var amount = $("#amount").val();
        $.getJSON('/currency/comparefx',
            {currencyFrom: currencyFrom, currencyTo: currencyTo, amount: amount},
            function(data) {
            //alert(amount+" "+currencyFrom+" = "+ data['res']+" "+currencyTo)
            $("#result").val(data['res'])
            });
    });
});