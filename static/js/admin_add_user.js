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

$(document).ready(function () {
    $(".ph-conditional").change(function () {
        let selected = $(".ph-conditional .custom-control-input:checked").data('tab');
        $('.ph-conditional-wrapper').hide();
        $('.ph-conditional-wrapper-2').hide();
        $('#' + selected).show();
        $('#' + selected + -2).show();

    });
    $('.ph-conditional-wrapper').hide();
    $('.ph-conditional-wrapper-2').hide();
});

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