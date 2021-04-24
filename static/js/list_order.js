$('[id^=reject-]').on('click', function (e) {
    e.preventDefault();

    const rejectReason = $(this).data('reject-reason')

    $('#bell-modal .modal-body').empty().append(`<span>${rejectReason}</span>`)
    $('#bell-modal').modal.show()
});
