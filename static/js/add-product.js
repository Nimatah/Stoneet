const categories = JSON.parse($('#categories').text());
const commission = "کمیسیون";


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

    $('#preview-image-0').attr('src', $('#file-upload-image-0').prop('src'))
    $('#preview-image-analyze').attr('src', $('#file-upload-image-attr-0').prop('src'))
    $('#preview-image-1').attr('src', $('#file-upload-image-1').prop('src'))
    $('#preview-image-2').attr('src', $('#file-upload-image-2').prop('src'))
    $('#preview-image-3').attr('src', $('#file-upload-image-3').prop('src'))
    $('#preview-image-4').attr('src', $('#file-upload-image-4').prop('src'))

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
