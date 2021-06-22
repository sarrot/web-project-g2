// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target === document.getElementById('id01')) {
        document.getElementById('id01').style.display = "none";
        window.location.href='/homepage'
    }
}

let txt='מגשים מומלצים';
 let i=0;
function text() {   //inside letters animation
    if (i<txt.length ){}
    {
        document.getElementById("text").innerHTML += txt.charAt(i);
        i++;
        setTimeout(text,80);
    }
}

function back(){
     window.location.href='/homepage'
    document.getElementById('id01').style.display='none'
}
