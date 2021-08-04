$('button[remove-analyze]').on('click', function (e) {
    const name = 'analyze'
    const pk = $(this).attr('pk')

    $.ajax(`/api/products/remove-image?name=${name}&pk=${pk}`, {
        method: "DELETE",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        error: function (xhr, status, error) {
            e.preventDefault();
            const response = JSON.parse(xhr.responseText)
            $('#error-modal .modal-body').empty().append(
                `<div><span class="font-weight-bold">خطا</span>: ${response.error}</div>`
            )
            $('#error-modal').modal('show');
        }
    })
})

$('button[remove-image]').on('click', function (e) {
    const name = 'image';
    const pk = $(this).attr('pk');

    $.ajax(`/api/products/remove-image?name=${name}&pk=${pk}`, {
        method: "DELETE",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        error: function (xhr, status, error) {
            e.preventDefault();
            const response = JSON.parse(xhr.responseText)
            $('#error-modal .modal-body').empty().append(
                `<div><span class="font-weight-bold">خطا</span>: ${response.error}</div>`
            )
            $('#error-modal').modal('show');
        }
    })
})

$('#t-1-c').find(`option[value=${category}]`).attr('selected', 'selected')
$('#t-1-c').trigger('change')
$('#t-2-c').find(`option[value=${subCategory}`).attr('selected', 'selected')
