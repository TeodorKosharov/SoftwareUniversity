import page from '../node_modules/page/page.mjs';
import {loginPage} from "./pages/loginPage.js";
import {registerPage} from "./pages/registerPage.js";
import {dashboardPage} from "./pages/dashboardPage.js";
import {detailsPage} from "./pages/detailsPage.js";
import {editPage} from "./pages/editPage.js";
import {createPage} from "./pages/createPage.js";
import {myPostsPage} from "./pages/myPostsPage.js";

export function updateNavi() {
    if (sessionStorage.userData !== undefined) {
        document.getElementById('user').style.display = 'block';
        document.getElementById('guest').style.display = 'none';
    } else {
        document.getElementById('user').style.display = 'none';
        document.getElementById('guest').style.display = 'block';
    }
}

page('/', dashboardPage);
page('/login', loginPage);
page('/register', registerPage);
page('/logout', loggingOut);
page('/dashboard', dashboardPage);
page('/dashboard/:id', detailsPage);
page('/deleting/:id', deletingPost);
page('/edit/:id', editPage);
page('/create', createPage);
page('/myPosts', myPostsPage);
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
    page.redirect('/');
}

async function deletingPost(context) {
    const clickedPostId = context.params.id;
    const choice = confirm('Delete the post?');
    if (choice) {
        await fetch(`http://localhost:3030/data/posts/${clickedPostId}`, {
            method: 'delete', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }
        });
        page.redirect('/dashboard');
    }
}
