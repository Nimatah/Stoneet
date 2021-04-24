function clearAuctionModal() {
    $('#ph_auction .modal-body #auction-start').val("")
    $('#ph_auction .modal-body #order-id').val("")
    $('#ph_auction .modal-body #auction-finish').val("")
    $('#ph_auction .modal-body #category').val("")
    $('#ph_auction .modal-body #delivery-type').val("")
    $('#ph_auction .modal-body #weight').val("")
    $('#ph_auction .modal-body #monthly-load').val("")
    $('#ph_auction .modal-body #monthly-load-weight').val("")
    $('#ph_auction .modal-body #source-province').text("")
    $('#ph_auction .modal-body #source-city').text("")
    $('#ph_auction .modal-body #source-address').text("")
    $('#ph_auction .modal-body #destination-province').text("")
    $('#ph_auction .modal-body #destination-city').text("")
    $('#ph_auction .modal-body #destination-address').text("")
    $('#ph_auction .modal-body #lowest-bid').val("")
    $('#ph_auction #persist-bid').removeAttr('data-auction-id')
}

$('#bid-action').on('click', function(e) {
    e.preventDefault();

    const auctionId = $('#bid-action').data('auction-id');

    $.ajax(`/api/auctions/${auctionId}`, {
        method: 'GET',
        dataType: 'json',
        success: function (response) {
            clearAuctionModal();
            $('#ph_auction').modal('show');
            $('#ph_auction .modal-body');
            $('#ph_auction .modal-body #auction-start').val(response.start_date)
            $('#ph_auction .modal-body #order-id').val(response.order.id)
            $('#ph_auction .modal-body #auction-finish').val(response.finish_date)
            $('#ph_auction .modal-body #category').val(response.order.category)
            $('#ph_auction .modal-body #delivery-type').val(response.order.delivery_type)
            $('#ph_auction .modal-body #weight').val(response.order.weight)
            $('#ph_auction .modal-body #monthly-load').val(response.order.monthly_load)
            $('#ph_auction .modal-body #monthly-load-weight').val(response.order.monthly_load_weight)
            $('#ph_auction .modal-body #source-province').text(response.source.province)
            $('#ph_auction .modal-body #source-city').text(response.source.city)
            $('#ph_auction .modal-body #source-address').text(response.source.address)
            $('#ph_auction .modal-body #destination-province').text(response.destination.province)
            $('#ph_auction .modal-body #destination-city').text(response.destination.city)
            $('#ph_auction .modal-body #destination-address').text(response.destination.address)
            $('#ph_auction .modal-body #lowest-bid').val(response.lowest_bid)
            $('#ph_auction #persist-bid').attr('data-auction-id', response.id)
        }
    })
});

$('#persist-bid').on('click', function (e) {
    e.preventDefault();

    const auctionId = $('#persist-bid').data('auction-id');
    const bidPrice = $('#bid-price').val();

    $.ajax(`/api/auctions/${auctionId}/bid`, {
        method: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify({
            price: bidPrice
        }),
        success: function (response) {
            location.reload();
            return false;
        },
        error: function (xhr, status, error) {
            let response = JSON.parse(xhr.responseText)
            $('#auction-error').text(response.message);
            $('#auction-error').show();
        }
    })


})