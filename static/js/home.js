$('.ph-default-products-slider').owlCarousel({
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
            items:3
        },
        1000:{
            items:4
        }
    }
})