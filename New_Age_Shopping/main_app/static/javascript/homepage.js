// Product slider
$('.prdouctSlider').slick({
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 6,
    slidesToScroll: 2,
    prevArrow: '<span class="prev_arrow" style="position: absolute; font-size: 25px; bottom: 50%; z-index:1; left: -32px; display: inline-block;"><i class="fas fa-chevron-circle-left"></i></span>',
    nextArrow: '<span class="next_arrow" style="position: absolute; font-size: 25px; bottom: 50%; z-index:1; right: -32px; display: inline-block;"><i class="fas fa-chevron-circle-right"></i></span>',
    responsive: [
      {
        breakpoint: 1024,
        settings: {
            slidesToShow: 4,
            slidesToScroll: 2,
            infinite: true,
        }
      },
      {
        breakpoint: 600,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });