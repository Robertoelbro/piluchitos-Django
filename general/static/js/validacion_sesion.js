const form = document.getElementById("form");
const email = document.getElementById("correo");
const pass = document.getElementById("contraseña");
const submitBtn = document.getElementById("submitBtn");

submitBtn.addEventListener("click", function() {
    let entrar = false;
    const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
    let alertShown = false;

    if (!regexEmail.test(email.value)) {
        if (!alertShown) {
            alert("El email no es valido");
            alertShown = true;
        }
        entrar = true;
    }

    if (email.value.trim() === "") {
        if (!alertShown) {
            alert("Por favor, ingrese su correo electrónico");
            alertShown = true;
        }
        entrar = true;
    }
    if (pass.value.trim() === "") {
        if (!alertShown) {
            alert("Por favor, ingrese su contraseña");
            alertShown = true;
        }
        entrar = true;
    }
    if (pass.value.length < 8) {
        if (!alertShown) {
            alert("La contraseña debe tener al menos 8 caracteres");
            alertShown = true;
        }
        entrar = true;
    }
    if (entrar) {
    } else {
        window.location.href = "i1.html";
    }
});
