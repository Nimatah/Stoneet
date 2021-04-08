//Created by Arious

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

jQuery(function ($) {
    var path = window.location.href;
    $('.nav-item a').each(function () {
        if (this.href === path) {
            $(this).addClass('active');
        }
    });
});

jQuery(function ($) {
    var path = window.location.href;
    $('.nav-item a').each(function () {
        if (this.href === path) {
            var parent = $(this).parents('.nav-second-level')
            if (parent.length == 1) {
                $(parent).addClass('show');
            }
        }
    });
});

var $form = $('#edit-admin-list'),
    $errorMsg = $("<span class='error'>پر کردن این گزینه اجباری است</span>");

$('#ph_signup_submit_btn').on("click", function () {

    if (isEmailValid($('#email-field').val())) {
        jQuery("#email-error-field").hide();
    } else {
        jQuery("#email-error-field").show();
    }

    var toReturn = true;
    $("input,select", $form).each(function () {

        if ($(this).val() == "") {

            if (!$(this).data("error")) {
                $(this).data("error", $errorMsg.clone().insertAfter($(this)));
            }
            toReturn = false;
        } else {

            if ($(this).data("error")) {
                $(this).data("error").remove();
                $(this).removeData("error");
            }
        }
    });
    return toReturn;
});

function isEmailValid(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}


$(document).ready(function () {
    $("#mobile-number").keypress(function (e) {
        if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
            return false;
        }
    });
});

function handleYourSuggestPrice() {
    const isPersianNumber = function (keyCode) {
        return keyCode >= 1776 && keyCode <= 1785;
    }

    const isArabicNumber = function (keyCode) {
        return keyCode >= 1632 && keyCode <= 1641;
    }

    const isEnglishNumber = function (keyCode) {
        return keyCode >= 48 && keyCode <= 57;
    }

    $('#your-suggest-price').keypress(function (e) {
        if (e.which != 8 && e.which != 0 && !(isPersianNumber(e.which) || isArabicNumber(e.which) || isEnglishNumber(e.which))) {
            return false;
        } else {
            $('#your-suggest-price').val(persianToEnglish($(this).val()));
        }
    });
}

$(document).ready(function () {
    $('#your-suggest-price').keyup(function (event) {

        if (event.which >= 37 && event.which <= 40) return;

        $(this).val(function (index, value) {
            return value
                .replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ",")
                ;
        });
    });
})

function handleDateField(elementId) {
    $(elementId).pDatepicker({
        initialValue: false,
        viewMode: 'year',
        formatter: function (unixDate) {
            console.log('shit ')
            const date = new persianDate(unixDate);
            const year = pad(date.State.persian.year);
            const month = pad(date.State.persian.month + 1);
            const day = pad(date.State.persian.day);
            return `${year}-${month}-${day}`;
        },
    })
}

$(document).ready(function () {
    handleYourSuggestPrice();
    handleDateField('#ph_logistic_license_start_date');
    handleDateField('#ph_logistic_license_end_date');
});

