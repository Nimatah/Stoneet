$(".imgAdd").click(function () {
        const parent = $(this).closest(".row").prop("id")
        $(this).closest(".row").find('.imgAdd').before(`
            <div class="col-3 col-md-2 imgUp">
                <div class="imagePreview"> </div>
                    <label>
                        <input id="image_${$(`div#${parent}`).find('.imgUp').length + 1}" class="image-name-3" type="text" readonly>
                    </label>
                    <label class="btn ph-spm-create-product-img-up-btn">آپلود
                        <input data-new="new" type="file" class="uploadFile img upload-btn-3" value="Upload Photo" style="width:0px;height:0px;overflow:hidden;" id="image_button_${$(`div#${parent}`).find('.imgUp').length + 1}">
                    </label>
                    <i class="fa fa-times del"></i>
            </div>`);
    }
);

$(document).on("click", "i.del", function () {
    $(this).parent().remove();
});

$('i.del-backend').on("click", function () {
    const mediapk = $(this).data('mediapk')
    $.ajax(`/api/orders/${orderId}/media/${mediapk}`, {
            method: "DELETE",
            success: function (resp) {

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
        }
    )
});

$(function () {
    $(document).on("change", ".uploadFile", function () {
        var uploadFile = $(this);
        var files = !!this.files ? this.files : [];
        if (!files.length || !window.FileReader) return;

        if (/^image/.test(files[0].type)) {
            var reader = new FileReader();
            reader.readAsDataURL(files[0]);

            reader.onloadend = function () {
                uploadFile.closest(".imgUp").find('.imagePreview').css("background-image", "url(" + this.result + ")");
            }
        }

    });
});

$(document).on('change', '.upload-btn-3', function () {
    $(this).parent().parent().find('.image-name-3').val(this.files && this.files.length ? this.files[0].name.split('.')[0] : '');
});

$('#s-3-btn').on('click', function (e) {
    const $images = $('#contract_images [id^="image_button"][data-new="new"]')

    const formData = new FormData()
    $images.toArray().forEach(function (v, i) {
        formData.append(`${i}`, v.files[0])
    })

    $.ajax(`/api/orders/${orderId}/upload-signed`, {
        method: "POST",
        data: formData,
        async: false,
        processData: false,
        contentType: false,
        success: function (e) {

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
})

$('#s-4-btn').on('click', function (e) {
    const $images = $('#finance_images [id^="image_button"][data-new="new"]')

    const formData = new FormData()
    $images.toArray().forEach(function (v, i) {
        formData.append(`${i}`, v.files[0])
    })

    $.ajax(`/api/orders/${orderId}/upload-finance`, {
        method: "POST",
        data: formData,
        async: false,
        processData: false,
        contentType: false,
        success: function (e) {

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
})

