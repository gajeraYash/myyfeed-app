var x = document.getElementsByClassName("alert");

setTimeout(function(){ 
    try {
        x[i].style.display = "none"; 
    }
    catch(err) {
        console.log("Login_Errors","Cleared");
    }
}, 5000);
