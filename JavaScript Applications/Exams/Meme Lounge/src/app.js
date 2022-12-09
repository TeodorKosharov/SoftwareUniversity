import page from '../node_modules/page/page.mjs';
import {logging} from "./pages/loginPage.js";
import {registering} from "./pages/registerPage.js";
import {homePage} from "./pages/homePage.js";
import {showMemes} from "./pages/allMemesPage.js";
import {createPage} from "./pages/createPage.js";
import {details} from "./pages/detailsPage.js";
import {editPage} from "./pages/editPage.js";
import {profilePage} from "./pages/profilePage.js";

export function updateNavi() {
    if (sessionStorage.userData !== undefined) {
        document.querySelector('.user').style.display = 'block';
        document.querySelector('.guest').style.display = 'none';
        document.querySelector('.profile span').textContent = `Welcome, ${JSON.parse(sessionStorage.userData).email}`;
    } else {
        document.querySelector('.user').style.display = 'none';
        document.querySelector('.guest').style.display = 'block';
    }
}

page('/', homePage);
page('/login', logging);
page('/register', registering);
page('/logout', loggingOut);
page('/memes', showMemes);
page('/memes/:id', details);
page('/create', createPage);
page('/edit/:id', editPage);
page('/profile', profilePage);
updateNavi();
page.start();

async function loggingOut() {
    await fetch('http://localhost:3030/users/logout', {
        method: 'get',
        headers: {
            'Content-Type': 'application/json',
            'x-authorization': JSON.parse(sessionStorage.userData).token
        }
    });
    sessionStorage.clear();
    updateNavi();
    page.redirect('/');
}
