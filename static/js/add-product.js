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
})

$('#s-2-btn').on('click', function (e) {
    if (!$('#p-t').val()) {
        e.preventDefault();
        $('#t-e').show();
    } else {
        $('#t-e').hide();
    }
})

$('#s-3-btn').on('click', function (e) {
    for (let attr of $('[data-attr]')) {
        if (!$(attr).find('[data-attr-value]').val()) {
            e.preventDefault();
            $(attr).find('small').show();
        } else {
            $(attr).find('small').hide();
        }
    }
});







      $(".imgAdd").click(function () {
         $(this).closest(".row").find('.imgAdd').before('<div class="col-6 col-md-4 imgUp"><div class="imagePreview"></div><label class="btn ph-spm-create-produc-img-up-btn">آپلود<input type="file" class="uploadFile img" value="Upload Photo" style="width:0px;height:0px;overflow:hidden;"></label><i class="fa fa-times del"></i></div>');
      });
      $(document).on("click", "i.del", function () {
         $(this).parent().remove();
      });
      $(function () {
         $(document).on("change", ".uploadFile", function () {
            var uploadFile = $(this);
            var files = !!this.files ? this.files : [];
            if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support

            if (/^image/.test(files[0].type)) { // only image file
               var reader = new FileReader(); // instance of the FileReader
               reader.readAsDataURL(files[0]); // read the local file

               reader.onloadend = function () { // set image data as background of div
                  //alert(uploadFile.closest(".upimage").find('.imagePreview').length);
                  uploadFile.closest(".imgUp").find('.imagePreview').css("background-image", "url(" + this.result + ")");
               }
            }

         });
      });