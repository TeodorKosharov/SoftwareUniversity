import page from '../node_modules/page/page.mjs';
import {homePage} from "./pages/homePage.js";
import {loginPage} from "./pages/loginPage.js";
import {registerPage} from "./pages/registerPage.js";
import {dashboardPage} from "./pages/dashboardPage.js";
import {createPage} from "./pages/createPage.js";
import {detailsPage} from "./pages/detailsPage.js";
import {editPage} from "./pages/editPage.js";

export function updateNavi() {
    if (sessionStorage.userData !== undefined) {
        document.querySelector('.user').style.display = 'block';
        document.querySelector('.guest').style.display = 'none';
    } else {
        document.querySelector('.user').style.display = 'none';
        document.querySelector('.guest').style.display = 'block';
    }
}

page('/', homePage);
page('/login', loginPage);
page('/register', registerPage);
page('/logout', loggingOut);
page('/dashboard', dashboardPage);
page('/dashboard/:id', detailsPage);
page('/addPair', createPage);
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
    page.redirect('/dashboard');
}

async function deleting(context) {
    const clickedShoesId = context.params.id;
    const choice = confirm('Delete the shoes?');
    if (choice) {
        await fetch(`http://localhost:3030/data/shoes/${clickedShoesId}`, {
            method: 'delete', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }
        });
        page.redirect('/dashboard');
    }
}
