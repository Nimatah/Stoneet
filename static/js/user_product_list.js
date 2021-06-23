function getQueryParams() {
    return new URLSearchParams(window.location.search)
}

const params = getQueryParams();

$('input#search_products').val(params.get('q'))

const categoryParams = params.getAll('category')

if (categoryParams) {
    for (let i in categoryParams) {
        $(`input[name="category"][value=${categoryParams[i]}]`).attr('checked', true)
    }
}
