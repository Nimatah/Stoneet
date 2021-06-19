$('#product_accept').on('click', function (e) {
   e.preventDefault();
   let $acceptButton = $(this)

   $.ajax($acceptButton.prop('href'), {
       method: 'GET',
       data: {
           reason: $('#reject-reason').val()
       },
       success: function (resp) {
           window.location.href = $acceptButton.attr('redirect')
       },
       error: function (xhr, status, error) {
            e.preventDefault();
            $('#error-modal .modal-body').empty()
            let response = JSON.parse(xhr.responseText)
             $('#error-modal .modal-body').append(
                    `<div><span class="font-weight-bold">خطا</span>: ${response.error}</div>`
                )
            $('#error-modal').modal('show');
       }
   })
});

$('#product_reject').on('click', function (e) {
    e.preventDefault();
    let $rejectButton = $(this)

    $.ajax($rejectButton.prop('href'), {
       method: 'GET',
       data: {
           reason: $('#reject-reason').val()
       },
       success: function (resp) {
           window.location.href = $rejectButton.attr('redirect')
       },
       error: function (xhr, status, error) {
            e.preventDefault();
            $('#error-modal .modal-body').empty()
            let response = JSON.parse(xhr.responseText)
             $('#error-modal .modal-body').append(
                    `<div><span class="font-weight-bold">خطا</span>: ${response.error}</div>`
                )
            $('#error-modal').modal('show');
       }
    })
});