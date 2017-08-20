$('.btn.add').click(function(){
    $('.errorlist').hide()
    $('.post-form').fadeIn()
    $(this).hide()
    $("html, body").animate({ scrollTop: $(document).height() }, 1000);
    $('.decline').show()
    $('.submitting').show()
    $('textarea').html('')
})



$('.controls.decline').click(function(){
    $(this).hide()
    $('.post-form').hide()
    $('.btn.add').fadeIn()

})