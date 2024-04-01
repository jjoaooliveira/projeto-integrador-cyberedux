const form = document.querySelector('form');
const nome = document.getElementById('nome');
const cpf = document.getElementById('cpf');
const email = document.getElementById('email');
const telefone = document.getElementById('telefone');
const condicaoFinanceira = document.getElementById('condicao_financeira');
const escolaridade = document.getElementById('escolaridade');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    checkForm();
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

condicaoFinanceira.addEventListener('blur', () => {
    checkCondicaoFinanceira();
})

escolaridade.addEventListener('blur', () => {
    checkEscolaridade();
})


function checkNome() {
    const nomeValue = nome.value;
    
    if(nomeValue === ''){
        errorInput(nome, 'Insira um nome');
    } else {
        nome.parentElement.classList.remove('erro')
    }
}

function checkEscolaridade() {
    const escolaridadeValue = escolaridade.value;

    if(escolaridadeValue === '#'){
        errorInput(escolaridade, 'selecione uma escolaridade');
    } else {
        escolaridade.parentElement.classList.remove('erro')
    }
    
}

function checkCondicaoFinanceira() {
    const condicaoFinanceiraValue = condicaoFinanceira.value;

    if(condicaoFinanceiraValue === '#'){
        errorInput(condicaoFinanceira, 'selecione uma condição financeira');
    } else {
        condicaoFinanceira.parentElement.classList.remove('erro')
    }
    
}

function checkCpf() {
    const cpfValue = cpf.value;
    
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
    const telefoneValue = telefone.value;
    const telefoneValueLimpo = telefoneValue.replaceAll(' ', '')

    if(telefoneValue === '') {
        errorInput(telefone, 'Insira um telefone');
    } else if(isNaN(telefoneValueLimpo)){
        errorInput(telefone, 'insira um telefone válido')
    } else if(telefoneValueLimpo.length < 9 || telefoneValueLimpo.length > 11){
        errorInput(telefone, 'telefone deve ter 11 numeros')
    } else {

        telefone.parentElement.classList.remove('erro')
    }
}

function checkForm() {
    checkNome();
    checkCpf();
    checkEmail();
    checkTelefone();

    const formItens = form.querySelectorAll('.form-content');
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