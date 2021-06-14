function verificar() {
    var data = new Date()
    var ano  = data.getFullYear()
    var fano = document.getElementById("txtano")
    var res = document.getElementById("res")
    if (fano.value.length == 0 || fano.value > ano) {
        window.alert("ERRO! Verifique os dados e tente novamente!")
    } else {
        var fsex = document.getElementsByName("radsex")
        var idade = ano - Number(fano.value)
        var genero = ""
        var img = document.createElement("img")
        img.setAttribute("id", "foto")
        if (fsex[0].checked) {
            genero = "Homem"
            if (idade < 10) {
                img.setAttribute("src", "foto-bebe-m.png")
                img.setAttribute("width", "300px")
            } else if (idade < 21) {
                img.setAttribute("src", "foto-jovem-m.png")
                img.setAttribute("width", "300px")
            } else if (idade < 50) {
                img.setAttribute("src", "foto-adulto-m.png")
                img.setAttribute("width", "300px")
            } else {
                img.setAttribute("src", "foto-idoso-m.png")
                img.setAttribute("width", "300px")
            }
        } else if (fsex[1].checked) {
            genero = "Mulher"
            if (idade < 10) {
                img.setAttribute("src", "foto-bebe-f.png")
                img.setAttribute("width", "300px")
            } else if (idade < 21) {
                img.setAttribute("src", "foto-jovem-f.png")
                img.setAttribute("width", "300px")
            } else if (idade < 50) {
                img.setAttribute("src", "foto-adulto-f.png")
                img.setAttribute("width", "300px")
            } else {
                img.setAttribute("src", "foto-idoso-f.png")
                img.setAttribute("width", "300px")
            }
        }
        res.style.textAlign = "center"
        res.innerHTML = `Detectamos ${genero} com ${idade} anos. <br/>`
        res.appendChild(img)
    }
}