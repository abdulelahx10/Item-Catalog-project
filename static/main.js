function removeActive() {
    $('#list>li.active').removeClass('active')
};
$('#list>li').click(function () {
    removeActive()
    $(this).addClass('active')
});