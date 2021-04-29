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


$('.btn').click(function (event) {
    event.preventDefault();
    var target = $(this).data('target');
    $('#click-alert').html('data-target= ' + target).fadeIn(50).delay(3000).fadeOut(1000);

});


// Multi-Step Form
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the crurrent tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "مرحله بعدی";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    //if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("ph_new_login_form").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}


$(document).ready(function () {
    $(".ph-conditional").change(function () {
        var selected = $(".ph-conditional .custom-control-input:checked").data('tab');
        $('.ph-conditional-wrapper').hide();
        $('.ph-conditional-wrapper-2').hide();
        $('#' + selected).show();
        $('#' + selected + -2).show();

    });
    $('.ph-conditional-wrapper').hide();
    $('.ph-conditional-wrapper-2').hide();
});


// Enter Tajious

function pad(d) {
    return (d < 10) ? '0' + d.toString() : d.toString();
}

function handleValidateUser() {
    $('#ph_signup_submit_btn').on('click', function (e) {
        const body = {
            email: $('#sign_up_email').val(),
            password: $('#sign_up_password').val(),
            mobile_number: $('#sign_up_number').val(),
        }
        $.ajax("/api/validate/registration/auth", {
            method: "POST",
            async: false,
            contentType: "application/json",
            headers: {
                'Accept-Language': 'fa',
            },
            data: JSON.stringify(body),
            success: function (){
                //enter arious
                nextPrev(1);
            },
            error: function (xhr, status, error) {
                e.preventDefault();
                $('#error-modal .modal-body').empty()
                let response = JSON.parse(xhr.responseText)
                let errors = [];
                for (let k in response) {
                    errors.push({
                        title: k,
                        value: response[k]
                    })
                }
                errors.forEach(function (v, i) {
                    $('#error-modal .modal-body').append(
                        `<div><span class="font-weight-bold">${v.title}</span>: ${v.value}</div>`
                    )
                })
                $('#error-modal').modal('show');
            }
        })
    })
}

function handleRegions(legal) {
    const regions = JSON.parse($('#regions').text());

    regions.forEach(function (region) {
        $(`#${legal}-provinces`).append(`<option value="${region.id}">${region.title}</option>`);
    });

    $(`#${legal}-provinces`).change(function () {
        $(this).find("[value='default']").remove();
        $(`#${legal}-cities`).empty();
        const provinceId = $(this).val();
        const province = regions.find(function (category) {
            return category.id.toString() === provinceId;
        });
        province.children.forEach(function (child) {
            $(`#${legal}-cities`).append(`<option value="${child.id}">${child.title}</option>`);
        })
    });
}

function handleSubmitForm() {
    $('#register-btn').on('click', function (e) {
        if (!$('#terms_conditions').prop('checked')) {
            $('#error-modal .modal-body').empty().append(`
                <div>
                    <span class="font-weight-bold">شرایط و قوانین</span>: برای ثبت نام تیک شرایط و قوانین رو بزنید
                </div>
            `);
            $('#error-modal').modal('show')
            return
        }

        const inputElements = function (type) {
            return $(`[data-type="${type}"]`).toArray().map(function (element) {
                return $(element)
            })
        }
        const legalType = $('#legal-individual').prop('checked') ? 'individual' : 'legal'

        const form = $(`<form method="post" enctype="multipart/form-data" action="${window.location}"/>`)
            .append($('[name="csrfmiddlewaretoken"]'),
                $('#sign_up_email'), $('#sign_up_password'), $('#sign_up_number'),
                $('#legal-individual'), $('#legal-legal'), ...inputElements(legalType))
        $(document.body).append(form);
        form.submit();
    })
}

function handleBirthday() {
    $(document).ready(function () {
        try {
            $('#birthday').pDatepicker({
                initialValue: false,
                viewMode: 'year',
                formatter: function (unixDate) {
                    const date = new persianDate(unixDate);
                    const year = pad(date.State.persian.year);
                    const month = pad(date.State.persian.month + 1);
                    const day = pad(date.State.persian.day);
                    return `${year}-${month}-${day}`;
                },
            })
        } catch (e) {
            console.log(e);
        }
    });
}

function handleSignupNumber() {
    const isPersianNumber = function (keyCode) {
        return keyCode >= 1776 && keyCode <= 1785;
    }

    const isArabicNumber = function (keyCode) {
        return keyCode >= 1632 && keyCode <= 1641;
    }

    const isEnglishNumber = function (keyCode) {
        return keyCode >= 48 && keyCode <= 57;
    }

    $('#sign_up_number').keypress(function (e) {
        if (e.which != 8 && e.which != 0 && !(isPersianNumber(e.which) || isArabicNumber(e.which) || isEnglishNumber(e.which))) {
            return false;
        } else {
            $('#sign_up_number').val(persianToEnglish($(this).val()));
        }
    });
}

handleValidateUser();
handleRegions('company');
handleRegions('individual');
handleSubmitForm();
handleBirthday();
$(document).ready(function () {
    handleSignupNumber();
})
