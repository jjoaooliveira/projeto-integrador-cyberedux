const form = document.querySelector('form');
const presente = document.getElementById('presente');
const aluno = document.getElementById('aluno');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    checkForm();
})

aluno.addEventListener('blur', () => {
    checkAluno();
})

function checkAluno() {
    const alunoValue = aluno.value;

    if(alunoValue === '#'){
        errorInput(aluno, 'selecione um aluno');
    } else {
        aluno.parentElement.classList.remove('erro')
    }
    
}

function checkForm() {
    checkAluno();

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