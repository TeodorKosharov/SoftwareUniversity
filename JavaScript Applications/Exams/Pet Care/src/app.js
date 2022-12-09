import page from '../node_modules/page/page.mjs';
import {loginPage} from "./pages/loginPage.js";
import {registerPage} from "./pages/registerPage.js";
import {homePage} from "./pages/homePage.js";
import {dashboardPage} from "./pages/dashboardPage.js";
import {createPage} from "./pages/createPage.js";
import {detailsPage} from "./pages/detailsPage.js";
import {editPage} from "./pages/editPage.js";

export function updateNavi() {
    if (sessionStorage.userData !== undefined) {
        document.querySelector('a[href="/login"]').style.display = 'none';
        document.querySelector('a[href="/register"]').style.display = 'none';
        document.querySelector('a[href="/create"]').style.display = 'block';
        document.querySelector('a[href="/logout"]').style.display = 'block';
    } else {
        document.querySelector('a[href="/login"]').style.display = 'block';
        document.querySelector('a[href="/register"]').style.display = 'block';
        document.querySelector('a[href="/create"]').style.display = 'none';
        document.querySelector('a[href="/logout"]').style.display = 'none';
    }
}

page('/', homePage);
page('/login', loginPage);
page('/register', registerPage);
page('/logout', loggingOut);
page('/home', homePage);
page('/dashboard', dashboardPage);
page('/dashboard/:id', detailsPage);
page('/create', createPage);
page('/edit/:id', editPage);
page('/delete/:id', deleting);
updateNavi();
page.start();

async function loggingOut() {
    await fetch('http://localhost:3030/users/logout', {
        method: 'get', headers: {
            'Content-Type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
        }
    });
    sessionStorage.clear();
    updateNavi();
    page.redirect('/home');
}

async function deleting(context) {
    const clickedPetId = context.params.id;
    const choice = confirm('Delete the post?');
    if (choice) {
        await fetch(`http://localhost:3030/data/pets/${clickedPetId}`, {
            method: 'delete', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }
        });
        page.redirect('/');
    }
}
