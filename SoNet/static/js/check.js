const v = document.getElementById("id_tariff_info");

let inputs = document.getElementsByClassName("check");

for (var i = 0; i < inputs.length; i++){
            inputs[i].onchange = checkboxHandler;
 }

function checkboxHandler(e) {

       for (let i = 0; i < inputs.length; i++){

          if (inputs[i].checked && inputs[i] !== this){
             inputs[i].checked = false;
             inputs[i].nextElementSibling.innerHTML = "Выбрать";
             }

          if (inputs[i].checked){
             v.value =  "Заявка интернет + ТВ "+ inputs[i].name + " " + inputs[i].value;
             document.getElementById('stoimost').innerHTML = "";
             document.getElementById('stoimost').innerHTML = "Стоимость равна: "+ inputs[i].value;
             inputs[i].nextElementSibling.innerHTML = "Выбран";
          }

       }
}