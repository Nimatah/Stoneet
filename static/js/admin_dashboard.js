$('#seller-submit').on('click', function (e) {
    let hasValue;
    const values = $('#seller-id,#seller-name,#seller-mobile-number').toArray().map(function (el) {
        if ($(el).val() != '') {
            hasValue = true
        }
    })

    if (!hasValue) {
        $('#seller-error').show();
    } else {
        $('#seller-error').hide();
        const queryParams = $('#seller-id,#seller-name,#seller-mobile-number')
            .toArray()
            .reduce(function (acc, cur) {
            const element = $(cur)
            if (element.val() !== '') {
                acc[element.prop('name')] = element.val()
            }
            return acc
        }, {});
        $.ajax('/api/users/',{
            data: queryParams,
            method: "GET",
            success: function (response) {
                $('#seller-table').show()
                $('#seller-table-body').empty()
                response.forEach(function (seller) {
                    $('#seller-table-body').empty().append(`
                    <tr>
                        <td>${seller.id}</td>
                        <td>${seller.full_name}</td>
                        <td>${seller.email}</td>
                        <td>${seller.mobile_number}</td>
                        <td>${seller.region}</td>
                        <td>${seller.state}</td>
                        <td>
                            <a href="/users/panel/admin-add-product/?seller=${seller.id}"
                               class="ph-btn ph-managements-btn qc"><i
                                    class="fas fa-mouse-pointer"></i>انتخاب</a>
                        </td>
                    </tr>
                    `)
                })
            },
        })
    }
})
