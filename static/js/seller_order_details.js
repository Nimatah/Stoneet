$('#seller-accept').on('click', function (e) {
    e.preventDefault();

    const orderId = $('#order-id').text()

    $.ajax(`/api/orders/${orderId}/seller-accept`, {
        method: "GET",
        dataType: 'json',
        success: function (response) {
            location.reload()
            return false
        },
            error: function (xhr, status, error) {
            $('#error-modal .modal-body').empty()
            let response = JSON.parse(xhr.responseText)
            $('#error-modal').modal.show();
            $('#error-modal .modal-body').append(`<div>
                <span>${response.message}</span>
            </div>`)
        }
    })
})

$('#seller-reject').on('click', function (e) {
    e.preventDefault();

    const orderId = $('#order-id').text()

    $.ajax(`/api/orders/${orderId}/seller-reject`, {
        method: "GET",
        dataType: 'json',
        success: function (response) {
            location.reload()
            return false
        },
            error: function (xhr, status, error) {
            $('#error-modal .modal-body').empty()
            let response = JSON.parse(xhr.responseText)
            $('#error-modal').modal.show();
            $('#error-modal .modal-body').append(`<div>
                <span>${response.message}</span>
            </div>`)
        }
    })
})