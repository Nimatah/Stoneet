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

$(document).ready(function () {
    $("#your-suggest-price").keypress(function (e) {
        if (e.which != 0 && e.which != 0 && (e.which < 48 || e.which > 57)) {
            return false;
        }
    });
});

/*$('#your-suggest-price').keyup(function(event) {

  if(event.which >= 37 && event.which <= 40){
   event.preventDefault();
  }

  $(this).val(function(index, value) {
      value = value.replace(/,/g,'');
      return numberWithCommas(value);
  });
});

function numberWithCommas(x) {
    var parts = x.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    let s = parts.join(".");
}*/

/*document.querySelectorAll('#your-suggest-price')[0].addEventListener('input', onInput_Arabic);
document.querySelectorAll('#your-suggest-price')[1].addEventListener('input', onInput_normal);

function onInput_normal(){
   var v = +(this.value.replace(/[,|\.|\D]/g,''));
   this.value =  this.value ? v.toLocaleString() : '';
}

function onInput_Arabic(){
   var v = transformNumbers.toEnglish( this.value );
   this.value =  this.value ? (+v).toLocaleString('ar-EG') : '';
}

var transformNumbers = (function(){
    var numerals = {
        persian : ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"],
        arabic  : ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"]
    };

    function fromEnglish(str, lang){
        var i, len = str.length, result = "";

        for( i = 0; i < len; i++ )
            result += numerals[lang][str[i]];

        return result;
    }

    return {
        toEnglish : function(str){
            var num, i, len = str.length, result = "";

            for( i = 0; i < len; i++ ){
                num = numerals["persian"].indexOf(str[i]);
                num = num != -1 ? num : numerals["arabic"].indexOf(str[i]);
                if( num == -1 ) continue
                result += num;
            }

            return result;
        },

        toPersian : function(str, lang){
            return fromEnglish(str, "persian");
        },

        toArabic : function(str){
            return fromEnglish(str, "arabic");
        }
    }
})();*/
