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