var lista = [];
let res = document.getElementById("saida");

function adicionar(num=0) {
    var tnum = document.getElementById("cnum");
    var n = Number(tnum.value);
    var pos = lista.indexOf(n)
    if (n < 1 || n > 100 || pos >= 0) {
        window.alert("Valor inválido ou já adicionado!");
    } else {
        var tab = document.getElementById("ctab");
        var item = document.createElement("option");
        item.text = `O número ${n} foi adicionado`;
        tab.appendChild(item);
        lista.push(n);
        res.innerHTML = ""
        tnum.value = ""
        tnum.focus()
    }
}

function analisar() {
    let total = lista.length;
    if (total == 0) {
        window.alert("Por favor adicione algum número antes de finalizar");
    } else {
        res.innerHTML = `<p>Ao todo, temos ${total} números cadastrados</p> <br/>`;
        let maior = 0;
        let menor = 0;
        for (let i = 0; i < total; i++) {
            if (i == 0) {
                maior = lista[i];
                menor = lista[i];
            } else if (lista[i] > maior) {
                maior = lista[i];
            } else if (lista[i] < menor) {
                menor = lista[i];
            }
        }
        res.innerHTML += `<p>O maior valor digitado foi ${maior}.</p> <br/>`;
        res.innerHTML += `<p>O menor valor digitado foi ${menor}.</p> <br/>`;
        soma = 0
        for(let i = 0; i < total; i++) {
            soma += lista[i];
        }
        res.innerHTML += `<p>A soma dos valores digitados é ${soma}.</p> <br/>`
        media = soma / total
        res.innerHTML += `<p>A média dos valores digitados é ${media}.</p>`
    }
    
}