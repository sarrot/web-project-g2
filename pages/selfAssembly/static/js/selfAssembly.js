let txt='馃馃崓馃崌 讛专讻讘 讗转 驻诇讟转 讛驻讬专讜转 砖诇讱  ';
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

function onlyOne(checkbox) {
    let checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
}