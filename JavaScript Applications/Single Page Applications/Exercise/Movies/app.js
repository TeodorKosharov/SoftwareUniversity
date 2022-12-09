import {login} from './src/login.js';
import {register} from './src/register.js';

export function updateNavi() {
    if (sessionStorage.userData !== undefined) {
        document.querySelector('.nav-link[data-action="logout"]').style.display = 'block';
        document.querySelector('.nav-link[data-action="login"]').style.display = 'none';
        document.querySelector('.nav-link[data-action="register"]').style.display = 'none';
        document.getElementById('add-movie-button').style.display = 'block';
        document.getElementById('welcome-msg').textContent = `Welcome, ${JSON.parse(sessionStorage.userData).email}`;
    } else {
        document.querySelector('.nav-link[data-action="logout"]').style.display = 'none';
        document.querySelector('.nav-link[data-action="login"]').style.display = 'block';
        document.querySelector('.nav-link[data-action="register"]').style.display = 'block';
        document.getElementById('add-movie-button').style.display = 'none';
        document.getElementById('welcome-msg').textContent = `Welcome, guest`;
    }
}

export function updateSections(...sectionIds) {
    const allSections = Array.from(document.querySelectorAll('section'));
    allSections.forEach(s => {
        if (sectionIds.includes(s.id)) {
            s.style.display = 'block';
        } else {
            s.style.display = 'none';
        }
    });

}

updateNavi();

document.querySelector('.navbar-brand').addEventListener('click', () => {
    updateSections('home-page', 'add-movie-button', 'movie');
});

document.querySelector('a[data-action="login"]').addEventListener('click', () => {
    updateSections('form-login');
    login();
});

document.querySelector('a[data-action="register"]').addEventListener('click', () => {
    updateSections('form-sign-up');
    register();
});

document.querySelector('a[data-action="logout"]').addEventListener('click', async () => {
    await fetch('http://localhost:3030/users/logout', {
        method: 'get', headers: {
            'x-authorization': JSON.parse(sessionStorage.userData).token
        }
    });
    updateSections('form-login');
    sessionStorage.clear();
    updateNavi();
});
