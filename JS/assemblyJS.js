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