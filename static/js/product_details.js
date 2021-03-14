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


handleAddressDetails();