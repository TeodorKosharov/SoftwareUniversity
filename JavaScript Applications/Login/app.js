const [registerForm, loginForm] = document.querySelectorAll('form');
const logoutButton = document.getElementById('logoutBtn');
const detailsButton = document.getElementById('userDetails');
const infoDiv = document.getElementById('userInfo');

registerForm.addEventListener('submit', registration);
loginForm.addEventListener('submit', logging);
logoutButton.addEventListener('click', logout);
detailsButton.addEventListener('click', details);

const registerUrl = 'http://localhost:3030/users/register';
const loginUrl = 'http://localhost:3030/users/login';
const logoutUrl = 'http://localhost:3030/users/logout';
const detailsUrl = 'http://localhost:3030/users/me';

async function registration(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    const repeat = formData.get('repass');
    event.target.reset();

    if (email === '' || password === '' || repeat === '') {
        alert('Inputs must not be empty!');
        throw new Error('Inputs must not be empty!');
    }

    if (password !== repeat) {
        alert('Passwords do not match!');
        throw new Error('Passwords do not match!');
    }

    const response = await fetch(registerUrl, {
        method: 'post', headers: {
            'content-type': 'application/json'
        }, body: JSON.stringify({email, password})
    });

    if (response.ok === false) {
        const error = await response.json();
        alert(error.message);
        throw new Error(error.message);
    }

    infoDiv.style.display = 'none';
    const data = await response.json();
    const token = data.accessToken;
    sessionStorage.setItem('accessToken', token);
    alert('User registered successfully!');

}

async function logging(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    event.target.reset();

    const response = await fetch(loginUrl, {
        method: 'post', headers: {
            'content-type': 'application/json'
        }, body: JSON.stringify({email, password})
    });

    if (response.ok === false) {
        const error = await response.json();
        alert(error.message);
        throw new Error(error.message);
    }

    infoDiv.style.display = 'none';
    const data = await response.json();
    const token = data.accessToken;
    sessionStorage.setItem('accessToken', token);
    alert('Successful login!');

}

async function logout() {
    const token = sessionStorage.getItem('accessToken');

    if (token === null) {
        alert('There is no logged in user!');
        throw new Error('There is no logged in user!');
    }
    // Правим get заявка, за да излезем, понеже така е описано в документацията на сървъра.
    // В хедъра на заявката добавяме задължително 'X-Authorization': token, където token е токена от sessionStorage-а
    await fetch(logoutUrl, {
        method: 'get', headers: {
            'X-Authorization': token
        }
    });

    sessionStorage.clear();
    infoDiv.style.display = 'none';
    alert('User logout successfully!');
}

async function details() {
    const token = sessionStorage.getItem('accessToken');

    if (token === null) {
        alert('There is no logged in user!');
        throw new Error('There is no logged in user!');
    }

    const response = await fetch(detailsUrl, {
        method: 'get', headers: {
            'X-Authorization': token
        }
    });
    const data = await response.json();
    infoDiv.style.display = 'block';
    const [email, name] = infoDiv.children;
    email.textContent = `Email: ${data.email}`;
    // Username работи при дадените регистрирани потребители от документацията на сървъра
    // защото в response-а има ключ със стойност username, а ако ние ръчно регистрираме
    // потребител няма username в response-а, защото при заявката не го подаваме. Можем
    // да го подадем, но трябва за използваме регекси, за да извлечем името, което усложнява
    // задачата, което не е цел на това демо.
    name.textContent = `Username: ${data.username}`;
}


// Стъпки при удостоверяване на данни:
// ! Тези стъпки са съобразени спрямо изискванията на учебния сървър !
// 1. Регистрираме потребител, изпращайки POST заявка
// *** Ако имаме регистрирани потребители в сървъра можем да пропуснем стъпка 1 ***

// 2. Логваме потребителя, изпращайки POST заявка към сървъра
// Response-а на сървъра ще бъде съобразен с това дали има регистриран потребител с тези данни
// Ако НЯМА такъв потребител, response-а ще бъде error
// Ако ИМА такъв потребител, response-a ще съдържа данните на потребителя, вкл. и токена

// 3. Съхраняваме токена в sessionStorage или localStorage, след което го използваме
// за оторизирани заявки. Синтаксисът на хедъра е 'X-Authorization': token
