jQuery(function ($) {
    var path = window.location.href;
    $('.nav-item a').each(function () {
        if (this.href === path) {
            $(this).addClass('active');
        }
    });
});

jQuery(function ($) {
    var path = window.location.href;
    $('.nav-item a').each(function () {
        if (this.href === path) {
            var parent = $(this).parents('.nav-second-level')
            if (parent.length == 1) {
                $(parent).addClass('show');
            }
        }
    });
});
