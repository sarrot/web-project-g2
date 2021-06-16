// function remove1 () { //אם מסירים את הפריט מהסל
//      document.getElementById("product1").style.display="none";
//  }
//  function remove2 () { //אם מסירים את הפריט מהסל
//      document.getElementById("product2").style.display="none";
//  }
//  function remove3 () { //אם מסירים את הפריט מהסל
//      document.getElementById("product2").style.display="none";
//  }
//  function remove2 () { //אם מסירים את הפריט מהסל
//      document.getElementById("product2").style.display="none";
//  }
//  function remove2 () { //אם מסירים את הפריט מהסל
//      document.getElementById("product2").style.display="none";
//  }
//  function remove2 () { //אם מסירים את הפריט מהסל
//      document.getElementById("product2").style.display="none";
//  }
 let txt='לחץ על שלח הזמנה כדי להינות מפלטת הפירות החלומית שלכם😊😊';
 let i=0;
function text() { //פונקציה להופעת המשפט
    if (i<txt.length ){}
    {
        document.getElementById("text").innerHTML += txt.charAt(i);
        i++;
        setTimeout(text,60);
    }
}