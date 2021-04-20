function getLatestActiveState() {
    let highestCheckedScore = Math.max(...$('input[data-score]:checked')
        .toArray()
        .map((v) => parseInt($(v).data('score')))
    )

    return $(`input[data-score="${highestCheckedScore}"]`)
}

$('#order-qc-submit').on('click', function (e) {
    e.preventDefault()

    const state = getLatestActiveState().prop('disabled', false)
    const contract = $('#admin_qc_check_6')

    $('#qc-form-data').append(state, contract)
    $('#order-qc-form').submit()
});
