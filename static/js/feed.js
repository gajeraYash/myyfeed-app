constrainInput = (event) => {
    event.target.value = event.target.value.replace(/[\r\n\v]+/g, '')
}

document.querySelectorAll('textarea').forEach(el => {
    el.addEventListener('keyup', constrainInput)
})




$(document).ready(function () {
    $('.announcementform').focus(function () {
        $(this).animate({rows: 4},);
    });
    console.log("Feed.js")
  });