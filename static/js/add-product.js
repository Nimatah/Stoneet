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
    $('#preview-product-title').text($('#product-title').val())
    $('#preview-product-description').text($('#product-description').val())

    const attributes = $('[id^="attribute-"]')
    for (let i = 0; i < attributes.length; i++) {
        let attr = $(attributes[i])
        console.log(attr)
        $(`#preview-${attr.id}`).text(attr.val())
        console.log(`preview-${attr.id}`)
    }
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
