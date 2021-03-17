function handleAddressDetails() {
    $.ajax(`/api/address/${$('#customer-address option:selected').val()}`, {
        method: 'GET',
        success: function (response) {
            $('#address-address').text(response.address)
            $('#address-postal-code').text(response.postal_code)
            $('#address-province').text(response.province)
            $('#address-region').text(response.region)
        }
    })
    $('#customer-address').on('change', function (e) {
        $.ajax(`/api/address/${$('#customer-address option:selected').val()}`, {
            method: 'GET',
            success: function (response) {
                $('#address-address').text(response.address)
                $('#address-postal-code').text(response.postal_code)
                $('#address-province').text(response.province)
                $('#address-region').text(response.region)
            }
        })
    })
}

//Enter Arious

function handleOrderWeightInput() {

    const isPersianNumber = function (keyCode) {
        return keyCode >= 1776 && keyCode <= 1785;
    }

    const isArabicNumber = function (keyCode) {
        return keyCode >= 1632 && keyCode <= 1641;
    }

    const isEnglishNumber = function (keyCode) {
        return keyCode >= 48 && keyCode <= 57;
    }

    $('#order-weight').keypress(function (e) {

        if (e.which != 8 && e.which != 0 && !(isPersianNumber(e.which) || isArabicNumber(e.which) || isEnglishNumber(e.which))) {
            return false;
        }
    });
    $(function () {
        $('#order-weight').keypress(function (e) {
            var ctrlKey = 67, vKey = 86;
            if (e.keyCode != ctrlKey && e.keyCode != vKey) {
                $('#order-weight').val(persianToEnglish($(this).val()));
            }
        });
    });

    function persianToEnglish(input) {
        var inputstring = input;
        var persian = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]
        var english = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        var arabic = ["۰", "۱", "۲", "۳", "٤", "۵", "٦", "۷", "۸", "۹"]
        for (var i = 0; i < 10; i++) {
            var regex = new RegExp(`[${persian[i]}${arabic[i]}]`, 'g');
            inputstring = inputstring.toString().replace(regex, english[i]);
        }
        return inputstring;
    }
}


function addCommas(x) {
    var parts = x.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return parts.join(",");
}

function handleFinalPrice() {

    $('#order-weight').keyup(function () {
        var rate = parseFloat($('#order-weight').val()) || 0;
        var box = parseFloat($('#base-product-price').text()) || 0;

        $('#final-price').text(rate * box);
        var x = $('#final-price').text();
        $('#final-price').text(addCommas(x));
    });
}


var $form = $("#details-form"),
    $errorMsg = $("<span class='error'>پر کردن این گزینه اجباری است</span>");

$("#submit").on("click", function () {

    var toReturn = true;
    $("input,select", $form).each(function () {

        if ($(this).val() == "") {

            if (!$(this).data("error")) {
                $(this).data("error", $errorMsg.clone().insertAfter($(this)));
            }
            toReturn = false;
        }

        else {

            if ($(this).data("error")) {
                $(this).data("error").remove();
                $(this).removeData("error");
            }
        }
    });
    return toReturn;
});

var maxLength = 14;
$('#order-weight').keyup(function() {
  var textlen = maxLength - $(this).val().length;
  $('#rchars').text(textlen);
});

handleFinalPrice();
handleOrderWeightInput();
handleAddressDetails();