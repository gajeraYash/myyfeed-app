
$(document).ready(function () {
    $('.announcementform').focus(function () {
        $(this).animate({ rows: 4 },);
    });

    $("#user-input").keyup(function () {
        var user_search = $(this).val();
        if (!user_search) {                      //if it is blank. 
            $("#replaceable-content").empty();
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