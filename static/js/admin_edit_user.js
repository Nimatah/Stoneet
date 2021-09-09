$(document).ready(function () {

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

$(document).ready(function () {
    $('.popup-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'در حال بارگداری #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',

        }
    });
});

function pad(d) {
    return (d < 10) ? '0' + d.toString() : d.toString();
}

function handleRegions(legal) {
    const regions = JSON.parse($('#regions').text());

    regions.forEach(function (region) {
        $(`#${legal}-provinces`).append(`<option value="${region.id}">${region.title}</option>`);
    });

    $(`#${legal}-provinces`).change(function () {
        $(this).find("[value='default']").remove();
        $(`#${legal}-cities`).empty();
        const provinceId = $(this).val();
        const province = regions.find(function (category) {
            return category.id.toString() === provinceId;
        });
        province.children.forEach(function (child) {
            $(`#${legal}-cities`).append(`<option value="${child.id}">${child.title}</option>`);
        })
    });
}

function handlePersianDatePicker(id) {
    $(document).ready(function () {
        try {
            $(id).pDatepicker({
                initialValue: false,
                viewMode: 'year',
                formatter: function (unixDate) {
                    const date = new persianDate(unixDate);
                    const year = pad(date.State.persian.year);
                    const month = pad(date.State.persian.month + 1);
                    const day = pad(date.State.persian.day);
                    return `${year}-${month}-${day}`;
                },
            })
        } catch (e) {
            console.log(e)
        }
    });
}

handleRegions('individual');
handleRegions('legal');
handlePersianDatePicker('#birthday');

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $(input).parents('.ph-regi-upload-file').find('.ph-regi-image-upload-wrap').hide();
            $(input).parents('.ph-regi-upload-file').find('.ph-regi-file-upload-image').attr('src', e.target.result);
            $(input).parents('.ph-regi-upload-file').find('.ph-regi-file-upload-content').show();
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        removeUpload(input);
    }
}

function removeUpload(input) {
    $(input).parents('.ph-regi-upload-file').find('.ph-regi-file-upload-input').replaceWith($('.ph-regi-file-upload-input').clone());
    $(input).parents('.ph-regi-upload-file').find('.ph-regi-file-upload-content').hide();
    $(input).parents('.ph-regi-upload-file').find('.ph-regi-image-upload-wrap').show();
}

$('.ph-regi-image-upload-wrap').bind('dragover', function () {
    $('.ph-regi-image-upload-wrap').addClass('image-dropping');
});
$('.ph-regi-image-upload-wrap').bind('dragleave', function () {
    $('.ph-regi-image-upload-wrap').removeClass('image-dropping');
});

$('[id$=provinces]').find(`option[value="${$('[id$=provinces]').data('value')}"]`).attr('selected', 'selected').trigger("change")
$('[id$=cities]').find(`option[value="${$('[id$=cities]').data('value')}"]`).attr('selected', 'selected')
