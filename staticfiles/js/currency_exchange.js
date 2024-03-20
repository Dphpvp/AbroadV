document.addEventListener("DOMContentLoaded", function () {
    function convertCurrency() {
        const fromCurrency = document.getElementById("fromCurrency").value;
        const toCurrency = document.getElementById("toCurrency").value;
        const amount = document.getElementById("amountInput").value;

        // Make an AJAX request to your Django view
        $.ajax({
            type: 'GET',
            url: `/currency_exchange/?from_currency=${fromCurrency}&to_currency=${toCurrency}&amount=${amount}`,
            success: function (response) {
                document.getElementById("exchangeRate").innerText = `Exchange Rate: 1 ${fromCurrency} = ${response.exchange_rate} ${toCurrency}`;
                document.getElementById("convertedAmount").innerText = `Converted Amount: ${response.converted_amount} ${toCurrency}`;
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    }

    document.getElementById("convertButton").addEventListener("click", convertCurrency);
});
