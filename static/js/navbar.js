$(document).ready(function () {
  var last_scroll_top = 0;
  $(window).scroll(function () {
    var scroll_top = $(window).scrollTop();
    if (scroll_top <= 5) {
      $('#navbar').removeClass("nav-init")
    } else if (scroll_top > 5 && scroll_top < 250) {
      $('#navbar').addClass('nav-init');
    } else if (scroll_top < last_scroll_top) {
      $('#navbar').removeClass('nav-down').addClass(["nav-up", "nav-init"]);
    } else {
      $('#navbar').removeClass(["nav-up", "nav-init"]).addClass("nav-down");
    }
    last_scroll_top = scroll_top;
  });
});