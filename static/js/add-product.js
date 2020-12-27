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


function initImageUpload(box) {
  let uploadField = box.querySelector('.image-upload');

  uploadField.addEventListener('change', getFile);

  function getFile(e){
    let file = e.currentTarget.files[0];
    checkType(file);
  }

  function previewImage(file){
    let thumb = box.querySelector('.js--image-preview'),
        reader = new FileReader();

    reader.onload = function() {
      thumb.style.backgroundImage = 'url(' + reader.result + ')';
    }
    reader.readAsDataURL(file);
    thumb.className += ' js--no-default';
  }

  function checkType(file){
    let imageType = /image.*/;
    if (!file.type.match(imageType)) {
      throw 'Datei ist kein Bild';
    } else if (!file){
      throw 'Kein Bild gewählt';
    } else {
      previewImage(file);
    }
  }

}

// initialize box-scope
var boxes = document.querySelectorAll('.box');

for (let i = 0; i < boxes.length; i++) {
  let box = boxes[i];
  initDropEffect(box);
  initImageUpload(box);
}



/// drop-effect
function initDropEffect(box){
  let area, drop, areaWidth, areaHeight, maxDistance, dropWidth, dropHeight, x, y;

  // get clickable area for drop effect
  area = box.querySelector('.js--image-preview');
  area.addEventListener('click', fireRipple);

  function fireRipple(e){
    area = e.currentTarget
    // create drop
    if(!drop){
      drop = document.createElement('span');
      drop.className = 'drop';
      this.appendChild(drop);
    }
    // reset animate class
    drop.className = 'drop';

    // calculate dimensions of area (longest side)
    areaWidth = getComputedStyle(this, null).getPropertyValue("width");
    areaHeight = getComputedStyle(this, null).getPropertyValue("height");
    maxDistance = Math.max(parseInt(areaWidth, 10), parseInt(areaHeight, 10));

    // set drop dimensions to fill area
    drop.style.width = maxDistance + 'px';
    drop.style.height = maxDistance + 'px';

    // calculate dimensions of drop
    dropWidth = getComputedStyle(this, null).getPropertyValue("width");
    dropHeight = getComputedStyle(this, null).getPropertyValue("height");

    // calculate relative coordinates of click
    // logic: click coordinates relative to page - parent's position relative to page - half of self height/width to make it controllable from the center
    x = e.pageX - this.offsetLeft - (parseInt(dropWidth, 10)/2);
    y = e.pageY - this.offsetTop - (parseInt(dropHeight, 10)/2) - 30;

    // position drop and animate
    drop.style.top = y + 'px';
    drop.style.left = x + 'px';
    drop.className += ' animate';
    e.stopPropagation();

  }
}
