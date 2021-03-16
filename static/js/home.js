
// PRODUCTS CAROUSEL IN HOMEPAGE
$('.ph-default-video-slider').owlCarousel({
    loop:true,
    rtl: true,
    margin:30,
    nav:true,
    dots:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        }
    }
})

// Sticky Header On Scroll
$(function() {
    var header = $(".ph-main-header");
    var vheight = $(window).height();
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= vheight) {
            header.addClass("sticky-header");
        } else {
            header.removeClass("sticky-header");
        }
    });

});


