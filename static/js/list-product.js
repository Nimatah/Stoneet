const categories = JSON.parse($('#categories').text());

function preventEmptyFieldForm(id) {
    $(id).submit(function () {
        $(this)
            .find('input[name]')
            .filter(function () {
                return !this.value;
            })
            .prop('name', '');
    });
}

function getUrlVars() {
    const vars = []
    let hash;
    const hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for (let i = 0; i < hashes.length; i++) {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

categories.forEach(function (category) {
    $('#ph-categories').append(`<option value="${category.id}">${category.title}</option>`);
});

$('#ph-categories').change(function () {
    $(this).find("[value='default']").remove();
    $('#ph-sub-categories').empty();
    $('#ph-sub-categories').append('<option value="">انتخاب کنید</option>');
    const categoryId = $(this).val();
    const category = categories.find(function (category) {
        return category.id.toString() === categoryId;
    });
    category.children.forEach(function (child) {
        $('#ph-sub-categories').append(`<option value="${child.id}">${child.title}</option>`);
    })
});

preventEmptyFieldForm('#ph_admin_search_text');
preventEmptyFieldForm('#ph-categories');
preventEmptyFieldForm('#ph-sub-categories');
preventEmptyFieldForm('#ph-state');

const queryParams = getUrlVars();

if (queryParams.category !== undefined && queryParams.category !== '') {
    $(`#ph-categories option[value=${queryParams.category}]`).attr('selected', 'selected').trigger('change');
}

if (queryParams.scategory !== undefined && queryParams.scategory !== '') {
    $(`#ph-sub-categories option[value=${queryParams.scategory}]`).attr('selected', 'selected').trigger('change');
}

if (queryParams.state !== undefined && queryParams.state !== '') {
    $(`#ph-state option[value=${queryParams.state}]`).attr('selected', 'selected').trigger('change');
}

if (queryParams.q !== undefined && queryParams.q !== '') {
    $('#ph_admin_search_text').text(queryParams.q).trigger('change');
}

