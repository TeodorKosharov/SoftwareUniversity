import page from '../node_modules/page/page.mjs';
import {loginPage} from "./pages/loginPage.js";
import {registerPage} from "./pages/registerPage.js";
import {dashboardPage} from "./pages/dashboardPage.js";
import {details} from "./pages/detailsPage.js";
import {addingBook} from "./pages/createPage.js";
import {editPage} from "./pages/editPage.js";
import {myBooksPage} from "./pages/myBooksPage.js";

export function updateNavi() {
    if (sessionStorage.userData !== undefined) {
        document.querySelector('#guest').style.display = 'none';
        document.querySelector('#user').style.display = 'block';
        document.querySelector('#user span').textContent = `Welcome, ${JSON.parse(sessionStorage.userData).email}`;
    } else {
        document.querySelector('#guest').style.display = 'block';
        document.querySelector('#user').style.display = 'none';
    }
}

page('/login', loginPage);
page('/register', registerPage);
page('/logout', loggingOut);
page('/dashboard', dashboardPage);
page('/dashboard/:id', details);
page('/edit/:id', editPage);
page('/deleting/:id', deleteBook);
page('/addBook', addingBook);
page('/myBooks', myBooksPage)
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
    page.redirect('/dashboard');
}

async function deleteBook(context) {
    const choice = confirm('Delete the book?');
    if (choice) {
        const clickedBookId = context.params.id;
        await fetch(`http://localhost:3030/data/books/${clickedBookId}`, {
            method: 'delete',
            headers: {
                'content-type': 'application/json',
                'x-authorization': JSON.parse(sessionStorage.userData).token
            }
        });
    }
    page.redirect('/dashboard');
}
