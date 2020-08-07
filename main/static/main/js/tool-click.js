$(document).ready(function () {
    // $('.tool').on('click', function () {
    //     $('.update-box ').css('opacity','1');
    //     $('.update-box ').css('position', 'unset');
       
    // });

    $('.tool').click(function () {
        $('.update-box ').toggleClass('active')
    })
       

    

    // function slideToggle() {
    //     $(".update-box").slideToggle(2000); // 窗簾效果的切換,點一下收,點一下開,參數可以無,參數說明同上
    // }
    // slideToggle()

    // $('.tool').toggle(
    //     function () { $(".update-box").css('opacity', '1'); },
    //     function () { $(".update-box").css('opacity', '0'); }
    // );
});

