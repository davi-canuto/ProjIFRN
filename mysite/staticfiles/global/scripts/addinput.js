function addNewInput(id_input) {
    const inputContainer = document.getElementById(id_input);
    const newInput = document.createElement('input');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('name', 'keyword');
    inputContainer.appendChild(newInput);
}





