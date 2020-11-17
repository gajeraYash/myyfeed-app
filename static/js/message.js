$(document).ready(function () {
    $("#user-input").keyup(function () {
        var msg_user = $(this).val();
        if (!msg_user) {                      //if it is blank. 
            $("#search-content").empty();
        } else {
            $.ajax({
                url: 'message/search',
                data: {
                    'msg_user': msg_user
                },
                dataType: 'html',
                success: function (data) {
                    $('#search-content').html(data)
                }
            });
        }
    });
});
