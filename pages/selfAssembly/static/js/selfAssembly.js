let txt='🥝🍍🍇 הרכב את פלטת הפירות שלך  ';
 let i=0;


function text() {
    if (i<txt.length ){}
    {
        document.getElementById("text").innerHTML += txt.charAt(i);
        i++;
        setTimeout(text,60);
    }
}

function chosen(element) {
    document.getElementById("size1").style.backgroundColor ='white';
    document.getElementById("size2").style.backgroundColor ='white';
    document.getElementById("size3").style.backgroundColor ='white';
    document.getElementById("size4").style.backgroundColor ='white';
    document.getElementById("size5").style.backgroundColor ='white';
    document.getElementById("size6").style.backgroundColor ='white';
    element.style.backgroundColor ='dimgray';
}
