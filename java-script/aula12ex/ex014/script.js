function carregar() {
    var msg = window.document.getElementById("msg")
    var img = window.document.getElementById("imagem")
    var data = new Date()
    var hora = data.getHours()
    var minuto = data.getMinutes()
    msg.innerHTML = `Agora são ${hora}:${minuto} horas.`
    if (hora >= 0 && hora < 12) {
        // Bom dia!
        img.src = "fotomanha.png";
        document.body.style.background = "#f4dab9";
    } else if (hora >= 12 && hora < 18) {
        // Boa tarde!
        img.src = "fototarde.png";
        document.body.style.background = "#f29b7f";
    } else {
        // Boa note!
        img.src = "fotonoite.png";
        document.body.style.background = "#20405b"
    }
}