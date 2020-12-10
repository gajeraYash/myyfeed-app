function get_feed() {

    $.ajax({
        url: 'user/feed',
        type: "get",
        cache: true,
        data: {
            'feed_param': 'FOLLOWING'
        },
        dataType: 'html',
        success: function (data) {
            $('#feed-content').html(data)
        }
    });
    // 'feed_param': 'FOLLOWING'  Get USER Following Announcements
    // 'feed_param': ''  Get Self created announcements
    // 'feed_param': 'username'  Get Other user created announcements
}

function like(post_id) {
    $.ajax({
        url: 'post/like',
        type: "POST",
        cache: true,
        data: {
            'post_id': post_id, 'operation': 'like_submit',
        },
        dataType: 'json',
        success: function(response){
            console.log(response)
            console.log('LikeStatus', response.liked)
            get_feed()
        }
});
}
get_feed();

$(document).ready(function () {

    $('#likecall').click(function(){
        console.log("YOU LIKED!")
        
    })
    //extend the announcement box
    $('.announcementform').focus(function () {
        $(this).animate({ rows: 4 },);
    });
    
    //Every 5 seconds update the list of announcements
    setInterval(function () {
        get_feed();
    }, 50000);

    //Disable Line Break
    $(".announcementform").keydown(function (e) {
        if (e.keyCode == 13 && !e.shiftKey) {
            e.preventDefault();
        }
    });

    //User search function
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
                    $('#search-content').html(data)
                }
            });
        }
    });
});