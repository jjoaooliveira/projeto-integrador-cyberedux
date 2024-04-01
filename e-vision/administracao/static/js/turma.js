const form = document.querySelector('form');
const disciplina = document.getElementById('disciplina');
const professor = document.getElementById('professor');
const ano = document.getElementById('ano');
const alunos = document.getElementById('alunos');
const periodo = document.getElementById('periodo');
const qtdVagas = document.getElementById('qtd_vagas');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    checkForm();
})

alunos.addEventListener('blur', () => {
    checkAlunos();
})

disciplina.addEventListener('blur', () => {
    checkDisciplina();
})

professor.addEventListener('blur', () => {
    checkProfessor();
})

periodo.addEventListener('blur', () => {
    checkPeriodo();
})

ano.addEventListener('blur', () => {
    checkAno();
})

qtdVagas.addEventListener('blur', () => {
    checkQtdVagas();
})


function checkQtdVagas() {
    const qtdVagasValue = qtdVagas.value;
    
    if(qtdVagasValue === ''){
        errorInput(ano, 'Campo ano não pode ser vazio');
    } else if(isNaN(qtdVagasValue)){
        errorInput(ano, 'Campo ano precisa ser um número');
    } else {
        qtdVagas.parentElement.classList.remove('erro')
    }
}

function checkAno() {
    const anoValue = ano.value;
    
    if(anoValue === ''){
        errorInput(ano, 'Campo ano não pode ser vazio');
    } else if(isNaN(anoValue)){
        errorInput(ano, 'Campo ano precisa ser um número');
    } else {
        ano.parentElement.classList.remove('erro')
    }
}

function checkPeriodo() {
    const periodoValue = periodo.value;
    
    if(periodoValue === ''){
        errorInput(periodo, 'Campo periodo não pode ser vazio');
    } else if(isNaN(periodoValue)){
        errorInput(periodo, 'Campo periodo precisa ser um número');
    } else {
        periodo.parentElement.classList.remove('erro')
    }
}

function checkProfessor() {
    const professorValue = professor.value;
    
    if(professorValue === '#'){
        errorInput(professor, 'Selecione um professor');
    } else {
        professor.parentElement.classList.remove('erro')
    }
}

function checkAlunos() {
    const alunosValue = alunos.value;
    
    if(alunosValue === ''){
        errorInput(alunos, 'Selecione ao menos um aluno');
    } else {
        alunos.parentElement.classList.remove('erro')
    }
}

function checkDisciplina() {
    const disciplinaValue = disciplina.value;
    
    if(disciplinaValue === '#'){
        errorInput(disciplina, 'Selecione uma disciplina');
    } else {
        disciplina.parentElement.classList.remove('erro')
    }
}

function checkForm() {
    checkAlunos();
    checkDisciplina();
    checkProfessor();
    checkPeriodo();
    checkAno();
    checkQtdVagas();

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