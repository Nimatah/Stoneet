$('button[remove-image]').on('click', function (e) {
    const name = 'analyze'
    const pk = $(this).attr('pk')

    $.ajax(`/api/users/remove-image?pk=${pk}`, {
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
