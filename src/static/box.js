$('.main').hover(function() {
    $(this).animate({
        width: '500px'
    }, 300);
}, function() {
    $(this).animate({
        width: '200px'
    }, 300);
});
