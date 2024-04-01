const form = document.querySelector('form');
const usuario = document.getElementById('user');
const nome = document.getElementById('nome');
const cpf = document.getElementById('cpf');
const email = document.getElementById('email');
const telefone = document.getElementById('telefone');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    checkForm();
})

usuario.addEventListener('blur', () => {
    checkUsuario();
})

nome.addEventListener('blur', () => {
    checkNome();
})

cpf.addEventListener('blur', () => {
    checkCpf();
})

email.addEventListener('blur', () => {
    checkEmail();
})

telefone.addEventListener('blur', () => {
    checkTelefone();
})

function checkUsuario() {
    usuarioValue = usuario.value;
    
    if(usuarioValue === '#'){
        errorInput(usuario, 'selecione um usuario');
    } else {
        usuario.parentElement.classList.remove('erro')
    }
}

function checkNome() {
    nomeValue = nome.value;
    
    if(nomeValue === ''){
        errorInput(nome, 'Insira um nome');
    } else {
        nome.parentElement.classList.remove('erro')
    }
}

function checkCpf() {
    cpfValue = cpf.value;
    
    if(cpfValue === '') {
        errorInput(cpf, 'Insira um cpf');
    } else if(isNaN(cpfValue) || cpfValue.length < 11){
        errorInput(cpf, 'insira um cpf válido')
    } else {
        cpf.parentElement.classList.remove('erro')
    }
}

function checkEmail() {
    const emailValue = email.value;

    if(emailValue === '') {
        errorInput(email, 'Insira um email');
    } else if(!(emailValue.includes("@")) || !(emailValue.includes(".com"))) {
        errorInput(email, 'insira um email válido')
    } else if(emailValue.startsWith('@')) {
        errorInput(email, 'insira um email válido')
    } else {
        email.parentElement.classList.remove('erro')
    }
}

function checkTelefone() {
    telefoneValue = telefone.value;
    telefoneValueLimpo = telefoneValue.replaceAll(' ', '')

    if(telefoneValue === '') {
        errorInput(telefone, 'Insira um telefone');
    } else if(isNaN(telefoneValueLimpo) || telefoneValueLimpo.length < 9){
        errorInput(telefone, 'insira um telefone válido')
    } else {
        telefone.parentElement.classList.remove('erro')
    }
}

function checkForm() {
    checkUsuario();
    checkNome();
    checkCpf();
    checkEmail();
    checkTelefone();

    formItens = form.querySelectorAll('.form-content');
    const notValid = [...formItens].some(item => item.classList.contains('erro'))
    
    if(notValid) {
        alert('Form Inválido')
    } else {
        form.submit();
    }
}


function errorInput(input, mensagem) {
    const formItem = input.parentElement;
    const textoErro = formItem.querySelector('span');

    textoErro.innerText = mensagem;
    formItem.classList.add('erro');
}