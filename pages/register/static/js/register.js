function text() {
}

// registration valid
function validUS() {
    let firstpassword=document.getElementById("psw").value;
    let secondpassword=document.getElementById("psw_repeat").value;
    let validEmail = document.getElementById("email").value;
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if(firstpassword==secondpassword){
        if(re.test(String(validEmail).toLowerCase())){
        return true;
        }
        else{
          alert("email is not valid");
          return false;
        }
    }
    else{
        if(re.test(String(validEmail).toLowerCase())) {
            alert("password must be same!");
            return false;
        }
        else{
             alert("wrong details!");
        }
    }
}

