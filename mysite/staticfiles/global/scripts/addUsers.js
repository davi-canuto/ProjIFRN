function addNewUser() {
    const nameUser = document.getElementById('id_user').value;
    const nameFunc = document.getElementById('nameFunc').value;

    const usersContainer = document.getElementById('users');
    const inputsContainer = document.getElementById('inputs-hidden')

    const newUserElement = document.createElement('div');
    newUserElement.classList.add('user-func-box'); // Adiciona a classe 'user' à div principal do usuário

    const nameElement = document.createElement('div');
    nameElement.textContent = `${nameUser}`;
    nameElement.classList.add('div-user'); // Adiciona a classe 'user-name' à div do nome do usuário

    const funcElement = document.createElement('div');
    funcElement.textContent = `${nameFunc}`;
    funcElement.classList.add('div-function'); // Adiciona a classe 'user-function' à div da função do usuário

    newUserElement.appendChild(nameElement);
    newUserElement.appendChild(funcElement);
    usersContainer.appendChild(newUserElement);

    const newInputUser = document.createElement('input');
    newInputUser.setAttribute('type', 'text');
    newInputUser.setAttribute('name', 'user_and_function');
    newInputUser.setAttribute('hidden', 'true');
    newInputUser.value = `${nameUser}-${nameFunc}`
    inputsContainer.appendChild(newInputUser);
    


    document.getElementById('id_user').value = '';
    document.getElementById('nameFunc').value = '';
}







