// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target === document.getElementById('id01')) {
        document.getElementById('id01').style.display = "none";
    }
}

function fruitp4() {
    document.getElementById('id01').style.display='block'; // show the
    let par = mediaModal(); // check screen size
    let words ='<p>' +
                    par+ ':פלטה "מהפנט"- מרכיבים' +
                    '<br>'+
                    'תותים, ענבים, דובדבנים, קרמבולה,'+
                    '<br>'+
                    'מלון, אננס, קוקוס קלוי, פסיפלורה ' +
                    '<br>'+
                    'מחיר: 265 ש"ח' +
                '</p>';
    document.getElementById('modal_img').src="imageProject/plate4.jpg";
    document.getElementById('target').innerHTML = words;
}

function fruitp3() {
    document.getElementById('id01').style.display='block';
    let par = mediaModal(); // check screen size
    let words ='<p>' +
                    par+ ':פלטה "מרגש"- מרכיבים' +
                    '<br>'+
                    'קלמנטינה, ענבים, אננס, תאנים,'+
                    '<br>'+
                    'אגס, דובדבנים, קוקוס קלוי, תפוז ' +
                    '<br>'+
                    'מחיר: 290 ש"ח' +
                '</p>';
    document.getElementById('modal_img').src="imageProject/plate3.jpg";
    document.getElementById('target').innerHTML = words;
}

function fruitp1() {
    document.getElementById('id01').style.display='block';
    let par = mediaModal(); // check screen size
    let words ='<p>' +
                    par+ ':פלטה "מפנק"- מרכיבים' +
                    '<br>'+
                    'פסיפלורה, ענבים, אננס, תאנים,'+
                    '<br>'+
                    'תפוח,אגס, בונבונירות, ליצי ובקבוק יין' +
                    '<br>'+
                    'מחיר: 350 ש"ח' +
                '</p>';
    document.getElementById('modal_img').src="imageProject/plate1.jpg";
    document.getElementById('target').innerHTML = words;
}

function fruitp2() {
    document.getElementById('id01').style.display='block';
    let par = mediaModal(); // check screen size
    let words ='<p>' +
                    par+ ':פלטה "אקזוטי"- מרכיבים' +
                    '<br>'+
                    'אבטיח, ענבים, אננס, קיווי,'+
                    '<br>'+
                    'תפוח,אגס, תותים, ליצי ומלון' +
                    '<br>'+
                    'מחיר: 275 ש"ח' +
                '</p>';
    document.getElementById('modal_img').src="imageProject/plate2.jpg";
    document.getElementById('target').innerHTML = words;
}

function fruit2() {
    document.getElementById('id01').style.display='block';
    let par = mediaModal(); // check screen size
    let words ='<p>' +
                    par+  ':פלטה "משפחתי"- מרכיבים' +
                    '<br>'+
                    'אבטיח, ענבים, אננס, פסיפלורה,'+
                    '<br>'+
                    'תפוח,אגס, תותים, קרמבולה ופטל' +
                    '<br>'+
                    'מחיר: 250 ש"ח' +
                '</p>';
    document.getElementById('modal_img').src="imageProject/fruit2.jpg";
    document.getElementById('target').innerHTML = words;
}

function fruit5() {
    document.getElementById('id01').style.display='block';
    let par = mediaModal(); // check screen size
    let words = '<p>' +
                     par+ ':פלטה "זוגי"- מרכיבים' +
                    '<br>'+
                    'אבטיח, ענבים, קיווי, דובדבנים,'+
                    '<br>'+
                    'תמרים ממולאים, תותים, קרמבולה ופטל' +
                    '<br>'+
                    'מחיר: 300 ש"ח' +
                '</p>';
    document.getElementById('modal_img').src="imageProject/fruit5.jpg";
    document.getElementById('target').innerHTML = words;
}

function mediaModal(){  //check if it mobile screen size
    let mediaQuery = window.matchMedia('(min-width: 768px)')
    let  par = '<b style="font-size: 5vw">';
    if (mediaQuery.matches){
       par = '<b>';
    }
    return par;  // returns tag needed
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