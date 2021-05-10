function remove1 () {
     document.getElementById("product1").style.display="none";
 }
 function remove2 () {
     document.getElementById("product2").style.display="none";
 }
 let txt='לחץ על שלח הזמנה כדי להינות מפלטת הפירות החלומית שלכם ';
 let i=0;
function text() {
    if (i<txt.length ){}
    {
        document.getElementById("text").innerHTML += txt.charAt(i);
        i++;
        setTimeout(text,60);
    }
}
