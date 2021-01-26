const categories = JSON.parse($('#categories').text());
const commission = "کمیسیون";

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

$(document).ready(function() {
    $('.popup-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'در حال بارگداری #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0,1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',

        }
    });
});

categories.forEach(function (category) {
    $('#t-1-c').append(`<option value="${category.id}">${category.title}</option>`);
});

$('#t-1-c').change(function () {
    $(this).find("[value='default']").remove();
    $('#t-2-c-e').hide();
    $('#t-2-c').empty();
    const categoryId = $(this).val();
    const category = categories.find(function (category) {
        return category.id.toString() === categoryId;
    });
    category.children.forEach(function (child) {
        $('#t-2-c').append(`<option value="${child.id}">${child.title} (${child.commission} ${commission})</option>`)
    })
});

$('#s-1-btn').on('click', function (e) {
    if (!$('#t-2-c :selected').val()) {
        e.preventDefault();
        $('#t-2-c-e').show();
    }

    if (!$('#p-t').val()) {
        e.preventDefault();
        $('#t-e').show();
    } else {
        $('#t-e').hide();
    }

    for (let attr of $('[data-attr]')) {
        if (!$(attr).find('[data-attr-value]').val()) {
            e.preventDefault();
            $(attr).find('small').show();
        } else {
            $(attr).find('small').hide();
        }
    }
})

$('#s-2-btn').on('click', function (e) {

})

$('#s-3-btn').on('click', function (e) {
    $('#preview-product-title').text($('#p-t').val())
    $('#preview-product-description').text($('#ph_spm_create_product_description').val())

    const attributes = $('[id^="attribute-"]')
    for (let i = 0; i < attributes.length; i++) {
        let attr = $(attributes[i])
        $(`#preview-${attr.prop('id')}`).text(attr.val())
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

    for (let i = 0; i < 5; i++) {
        if (!$(`#file-upload-image-${i}`).prop('src').endsWith("#")) {
            $(`#preview-image-${i}`).attr('src', $(`#file-upload-image-${i}`).prop('src'))
            $(`#preview-image-${i}-link`).attr('href', $(`#file-upload-image-${i}`).prop('src'))
        } else {
            $(`#preview-image-${i}`).attr('src', '#').prop('src')
            $(`#preview-image-${i}`).hide()
            $(`#preview-image-${i}-link`).attr('class', 'ph-preview-placeholder')
        }
    }
    $('#preview-image-analyze').attr('src', $('#file-upload-image-attr-0').prop('src'))
    $('#preview-image-analyze-link').attr('href', $('#file-upload-image-attr-0').prop('src'))
});


function readURL(input, id) {
    if (input.files && input.files[0]) {

        var reader = new FileReader();

        reader.onload = function (e) {
            $(`#image-upload-wrap-${id}`).hide();

            $(`#file-upload-image-${id}`).attr('src', e.target.result);
            $(`#file-upload-content-${id}`).show();

        };

        reader.readAsDataURL(input.files[0]);

    } else {
        removeUpload();
    }
}

function removeUpload(id) {
    $(`#file-upload-input-${id}`).replaceWith($(`#file-upload-input-${id}`).clone());
    $(`#file-upload-content-${id}`).hide();
    $(`#image-upload-wrap-${id}`).show();
}

$('[id^="image-upload-wrap-"]').bind('dragover', function () {
    $('[id^="image-upload-wrap-"]').addClass('image-dropping');
});
$('[id^="image-upload-wrap-"]').bind('dragleave', function () {
    $('[id^="image-upload-wrap-"]').removeClass('image-dropping');
});




////////////////////////////////ارسال نمونه


function valueChanged() {
  if($('.ph_ap_check').is(":checked"))
    $(".ph-ap-checked").show();
  else
    $(".ph-ap-checked").hide();
};