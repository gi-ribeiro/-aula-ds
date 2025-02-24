const btn = document.getElementsByClassName('calc');

function calculo(){
    const peso = document.getElementById('peso').value;
    const altura = document.getElementById('altura').value;
    const resul = document.getElementsByClassName('res');

    const calculo = peso / (altura * altura);
    resul.innerHTML= calculo.toFixed(2);
}

btn.addEventListener("click" , click)
