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
    const contract = $('input#et_pb_contact_brand_file_request_0')

    $('#qc-form-data').append(state, contract)
    $('#order-qc-form').submit()
});

$(document).ready(function() {

    $('.image-popup-vertical-fit').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        mainClass: 'mfp-img-mobile',
        image: {
            verticalFit: true
        }

    });

    $('.image-popup-fit-width').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        image: {
            verticalFit: false
        }
    });

    $('.image-popup-no-margins').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        closeBtnInside: false,
        fixedContentPos: true,
        mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
        image: {
            verticalFit: true
        },
        zoom: {
            enabled: true,
            duration: 300 // don't foget to change the duration also in CSS
        }
    });

});