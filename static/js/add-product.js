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

function handleCategories() {
    const categories = JSON.parse($('#categories').text());

    categories.forEach(function (category) {
        $('#t-1-c').append(`<option value="${category.id}">${category.title}</option>`);
    });

    $('input[data-choice]').on('change', function (e) {
        const input = $(this);
        const labels = $(`label[for^="multiple-choice-${input.data('attr-id')}"]`);
        let value = labels
            .map((i, v) => $(`input#${$(v).prop('for')}`).is(":checked") ? $(v).text() : '')
            .filter((i, v) => v !== '');
        $(`input#attribute-${input.data('attr-id')}`).attr('value', value.toArray().join('|'));
    })

    $('#t-1-c').change(function () {
        $(this).find("[value='default']").remove();
        $('#t-2-c-e').hide();
        $('#t-2-c').empty();
        const categoryId = $(this).val();
        const category = categories.find(function (category) {
            return category.id.toString() === categoryId;
        });
        category.children.forEach(function (child) {
            $('#t-2-c').append(`<option data-comission="${child.comission}" value="${child.id}">${child.title}</option>`)
        })
    });
}

function handlePart1Form() {
    $('[id^="weight-attribute-"]').on('change', function () {
        $(this).find('[value="default"]').remove()
    })

    $('#ph-btn-next1').on('click', function (e) {
        let category = $('#t-2-c').val()
        if (category === '') {
            e.preventDefault()
            $('#error-modal .modal-body').empty().append(`<div><span class="font-weight-bold">گروه</span>: لطفا گروه را انتخاب کنید</div>`);
            $('#error-modal').modal('show');
            return
        }

        let attributes = $('div#part1 [id^="attribute-"], [id^="weight-attribute"], [id^="child-attribute"]')
        const body = attributes.toArray().reduce(function (acc, cur) {
            const element = $(cur)
            if (element.val() !== '') {
                acc[element.prop('name')] = element.val()
            }
            return acc
        }, {});
        body['mine'] = $('#product-mine').val()
        $.ajax("/api/validate/add-product/p1", {
            method: "POST",
            async: false,
            contentType: "application/json",
            headers: {
                'Accept-Language': 'fa',
            },
            data: JSON.stringify(body),
            error: function (xhr, status, error) {
                e.preventDefault();
                $('#error-modal .modal-body').empty()
                let response = JSON.parse(xhr.responseText)
                let errors = [];
                for (let k in response) {
                    errors.push({
                        title: k,
                        value: response[k]
                    })
                }
                errors.forEach(function (v, i) {
                    $('#error-modal .modal-body').append(
                        `<div><span class="font-weight-bold">${v.title}</span>: ${v.value}</div>`
                    )
                })
                $('#error-modal').modal('show');
            }
        })
    });
}

function handlePart2Form() {
    $('#ph-btn-next2').on('click', function (e) {
        let analyzeImage = $('#file-upload-input-analyze');
        if (analyzeImage.val() === "" || analyzeImage.val() === undefined || analyzeImage.val() === null) {
            e.preventDefault();
            $('#error-modal .modal-body').empty();
            $('#error-modal .modal-body').append(`<div>لطفا عکس آنالیز محصول را وارد نمایید</div>`);
            $("#error-modal").modal('show');
        }
    })
}

function handlePart3Form() {
    $('#ph-btn-next3').on('click', function (e) {
        let primaryImage = $('#file-upload-input-0');
        if (primaryImage.val() === "" || primaryImage.val() === undefined || primaryImage.val() === null) {
            e.preventDefault();
            $('#error-modal .modal-body').empty();
            $('#error-modal .modal-body').append(`<div>لطفا عکس اصلی محصول را وارد نمایید</div>`);
            $("#error-modal").modal('show');
        }
        _handleFormPreview();
    });
}

function handlePart4Form() {
    $('#add-product-submit').on('click', function (e) {
        if (!$('#rules_check').prop('checked')) {
            $('#error-modal .modal-body').empty();
            $('#error-modal .modal-body').append(`<div>برای ثبت محصول قوانین و مقررات را مطالعه کرده و تیک آن را بزنید.</div>`);
            $('#error-modal').modal('show')
            e.preventDefault();
        }
    })
}

function _handleFormPreview() {

    const imagePreviewElement = function (src) {
        return `<a href="${src}">
            <img class="square-image" src="${src}">
            </a>`;
    }
    const handleTitle = function () {
        const CARET = 'عیار';
        const TO = '-';
        const category = $('select[name="category"] :selected').text();
        const _caretMin = $('#attribute-12').val();
        const _caretMax = $('#attribute-13').val();
        const caret = _caretMin === _caretMax ? `${_caretMin}` : `${_caretMin} ${TO} ${_caretMax}`
        $('#preview-product-title').text(`${category} ${CARET} ${caret} %`)
        $('input[name="title"]').val(`${category} ${CARET} ${caret} %`)
    }

    const handleMine = function () {
        let mine = $('#product-mine option:selected').text()
        $('#preview-product-mine').text(mine);
    }

    const handleDescription = function () {
        let description = $('#ph_spm_create_product_description').val()
        description.replace(/(?:\r\n|\r|\n)/g, '<br>');
        $('#preview-product-description').text(description)
    }

    const handleAttributes = function () {
        const attributes = $('[id^="attribute-"]')
        for (let i = 0; i < attributes.length; i++) {
            let attr = $(attributes[i])
            if (attr.parents(".num-input").length) {
                let text = attr.val() === attr.parents(".num-input").find('[data-max]').val() ? attr.val() : `${attr.val()} - ${attr.parents(".num-input").find('[data-max]').val()}`
                if (attr.parents('.num-input').find('select')) {
                    text = text + ' ' + attr.parents('.num-input').find('select option:selected').text()
                }
                $(`#preview-${attr.prop('id')}`).text(text)
            } else {
                ` `
                let val = attr.val().replaceAll("|", "، ")
                val = val ? `${val} ${attr.prop('id') == 'attribute-17' ? 'تن' : attr.prop('id') == 'attribute-5' ? "کیلوگرم" : ""}` : 'ندارد'
                $(`#preview-${attr.prop('id')}`).text(val)
            }
            let child = $(`#child-${attr.prop('id')}`)
            let weight = $(`#weight-${attr.prop('id')}`)
            if (child.val() || weight.val()) {
                let previewText = $(`#preview-${attr.prop('id')}`).text()
                $(`#preview-${attr.prop('id')}`).text(`${previewText} ${child.val() || ''} ${attr.prop("id") == "attribute-1" ? "ریال به ازای هر" : ""} ${weight.find('option:selected').text() || ''}`)
            }
        }

        const boolAttributes = $('[id^="attributebool-"]')
        for (let i = 0; i < boolAttributes.length; i++) {
            let attr = $(boolAttributes[i])
            let preview = $(`#preview-${attr.prop('id')}`)
            if (attr.prop('checked')) {
                preview.attr('class', 'fas fa-check')
            } else {
                preview.attr('class', 'fas fa-times')
            }
        }
    }

    const handleImages = function () {
        $('#images-preview').empty();
        for (let i = 1; i < 5; i++) {
            if ($(`#file-upload-input-${i}`).val() && $(`#file-upload-input-${i}`).val() !== "") {
                $('#images-preview').append(imagePreviewElement($(`#file-upload-image-${i}`).prop('src')));
            }
        }

        $('#preview-image-0').attr('src', $('#file-upload-image-0').prop('src'))
        $('#preview-image-0-link').removeAttr("href")
        $('#preview-image-0-link').attr('href', $('#file-upload-image-0').prop('src'))

        $('#preview-image-analyze').attr('src', $('#file-upload-image-analyze').prop('src'))
        $('#preview-image-analyze-link').removeAttr("href")
        $('#preview-image-analyze-link').attr('href', $('#file-upload-image-analyze').prop('src'))
    }

    handleTitle();
    handleDescription();
    handleMine();
    handleAttributes();
    handleImages();
}

function readURL(input, id) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $(`#image-upload-wrap-${id}`).hide();
            $(`a[id="file-upload-image-${id}"]`).attr('href', e.target.result);
            $(`img[id="file-upload-image-${id}"]`).attr('src', e.target.result);
            $(`#file-upload-content-${id}`).show();
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        removeUpload();
    }
}

function removeUpload(id) {
    $(`#file-upload-input-${id}`).val("")
    $(`#file-upload-content-${id}`).hide();
    $(`#image-upload-wrap-${id}`).show();
}

$('[id^="image-upload-wrap-"]').bind('dragover', function () {
    $('[id^="image-upload-wrap-"]').addClass('image-dropping');
});
$('[id^="image-upload-wrap-"]').bind('dragleave', function () {
    $('[id^="image-upload-wrap-"]').removeClass('image-dropping');
});


function sampleViewInputField() {
    if ($('.ph_ap_check').is(":checked")) {
        $(".ph-ap-checked").show();
    } else {
        $(".ph-ap-checked input").val('');
        $(".ph-ap-checked").hide();
    }
}

var $form = $('#edit-admin-list'),
    $errorMsg = $("<span class='error'>پر کردن این گزینه اجباری است</span>");

$('#ph_signup_submit_btn').on("click", function () {

    if (isEmailValid($('#email-field').val())) {
        jQuery("#email-error-field").hide();
    } else {
        jQuery("#email-error-field").show();
    }

    var toReturn = true;
    $("input,select", $form).each(function () {

        if ($(this).val() == "") {

            if (!$(this).data("error")) {
                $(this).data("error", $errorMsg.clone().insertAfter($(this)));
            }
            toReturn = false;
        } else {

            if ($(this).data("error")) {
                $(this).data("error").remove();
                $(this).removeData("error");
            }
        }
    });
    return toReturn;
});

function isEmailValid(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

handleCategories();
handlePart1Form();
handlePart2Form();
handlePart3Form();
handlePart4Form();

//
// const $fale = $('select#attribute-16')
//
// if ($fale.val() == 'بار فله‌ای') {
//     $('#weight-attribute-16').hide()
//     $('#child-attribute-16').hide()
// }
//
// $fale.on('change', function (e) {
//     if ($fale.val() == 'بار فله‌ای') {
//         $('#weight-attribute-16').hide()
//         $('#child-attribute-16').hide()
//     } else {
//         $('#weight-attribute-16').show()
//         $('#child-attribute-16').show()
//     }
// })