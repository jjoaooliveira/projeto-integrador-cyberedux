const form = document.querySelector('form');
const data = document.getElementById('data');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    checkForm();
})

data.addEventListener('blur', () => {
    checkData();
})

function checkData() {
    const dataValue = data.value;

    if(dataValue === ''){
        errorInput(data, 'defina uma data');
    } else {
        data.parentElement.classList.remove('erro')
    }
    
}

function checkForm() {
    checkData();

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