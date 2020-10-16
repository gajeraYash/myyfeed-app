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

    $("#user-input").keyup(function () {
        var user_search = $(this).val();
        if (!user_search) {                      //if it is blank. 
            $("#search-content").empty();
        } else {
            $.ajax({
                url: 'user/search',
                data: {
                    'user_search': user_search
                },
                dataType: 'html',
                success: function (data) {
                    $('#replaceable-content').html(data)
                }
            });
        }
    });
});