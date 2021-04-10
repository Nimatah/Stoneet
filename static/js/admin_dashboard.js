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


$('#seller-submit').on('click', function (e) {
    let hasValue;
    const values = $('#seller-id,#seller-name,#seller-mobile-number').toArray().map(function (el) {
        if ($(el).val() != '') {
            hasValue = true
        }
    })

    if (!hasValue) {
        $('#seller-error').show();
    } else {
        $('#seller-error').hide();
        const queryParams = $('#seller-id,#seller-name,#seller-mobile-number')
            .toArray()
            .reduce(function (acc, cur) {
            const element = $(cur)
            if (element.val() !== '') {
                acc[element.prop('name')] = element.val()
            }
            return acc
        }, {});
        $.ajax('/api/users/',{
            data: queryParams,
            method: "GET",
            success: function (response) {
                $('#seller-table').show()
                $('#seller-table-body').empty()
                response.forEach(function (seller) {
                    $('#seller-table-body').append(`
                    <tr>
                        <td>${seller.id}</td>
                        <td>${seller.full_name}</td>
                        <td>${seller.email}</td>
                        <td>${seller.mobile_number}</td>
                        <td>${seller.region}</td>
                        <td>${seller.state}</td>
                        <td>
                            <a href="/users/panel/admin-add-product/?seller=${seller.id}"
                               class="ph-btn ph-managements-btn qc"><i
                                    class="fas fa-mouse-pointer"></i>انتخاب</a>
                        </td>
                    </tr>
                    `)
                })
            },
        })
    }
})

/*$(document).ready(function () {
  $("#seller-mobile-number").keypress(function (e) {
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
               return false;
    }
   });
});*/

function handleSellerMobileNumber() {
    const isPersianNumber = function (keyCode) {
        return keyCode >= 1776 && keyCode <= 1785;
    }

    const isArabicNumber = function (keyCode) {
        return keyCode >= 1632 && keyCode <= 1641;
    }

    const isEnglishNumber = function (keyCode) {
        return keyCode >= 48 && keyCode <= 57;
    }

    $('#seller-mobile-number').keypress(function (e) {
        if (e.which != 8 && e.which != 0 && !(isPersianNumber(e.which) || isArabicNumber(e.which) || isEnglishNumber(e.which))) {
            return false;
        } else {
            $('#seller-mobile-number').val(persianToEnglish($(this).val()));
        }
    });
}

$(document).ready(function (){
    handleSellerMobileNumber();
})