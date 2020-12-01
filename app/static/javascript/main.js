/**
  * isMobile
  * responsiveMenu
  * simpleSlider
  * popupGallery  
  * iconCanvasClick
  * iconSearchClick
  * iconFilterClick
  * parallax
  * Carousel_slider
  * blogMasory
  * Masonry_GalleryGrid
  * projectIsotope
  * flatAnimation
  * ajaxContactForm
  * alertBox
  * WoocommerceSlider
  * Flexslider_Images
  * goTop  
  * removePreloader
*/

;(function($) {

    'use strict'
    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };

    var responsiveMenu = function() {
        var menuType = 'desktop';

        $(window).on('load resize', function() {
            var currMenuType = 'desktop';

            if ( matchMedia( 'only screen and (max-width: 991px)' ).matches ) {
                currMenuType = 'mobile';
            }

            if ( currMenuType !== menuType ) {
                menuType = currMenuType;

                if ( currMenuType === 'mobile' ) {
                    var $mobileMenu = $('#mainnav').attr('id', 'mainnav-mobi').hide();
                    var hasChildMenu = $('#mainnav-mobi').find('li:has(ul)');

                    $('#header').after($mobileMenu);
                    hasChildMenu.children('ul').hide();
                    hasChildMenu.children('a').after('<span class="btn-submenu"></span>');
                    $('.btn-menu').removeClass('active');
                } else {
                    var $desktopMenu = $('#mainnav-mobi').attr('id', 'mainnav').removeAttr('style');

                    $desktopMenu.find('.submenu').removeAttr('style');
                    $('#header').find('.nav-wrap').append($desktopMenu);
                    $('.btn-submenu').remove();
                }
            }
        });

        $('.btn-menu').on('click', function() {         
            $('#mainnav-mobi').slideToggle(300);
            $(this).toggleClass('active');
        });

        $(document).on('click', '#mainnav-mobi li .btn-submenu', function(e) {
            $(this).toggleClass('active').next('ul').slideToggle(300);
            e.stopImmediatePropagation()
        });
    }

    var headerFixed = function() {
        if ( $('body').hasClass('header-sticky') ) {
            var nav = $('.header');

            if ( nav.size() != 0 ) {
                var offsetTop = $('.header').offset().top,
                    headerHeight = $('.header').height(),
                    injectSpace = $('<div />', { height: headerHeight }).insertAfter(nav);   
                    injectSpace.hide();                 

                $(window).on('load scroll', function(){
                    if ( $(window).scrollTop() > 0 ) {
                        $('.header').addClass('header-fix');
                        injectSpace.show();
                    } else {
                        $('.header').removeClass('header-small header-fix');
                        injectSpace.hide();
                    }                    
                })
            }
        }     
    };
    
    var simpleSlider = function() { 
        if ( $().flexslider ) {
                $('.flexslider').flexslider({
                    animation      :  "slide",
                    direction      :  "horizontal", // vertical
                    pauseOnHover   :  true,
                    useCSS         :  false,
                    pausePlay      : false,
                    easing         :  "swing",
                    animationSpeed :  500,
                    slideshowSpeed :  5000,
                    controlNav     :  true,
                    directionNav   :  true,
                    slideshow      :  true,
                    prevText       :  '<i class="fa fa-angle-left"></i>',
                    nextText       :  '<i class="fa fa-angle-right"></i>',
                    smoothHeight   :  true
                }); // flexslider
           // }); // simple-slider
        }
    };

    var popupGallery = function () {
        $('.blog').each(function() {
            if ( $('a').hasClass('popup-gallery') ) {                
                 $(".popup-gallery").magnificPopup({
                    type: "image",
                    tLoading: "Loading image #%curr%...",
                    removalDelay: 600,
                    mainClass: "my-mfp-slide-bottom",
                    gallery: {
                        enabled: true,
                        navigateByImgClick: true,
                        preload: [ 0, 1 ]
                    },
                    image: {
                        tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
                    }
                });
            }
        }); 

        $('.gallery-grid' || '.images-shop-detail').each(function() {
            if ( $('a').hasClass('popup-gallery') ) {                
                 $(".popup-gallery").magnificPopup({
                    type: "image",
                    tLoading: "Loading image #%curr%...",
                    removalDelay: 600,
                    mainClass: "my-mfp-slide-bottom",
                    gallery: {
                        enabled: true,
                        navigateByImgClick: true,
                        preload: [ 0, 1 ]
                    },
                    image: {
                        tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
                    }
                });
            }
        });      
    }     

    var iconCanvasClick = function() {
        $('.off-canvas').on('click', function() { 
            if ($('.off-canvas').hasClass("canvas-show")  ) {
                $('body').removeClass('off-canvas-active');
                $(this).removeClass("canvas-show");
            } else {
                $(this).addClass('canvas-show');
                $('body').addClass('off-canvas-active');
            }
        });
    }

    var topSearch = function () {   

        $(document).on('click', function(e) {   
            var clickID = e.target.id;   
            if ( ( clickID != 's' ) ) {
                $('.search-box').removeClass('active');                
            } 
        });

        $('.search-box').on('click', function(event){
            event.stopPropagation();
        });

        $('.search-form').on('click', function(event){
            event.stopPropagation();
        });        

        $('.search-box').on('click', function () {
            if(!$('.search-box').hasClass( "active" ))
                $('.search-box').addClass('active');
            else
                $('.search-box').removeClass('active');
        });          
    }  

    var iconFilterClick = function() {
        $('.projects-filter-toggler').on('click', function() { 
            if ($('.controlnav-folio').hasClass("show")  ) {
                $('.controlnav-folio').removeClass("show");
            } else {
                $('.controlnav-folio').addClass('show');
            }
        });
    }

    var parallax = function() {
        if ( $().parallax && isMobile.any() == null ) {
            $('.parallax1').parallax("50%", 0.2);
            $('.parallax2').parallax("50%", 0.4);  
            $('.parallax3').parallax("50%", 0.5);
            $('.parallax4').parallax("50%", 0.5);  
            $('.parallax5').parallax("50%", 0.5);
            $('.parallax6').parallax("50%", 0.5); 
            $('.parallax7').parallax("50%", 0.5);             
        }
    };
    
    var Carousel_slider = function() {
        $('.slider-entry').each(function(){
            if ( $().owlCarousel ) {
                $(this).find('#flat-entry-carousel').owlCarousel({
                    loop: true,
                    margin: 30,
                    auto:true,
                    nav:true,
                    responsive:{
                        0:{
                            items: 1
                        },
                        767:{
                            items: 2
                        },
                        991:{
                            items: 2
                        }, 
                        1200:{
                            items: 3
                        }               
                    }
                });
            }
        });
    };

    var blogMasory = function() {         
        if ( $().isotope ) {           
            var $container = $('.wrap-entry-masonry');
            $container.imagesLoaded(function(){
                $container.isotope({
                    itemSelector: '.entry',
                    transitionDuration: '1s'
                });
            });           
            
        };
    };

    var Masonry_GalleryGrid = function() {         
        if ( $().isotope ) {           
            var $container = $('.project-gallery-wrap');
            $container.imagesLoaded(function(){
                $container.isotope({
                    itemSelector: '.project-item',
                    transitionDuration: '1s'
                });
            });           
            
        };
    };

    var projectIsotope = function() {
        if ( $().isotope ) {
            var $container = $('.project-wrap');

            $container.imagesLoaded(function(){
                $container.isotope({
                    itemSelector: '.project-item',
                    transitionDuration: '1s'
                });
            });

            $('.project-filter li').on('click',function() {
                var selector = $(this).find("a").attr('data-filter');
                $('.project-filter li').removeClass('active');
                $(this).addClass('active');
                $container.isotope({ filter: selector });
                return false;
            });
        };
    };

    var flatAnimation = function() {
        $('.flat-animation').each( function() {
            var el = $(this),
                rollClass  = el.data('animation'),
                rollDelay  = el.data('animation-delay'),
                rollOffset = el.data('animation-offset');

            el.css({
                '-webkit-animation-delay':  rollDelay,
                '-moz-animation-delay':     rollDelay,
                'animation-delay':          rollDelay
            });
            
            el.waypoint(function() {
                el.addClass('animated').addClass(rollClass);
            },{
                triggerOnce: true,
                offset: rollOffset
            });
        });
    };

    var ajaxContactForm = function() {  
        $('#contactform').each(function() {
            $(this).validate({
                submitHandler: function( form ) {
                    var $form = $(form),
                        str = $form.serialize(),
                        loading = $('<div />', { 'class': 'loading' });

                    $.ajax({
                        type: "POST",
                        url:  $form.attr('action'),
                        data: str,
                        beforeSend: function () {
                            $form.find('.send-wrap').append(loading);
                        },
                        success: function( msg ) {
                            var result, cls;                            
                            if ( msg == 'Success' ) {                                
                                result = 'Email Sent Successfully. Thank you, Your application is accepted - we will contact you shortly';
                                cls = 'msg-success';
                            } else {
                                result = 'Error sending email.';
                                cls = 'msg-error';
                            }

                            $form.prepend(
                                $('<div />', {
                                    'class': 'flat-alert ' + cls,
                                    'text' : result
                                }).append(
                                    $('<a class="close" href="#"><i class="fa fa-close"></i></a>')
                                )
                            );

                            $form.find(':input').not('.submit').val('');
                        },
                        complete: function (xhr, status, error_thrown) {
                            $form.find('.loading').remove();
                        }
                    });
                }
            });
        }); // each contactform
    };   

    var alertBox = function() {
        $(document).on('click', '.close', function(e) {
            $(this).closest('.flat-alert').remove();
            e.preventDefault();
        })     
    }  

    var WoocommerceSlider = function() {
        if( $().slider ) {
            $( ".price_slider" ).slider({
                range: true,
                min: 9,
                max: 35,
                values: [ 9, 35 ],
                slide: function( event, ui ) {
                    $( ".price_label > input " ).val( "£" + ui.values[ 0 ] + "  - £" + ui.values[ 1 ] );
                    }
            });

            $( ".price_label > input " ).val( "£" + $( ".price_slider" ).slider( "values", 0 ) +
            "  -  £" + $( ".price_slider" ).slider( "values", 1 ) );
            $( ".ui-slider-handle").append("<span class='shadow'></span>");
        }
    };

    var woocommerceTabs = function() {
        $('.woocommerce-tabs').each(function() {
           var content = $('.wc-tab');
            content.hide();
            if ( (content).hasClass("active")) {
                $('.wc-tab.active').show();
            } else {
                content.first().show();
            }                     
            $(this).find(' > ul > li').on('click',function(e) {                
                var hid = $(this).index();
                e.preventDefault();
                $(this).siblings().removeClass('active');
                $(this).addClass('active');
                var contentActive = $(this).parents('.tabs').siblings('.wc-tab').eq(hid);                
                content.not(':eq(hid)').hide();
                contentActive.fadeIn(300);                
            })
        });
    };

    var Flexslider_Images = function() {
        $('.justify-layout').each(function() {
           $('#flex-img-in-container').flexImages({rowHeight: 324});
        });

        $('.justify-layout.without').each(function() {
           $('#flex-img-out-container').flexImages({rowHeight: 400});
        });
    };

    var goTop = function() {
        $(window).scroll(function() {
            if ( $(this).scrollTop() > 800 ) {
                $('.go-top').addClass('show');
            } else {
                $('.go-top').removeClass('show');
            }
        }); 

        $('.go-top').on('click', function() {           
            $("html, body").animate({ scrollTop: 0 }, 1000 , 'easeInOutExpo');
            return false;
        });
    };  

    var removePreloader = function() {        
        $('.loader').fadeOut('slow',function () {
            $(this).remove();
        });
    };

   	// Dom Ready
	$(function() {         
        responsiveMenu();
        if ( matchMedia( 'only screen and (min-width: 991px)' ).matches ) {
            headerFixed();
        }   
        simpleSlider(); 
        popupGallery();
        topSearch();
        iconCanvasClick();
        iconFilterClick();
        Carousel_slider();
        parallax();
        blogMasory();
        Masonry_GalleryGrid();
        projectIsotope();
        flatAnimation();
        ajaxContactForm();
        alertBox();
        WoocommerceSlider();
        woocommerceTabs();
        Flexslider_Images();
        goTop();       
        removePreloader();
   	});

})(jQuery);
