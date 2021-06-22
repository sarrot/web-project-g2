

function validUS() {
    let num = document.getElementById("cardNumber").value;
    let date = document.getElementById("date").value;
    let cvv = document.getElementById("cvv").value;
    const re =/^[0-9]{3}$/;
    var regex = new RegExp("^[0-9]{16}$");
    var ra =/^(0[1-9]|1[0-2])\/\d{2}$/;
    let myArray = re.exec(cvv);

    if (!regex.test(num)) {
        alert("הכנס מספר אשראי בעל 16 ספרות");
        return false;
    }
    else {
        if(!ra.test(date)){
             alert("הוכנס תאריך לא נכון");
             return false;
        }
        else{
            if(cvv!=myArray) {
                alert(" לא תקין cvv "); //invalid cvv number
                return false;
             }
            else{
                return true;  //valid cvv number
            }

        }

    }

}
