const form = document.querySelector('form');
const username = document.getElementById('username');
const nome = document.getElementById('first_name');
const sobrenome = document.getElementById('last_name');
const senha = document.getElementById('password1');
const senhaConfirmacao = document.getElementById('password2');
const email = document.getElementById('email');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    checkForm();
})

username.addEventListener('blur', () => {
    checkUsername();
})

senha.addEventListener('blur', () => {
    checkSenha();
})

senhaConfirmacao.addEventListener('blur', () => {
    checkSenhaConfirmacao();
})
email.addEventListener('blur', () => {
    checkEmail();
})

function checkUsername() {
    const usernameValue = username.value;
    
    if(usernameValue === ''){
        errorInput(username, 'Insira um nome de usuario');
    } else {
        username.parentElement.classList.remove('erro')
    }
}

function checkSenha() {
    const senhaValue = senha.value;
    
    if(senhaValue === '') {
        errorInput(senha, 'Insira uma senha');
    } else if(senhaValue.length < 8){
        errorInput(senha, 'a senha deve ter pelo menos 8 caracteres')
    } else if(!isNaN(senhaValue)){
        errorInput(senha, 'a senha não pode ser inteiramente números')
    } else {
        senha.parentElement.classList.remove('erro')
    }
}

function checkSenhaConfirmacao() {
    const senhaConfirmacaoValue = senhaConfirmacao.value;
    const senhaValue = senha.value;
    if(senhaConfirmacaoValue === '') {
        errorInput(senhaConfirmacao, 'insira a mesma senha digitada acima');
    }
    else if(senhaValue !== senhaConfirmacaoValue) {
        errorInput(senhaConfirmacao, 'As senhas devem ser iguais');
    } else {
        senhaConfirmacao.parentElement.classList.remove('erro')
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

function checkForm() {
    checkSenha();
    checkSenhaConfirmacao();
    checkUsername();
    checkEmail();

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