function get_feed() {
    var username = window.location.pathname.split("/").pop();
    var params = {
        url: '/user/feed',
        type: "get",
        cache: true,
        data: {
            'feed_param': username
        },
        dataType: 'html',
        success: function (data) {
            $('#feed-content').html(data)
        }
    };
    if (username == 'profile'){
        // params.url = 'user/feed'
        params.data.feed_param = ''; 
    }
    console.log('DATA FOR:', params.data.feed_param);
    $.ajax(params);
    // 'feed_param': 'FOLLOWING'  Get USER Following Announcements
    // 'feed_param': ''  Get Self created announcements
    // 'feed_param': 'username'  Get Other user created announcements
}

function like(post_id) {
    $.ajax({
        url: '/post/like',
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


function follow_user(username) {
    
    var params = {
        url: 'follow/' + username,
        type: "get",
        cache: true,
        data: {
            'feed_param': username
        },
        dataType: 'html',
        success: function (data) {
            $('#feed-content').html(data)
        }
    };
    if (username == 'profile'){
        params.url = 'user/feed'
        params.data.feed_param = ''; 
    }
    console.log('DATA FOR:', params.data.feed_param);
    $.ajax(params);
}

$(document).ready(function () {
    get_feed();
});