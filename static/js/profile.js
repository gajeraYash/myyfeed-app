function get_feed() {
    $.ajax({
        url: 'user/feed',
        type: "get",
        cache: true,
        dataType: 'html',
        success: function (data) {
            $('#feed-content').html(data)
        }
    });
}

get_feed();

$(document).ready(function () {
    $('.announcementform').focus(function () {
        $(this).animate({ rows: 4 },);
    });

    setInterval(function () {
        get_feed();
    }, 50000);

});