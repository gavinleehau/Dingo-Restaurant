 $(function(){
    khoimonan = $('.nhieumon').isotope({
        itemSelector: '.motmon',
        layoutMode: 'masonry'
    });
    
    khoimonan.imagesLoaded().progress( function() {
        khoimonan.isotope('layout');
    });

    $('.tieudect a').click(function(){
        dulieu = $(this).data('monan'); // lay du lieu ve data('abc')
        // console.log(dulieu); khối này để check trong console
        khoimonan.isotope({filter: dulieu})
        return false; //vô hiệu hóa thẻ a link
    })

    // new WOW().init();
})
$(function(){
  new WOW().init(); 
});