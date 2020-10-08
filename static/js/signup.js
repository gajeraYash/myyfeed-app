var x = document.getElementsByClassName("alert");

setTimeout(function(){ 
    try {
        for (i = 0; i < 2; i++) {
            x[i].style.display = "none"; 
        }
    }
    catch(err) {
        console.log("Signup_Errors","Cleared");
    }
}, 5000);
