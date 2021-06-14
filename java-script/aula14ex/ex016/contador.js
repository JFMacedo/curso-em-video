function contar() {
    var ini = document.getElementById("inicio")
    var fim = document.getElementById("fim")
    var pas = document.getElementById("passo")
    var res = document.getElementById("saida")
    var i = Number(ini.value)
    var f = Number(fim.value)
    var p = Number(pas.value)    
    if (ini.value.length == 0 || fim.value.length == 0 || pas.value.length == 0) {
        res.innerHTML = "Impossivel contar!"
    } else {
        res.innerHTML = "Contando... <br/>"
        if (p == 0) {
            window.alert("Passo inválido... Considerando PASSO 1")
            p = 1
        }
        if (i < f) {
            for (var c = i; c <= f; c += p) {
                res.innerHTML += `${c} \u{1F449} `
            }
        } else {
            for (var c = i; c >= f; c -= p) {
                res.innerHTML += `${c} \u{1F449} `
            }
        }
        res.innerHTML += `\u{1F3C1}`
    }
}