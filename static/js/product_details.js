function handleAddressDetails() {
    $('#customer-address').on('change', function(e) {
        $.ajax(`/api/address/${$(this.data('attr-id'))}`, {
            method: 'GET',
            success: function (response) {
                console.log(response);
            }
        })
    })
}

handleAddressDetails();