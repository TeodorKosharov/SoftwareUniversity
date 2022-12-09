import {render} from '../node_modules/lit-html/lit-html.js';
import {logout} from "./api/api.js";
import {getUserData} from "./util.js";
import page from '../node_modules/page/page.mjs';
import {loginPage} from "./views/login.js";
import {registerPage} from './views/register.js';
import {homePage} from "./views/home.js";
import {createPage} from "./views/create.js";
import {myBooksPage} from "./views/my-books.js";
import {searchPage} from "./views/search.js";
import {detailsPage} from "./views/details.js";

const root = document.getElementById('site-content');

// middleware function:
// context идва от метода page автоматично
function decorateContext(context, next) {
    context.render = (content) => render(content, root);
    context.updateUserNav = updateUserNav
    next();
}

export function updateUserNav() {
    const userData = getUserData();

    if (userData) {
        document.getElementById('user').style.display = 'inline-block';
        document.getElementById('guest').style.display = 'none';
        document.querySelector('#user span').textContent = `Welcome ${userData.email}`;
    } else {
        document.getElementById('guest').style.display = 'inline-block';
        document.getElementById('user').style.display = 'none';
    }
}

document.getElementById('logoutBtn').addEventListener('click', (e) => {
    logout();
    updateUserNav();
    page.redirect('/');
})

page(decorateContext);
page('/', homePage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/mybooks', myBooksPage);
page('/search', searchPage);
page('/details/:id', detailsPage);
updateUserNav();
page.start();
