/*$(document).ready(function () {
    $('#navAccordion .nav-item').click(function (ev) {
        $('#navAccordion .nav-item').removeClass('active');
        $(ev.currentTarget).parent('li').addClass('active');
    });
});

$( function() {
  $('#navAccordion .nav-item').click( function() {
    $(this).toggleClass("ph-sp-navbar-nav");
  } );
} );

$('#navAccordion .nav-item').click(function() {
    $("#navAccordion .nav-item").each(function(i,elem) {
        $(elem).removeClass("clicked");
    });
    $(this).addClass("clicked");
});

$('#navAccordion .nav-item').hover(
   function() {
    if(!$(this).hasClass("clicked"))
    {
     $(this).animate({
         backgroundColor: '#000'
     }, 300);
    }
   },
  function() {
   if(!$(this).hasClass("clicked")) {
     $(this).animate({
         backgroundColor: '#999'
     }, 200);
     }
    }
);

$('#navAccordion .nav-item').on('click', function (){
    $('#navAccordion .nav-item').removeClass('active');
    $(this).addClass('active');
})*/
/*
        $('#navAccordion .nav-item a').click(function(){
        $(this).addClass('active').siblings().removeClass('active');
        });*/
/*$(document).ready(function() {
    $("#navAccordion .nav-item").each(function() {
        if (this.href == window.location.href) {
            $(this).addClass("active");
        }
    });
});*/

/*$(function() {
  $('nav a[href^="/users/panel/seller-dashboard/' + location.pathname.split("/users/panel/seller-dashboard/")[1] + '"]').addClass('active');
});

$(function(){
    var current = location.pathname;
    $('#navAccordion .nav-item li a').each(function(){
        var $this = $(this);
        if($this.attr('href').indexOf(current) !== -1){
            $this.addClass('active');
        }
    })
})*/
/*var doc_location = document.location.href;
var url_strip = new RegExp("http:\/\/.*\/");
var base_url = url_strip.exec(doc_location)
var base_url_string = base_url[0];

switch (base_url_string){
    case "/users/panel/seller-dashboard/":
                $('.menu-item a').click(function(){
        $(this).addClass('active').siblings().removeClass('active');
        });
                break;
}*/

/*
    $(document).ready(function () {
        console.log("current page", window.location.href);
        $("[href]").each(function () {
            $('a[href]:not([href=#])').each(function () {

                if (window.location.href.indexOf($(this).attr('href')) > -1) {
                    console.log($(this).attr('href') +" is active ");
                    $(this).addClass('active');
                }
                else {
                    console.log($(this).attr('href') + "is not active ");
                }
            });
        });
    });*/

/*$(document).ready(function() {

 var url = window.location.href;

 url = url.substring(0, (url.indexOf("#") == -1) ? url.length : url.indexOf("#"));

 url = url.substring(0, (url.indexOf("?") == -1) ? url.length : url.indexOf("?"));

 url = url.substr(url.lastIndexOf("/") + 1);

 if(url == ''){
 url = 'index.html';
 }

 $('.nav-item a').each(function(){

  var href = $(this).find('a').attr('href');

  if(url == href){

   var parentClass = $(this).parent('ul').attr('class');

   if(parentClass == 'submenu'){

    $(this).addClass('subactive');
    $(this).parents('.nav-item a').addClass('active');
   }else{

    $(this).addClass('active');
   }

  }
 });
 console.log(url);
});*/
/*
  jQuery(function($) {
      var pgurl = window.location.href.substr(window.location.href.lastIndexOf("/")+1);
        $("#navAccordion .nav-link").each(function(){
        if($(this).attr("href") == pgurl || $(this).attr("href") == '' )
        $(this).addClass("active");
        // $(this).parent("li").addClass("active");
      })
  });*/

/*
$(function () {
    setNavigation();
});

function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $(".nav-link a").each(function () {
        var href = $(this).attr('href');
        if (path.substring(0, href.length) === href) {
            $(this).closest('li').addClass('active');
        }
    });
}
*/

jQuery(function($) {
  var path = window.location.href;
  $('.nav-item a').each(function() {
    if (this.href === path) {
      $(this).addClass('active');
    }
  });
});

/** add active class and stay opened when selected */
/*
var url = window.location;

// for sidebar menu entirely but not cover treeview
$('ul.nav-link a').filter(function() {
	 return this.href == url;
}).parent().addClass('active');

// for treeview
$('ul.nav-second-level a').filter(function() {
	 return this.href == url;
}).parentsUntil(".nav-link > .nav-second-level").addClass('active');*/

/*
$('.nav-item .nav-second-level').on({
	"click":function(e){
      e.stopPropagation();
    }
});
$('.closer').on('click', function () {
    $('.btn-group').removeClass('open');
});*/
/*
var dropdown = document.getElementsByClassName("nav-link");
var i;
for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    //	    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

$(".nav-second-level a").each(function() {
  if (this.href == window.location.href) {
    $(this).addClass("active");
    $("dropdown-btn").css({display : "none"});
    $(this).closest(".dropdown-btn").css({display : "block"});
  }
});
*/
/*var url = location.href;

$('.nav-link').each(function() {
    var $dropdownmenu = $(this);
    $(this).find('li').each(function() {
        if( $(this).find('a').attr('href')== url ) {
            console.log( $dropdownmenu ); // this is your dropdown menu which you want to display
            console.log($($dropdownmenu).parents('li')); // this is the parent list item of the dropdown menu. Add collapse class or whatever that collapses its child list
        }
    });
});*/
