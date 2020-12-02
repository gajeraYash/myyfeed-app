var x = document.getElementsByClassName("alert");

setTimeout(function(){ 
    try {
        x[i].style.display = "none"; 
    }
    catch(err) {
        console.group();
        console.log("Login_Errors","Cleared");
        console.groupEnd();
    }
}, 5000);
