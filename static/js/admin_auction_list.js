function countdownTimeStart(time) {

    var countDownDate = new Date(time).getTime();

    window.countdownInterval = setInterval(function () {

        var now = new Date().getTime();

        // Find the distance between now an the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Output the result in an element with id="demo"
        document.getElementById("countdown").innerHTML = hours + ":"
            + minutes + ":" + seconds + ":";

        // If the count down is over, write some text
        if (distance < 0) {
            clearInterval(window.countdownInterval);
            document.getElementById("countdown").innerHTML = "تمام شده";
        }
    }, 1000);
}

function clearAuctionModal() {
    $('#ph_auction_admin_Modal .modal-body #auction-start').val("")
    $('#ph_auction_admin_Modal .modal-body #order-id').val("")
    $('#ph_auction_admin_Modal .modal-body #auction-finish').val("")
    $('#ph_auction_admin_Modal .modal-body #category').val("")
    $('#ph_auction_admin_Modal .modal-body #delivery-type').val("")
    $('#ph_auction_admin_Modal .modal-body #weight').val("")
    $('#ph_auction_admin_Modal .modal-body #monthly-load').val("")
    $('#ph_auction_admin_Modal .modal-body #monthly-load-weight').val("")
    $('#ph_auction_admin_Modal .modal-body #source-province').text("")
    $('#ph_auction_admin_Modal .modal-body #source-city').text("")
    $('#ph_auction_admin_Modal .modal-body #source-address').text("")
    $('#ph_auction_admin_Modal .modal-body #destination-province').text("")
    $('#ph_auction_admin_Modal .modal-body #destination-city').text("")
    $('#ph_auction_admin_Modal .modal-body #destination-address').text("")
    $('#ph_auction_admin_Modal .modal-body #lowest-bid').val("")
    $('#ph_auction_admin_Modal .modal-body #reactivate').removeAttr('data-auction-id')
    clearInterval(window.countdownInterval);
}

$('#view-auction').on('click', function(e) {
    e.preventDefault();

    const auctionId = $('#view-auction').data('auction-id');

    $.ajax(`/api/auctions/${auctionId}/admin`, {
        method: 'GET',
        dataType: 'json',
        success: function (response) {
            clearAuctionModal();
            $('#ph_auction_admin_Modal').modal('show');
            $('#ph_auction_admin_Modal .modal-body');
            $('#ph_auction_admin_Modal .modal-body #auction-start').val(response.start_date)
            $('#ph_auction_admin_Modal .modal-body #order-id').val(response.order.id)
            $('#ph_auction_admin_Modal .modal-body #auction-finish').val(response.finish_date)
            $('#ph_auction_admin_Modal .modal-body #category').val(response.order.category)
            $('#ph_auction_admin_Modal .modal-body #delivery-type').val(response.order.delivery_type)
            $('#ph_auction_admin_Modal .modal-body #weight').val(response.order.weight)
            $('#ph_auction_admin_Modal .modal-body #monthly-load').val(response.order.monthly_load)
            $('#ph_auction_admin_Modal .modal-body #monthly-load-weight').val(response.order.monthly_load_weight)
            $('#ph_auction_admin_Modal .modal-body #source-province').text(response.source.province)
            $('#ph_auction_admin_Modal .modal-body #source-city').text(response.source.city)
            $('#ph_auction_admin_Modal .modal-body #source-address').text(response.source.address)
            $('#ph_auction_admin_Modal .modal-body #destination-province').text(response.destination.province)
            $('#ph_auction_admin_Modal .modal-body #destination-city').text(response.destination.city)
            $('#ph_auction_admin_Modal .modal-body #destination-address').text(response.destination.address)
            $('#ph_auction_admin_Modal .modal-body #lowest-bid').val(response.min_bid)
            $('#ph_auction_admin_Modal .modal-body #reactivate').attr('data-auction-id', response.id)
            countdownTimeStart(response.finish_timestamp)
        }
    })
});

$('#reactivate').on('click', function (e) {
    e.preventDefault();

    const auctionId = $('#reactivate').data('auction-id')

    $.ajax(`/api/auctions/${auctionId}/admin/reactivate`, {
        method: "GET",
        dataType: 'json',
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