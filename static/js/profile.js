let mineCount = 0;
let addressCount = 0;
const regions = JSON.parse($('#regions').text());

$(document).ready(function() {
    if (window.location.hash !== '') {
        $(window.location.hash).click()
    }
})


function addMineHandler(element) {
    const parent = $(element).parent('#mine')
    let body = {
        title: parent.find('[name="title"]').val(),
        region_id: parent.find('[name="region_id"]').val(),
        address: parent.find('[name="address"]').val(),
        road_name: parent.find('[name="road"]').val(),
        location_in_region: parent.find('[name="location_in_region"]').val(),
        distance_to_road: parent.find('[name="distance_to_road"]').val(),
        proper_road: parent.find('[name="proper_road"]').prop('checked'),
        load_tools: parent.find('[name="load_tools"]').prop('checked')
    }

    $.ajax("/api/mine/", {
        method: "POST",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
        error: function (xhr, status, error) {
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
        },
        success: function (response) {
            parent.find('[form-field]').toArray().forEach(function (v) {
                $(v).attr('disabled', 'true')
            })
            parent.find('#add-mine').remove()
        }
    })
}

function editMineHandler(element) {
    const parent = $(element).parent(`#mine`)
    let body = {
        title: parent.find('[name="title"]').val(),
        region_id: parent.find('[name="region_id"]').val(),
        address: parent.find('[name="address"]').val(),
        road_name: parent.find('[name="road"]').val(),
        location_in_region: parent.find('[name="location_in_region"]').val(),
        distance_to_road: parent.find('[name="distance_to_road"]').val(),
        proper_road: parent.find('[name="proper_road"]').prop('checked'),
        load_tools: parent.find('[name="load_tools"]').prop('checked')
    }

    $.ajax(`/api/mine/${parent.data('count')}`, {
        method: "PUT",
        async: false,
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
        error: function (xhr, status, error) {
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
        },
        success: function (response) {
            parent.find('[form-field]').toArray().forEach(function (v) {
                $(v).attr('disabled', 'true')
            })
            parent.find('#add-mine').remove()
        }
    })
}

function handleMine() {
    $('.extra-fields-customer').click(function () {
        const mineRecord = $('.mine-record').clone();
        mineRecord.appendTo('.customer_records_dynamic');
        mineRecord.attr('class', 'single remove');
        mineRecord.append(`<a href="#" class="edit-info ph-btn" data-count=${mineCount} onclick="addMineHandler(this)" id="add-mine" style="width: 75px">اضافه</a>`);
        mineRecord.append(`<a href="#" data-count="${mineCount}" onclick="removeMineHandler(this)" class="remove-field ph-btn btn-remove-customer" id="remove-mine" style="left: 15%; width: 75px">حذف</a>`);
        mineRecord.attr("id", "mine").attr('data-count', mineCount);
        mineRecord.find('[form-field]').toArray().forEach(function (v, i) {
            let vId = $(v).attr('id')
            vId = `${vId}-${mineCount}`
            $(v).attr('id', vId)
        })
        mineRecord.find('[form-label]').toArray().forEach(function (v, i) {
            let vFor = $(v).attr('for')
            vFor = `${vFor}-${mineCount}`
            $(v).attr('for', vFor)
        })
        mineCount--;
    });
}

function regionChangeHandler(element, id) {
    const parent = $(element).parents(`#${id}`)
    $(element).find("[value='default']").remove();
    parent.find('[id^="city"]').empty();
    const provinceId = $(element).val();
    const province = regions.find(function (category) {
        return category.id.toString() === provinceId;
    });
    province.children.forEach(function (child) {
        parent.find('[id^="city"]').append(`<option value="${child.id}">${child.title}</option>`);
    })
}

function handleRegions() {
    regions.forEach(function (region) {
        $(`[id="province"]`).append(`<option value="${region.id}">${region.title}</option>`);
    });

}

function addAddressHandler(element) {
    const parent = $(element).parents('#address')
    let body = {
        receiver_name: parent.find('[name="receiver_name"]').val(),
        region_id: parent.find('[name="region_id"]').val(),
        address: parent.find('[name="address"]').val(),
        postal_code: parent.find('[name="postal_code"]').val()
    }

    $.ajax("/api/address/", {
        method: "POST",
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
        error: function (xhr, status, error) {
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
        },
        success: function (response) {
            parent.find('[form-field]').toArray().forEach(function (v) {
                $(v).attr('disabled', 'true')
            });
            parent.find('#add-address').remove()
        }
    });
}

function editAddressHandler(element) {
    const parent = $(element).parents(`#address`)
    let body = {
        receiver_name: parent.find('[name="receiver_name"]').val(),
        region_id: parent.find('[name="region_id"]').val(),
        address: parent.find('[name="address"]').val(),
        postal_code: parent.find('[name="postal_code"]').val()
    }


    $.ajax(`/api/address/${parent.data('count')}`, {
        method: "PUT",
        async: false,
        contentType: "application/json",
        headers: {
            'Accept-Language': 'fa',
        },
        data: JSON.stringify(body),
        error: function (xhr, status, error) {
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
        },
        success: function (response) {
            parent.find('[form-field]').toArray().forEach(function (v) {
                $(v).attr('disabled', 'true')
            });
            parent.find('#add-address').remove()
        }
    });
}

function handleAddress() {
    $('.extra-fields-customer').click(function () {
        const addressRecord = $('.address-record').clone();
        addressRecord.appendTo('.customer_records_dynamic');
        addressRecord.attr('class', 'single remove');
        addressRecord.append(`<a href="#" class="edit-info ph-btn" data-count=${addressCount} onclick="addAddressHandler(this)" id="add-address" style="width: 75px">اضافه</a>`);
        addressRecord.append(`<a href="#" data-count="${addressCount}" onclick="removeAddressHandler(this)" class="remove-field ph-btn btn-remove-customer" id="remove-address" style="left: 15%; width: 75px">حذف</a>`);
        addressRecord.attr("id", "address").attr('data-count', addressCount);
        addressRecord.find('[form-field]').toArray().forEach(function (v, i) {
            let vId = $(v).attr('id')
            vId = `${vId}-${addressCount}`
            $(v).attr('id', vId)
        })
        addressRecord.find('[form-label]').toArray().forEach(function (v, i) {
            let vFor = $(v).attr('for')
            vFor = `${vFor}-${addressCount}`
            $(v).attr('for', vFor)
        })
        addressCount--;
    });
}


handleMine()
handleRegions()
handleAddress()
$('select[mine-val]#province').find(`option[value="${$('select[mine-val]#province').data('value')}"]`).attr('selected', 'selected').trigger("change")
$('select[mine-val]#city').find(`option[value="${$('select[mine-val]#city').data('value')}"]`).attr('selected', 'selected')
