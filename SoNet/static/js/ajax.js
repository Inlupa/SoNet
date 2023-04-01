//function getCookie(name) {
//    let cookieValue = null;
//    if (document.cookie && document.cookie !== '') {
//        const cookies = document.cookie.split(';');
//        for (let i = 0; i < cookies.length; i++) {
//            const cookie = cookies[i].trim();
//            // Does this cookie string begin with the name we want?
//            if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                break;
//            }
//        }
//    }
//    return cookieValue;
//}
//
//const csrftoken = getCookie('csrftoken');
//
//
//
//data = JSON.stringify({"tariff": "300", "price": "300" })
//
//fetch(url_ajax, {
//    method: 'POST',
//    headers: { 'Accept': 'application/json, text/plain, */*',
//        'Content-Type': 'application/json',
//        "X-CSRFToken": csrftoken },
//    body: JSON.stringify({"tariff": "300", "price": "300" })
//})
//.then(response => {
//        return response.json() //Convert response to JSON
//})

//$( document ).ready(function() {
//    console.log( "ready!" );
//});
var price = 300
var name = "Оптимальный"

// function myFunction() {
//    $.ajax({
//        type: "GET",
//        url: url_ajax,
//        data: {
//            "tariff": "Оптимальный",
//             "price": "300",
//        },
//        dataType: "json",
//    });
////    var price = 300
////    var name = "Оптимальный"
////    window.location = "http://127.0.0.1:8000/offer/internet+tv?tariff=" + name + "&price="+ price
//}

