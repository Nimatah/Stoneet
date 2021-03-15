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

function handleOrderWeight(){
    $('#order-weight').on('change', function (e){
        let persianNumbers = [/۰/g, /۱/g, /۲/g, /۳/g, /۴/g, /۵/g, /۶/g, /۷/g, /۸/g, /۹/g],
            arabicNumbers = [/٠/g, /١/g, /٢/g, /٣/g, /٤/g, /٥/g, /٦/g, /٧/g, /٨/g, /٩/g],
            fixNumbers = function (str) {
                if (typeof str === 'string') {
                    for (let i = 0; i < 10; i++) {
                        str = str.replace(persianNumbers[i], i).replace(arabicNumbers[i], i);
                    }
                }
                return str;
            };
    })
    $(document).ready(function () {
  $('#order-weight').keypress(function (e) {
     //if the letter is not digit then display error and don't type anything
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        //display error message
        $("#errmsg").html("Digits Only").show().fadeOut("slow");
               return false;
    }
   });
});
}

handleAddressDetails();