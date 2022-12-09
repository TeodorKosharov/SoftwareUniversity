import {html, render} from '../../node_modules/lit-html/lit-html.js';

let profileTemplate;
let userId;
let userMemes = [];

if (sessionStorage.userData !== undefined) {
    userId = JSON.parse(sessionStorage.userData).id;
    userMemes = await (await fetch(`http://localhost:3030/data/memes?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`)).json();
}

export async function profilePage() {
    const gender = JSON.parse(sessionStorage.userData).gender;

    if (userMemes.length === 0) {
        if (gender === 'female') {
            profileTemplate = (user) => html`
                <section id="user-profile-page" class="user-profile">
                    <article class="user-info">
                        <img id="user-avatar-url" alt="user-profile" src="/images/female.png">
                        <div class="user-content">
                            <p>Username: ${user.username}</p>
                            <p>Email: ${user.email}</p>
                            <p>My memes count: ${userMemes.length}</p>
                        </div>
                    </article>
                    <h1 id="user-listings-title">User Memes</h1>
                    <div class="user-meme-listings">
                        <p class="no-memes">No memes in database.</p>
                    </div>
                </section>
            `;
        }
        else {
            {
                profileTemplate = (user) => html`
                    <section id="user-profile-page" class="user-profile">
                        <article class="user-info">
                            <img id="user-avatar-url" alt="user-profile" src="/images/male.png">
                            <div class="user-content">
                                <p>Username: ${user.username}</p>
                                <p>Email: ${user.email}</p>
                                <p>My memes count: ${userMemes.length}</p>
                            </div>
                        </article>
                        <h1 id="user-listings-title">User Memes</h1>
                        <div class="user-meme-listings">
                            <p class="no-memes">No memes in database.</p>
                        </div>
                    </section>
                `;
            }
        }
    }
    else {
        if (gender === 'female') {
            profileTemplate = (user) => html`
                <section id="user-profile-page" class="user-profile">
                    <article class="user-info">
                        <img id="user-avatar-url" alt="user-profile" src="/images/female.png">
                        <div class="user-content">
                            <p>Username: ${user.username}</p>
                            <p>Email: ${user.email}</p>
                            <p>My memes count: ${userMemes.length}</p>
                        </div>
                    </article>
                    <h1 id="user-listings-title">User Memes</h1>
                    <div class="user-meme-listings">
                        <!-- Display : All created memes by this user (If any) -->
                        <div class="user-meme">
                            ${userMemes.map(meme => html`
                                <p class="user-meme-title">${meme.title}</p>
                                <img class="userProfileImage" alt="meme-img" src="${meme.imageUrl}">
                                <a class="button" href="/memes/${meme._id}">Details</a>
                            `)}
                        </div>
                    </div> 
                </section>
            `;
        }
        else {
            profileTemplate = (user) => html`
                <section id="user-profile-page" class="user-profile">
                    <article class="user-info">
                        <img id="user-avatar-url" alt="user-profile" src="/images/male.png">
                        <div class="user-content">
                            <p>Username: ${user.username}</p>
                            <p>Email: ${user.email}</p>
                            <p>My memes count: ${userMemes.length}</p>
                        </div>
                    </article>
                    <h1 id="user-listings-title">User Memes</h1>
                    <div class="user-meme-listings">
                        <div class="user-meme">
                            ${userMemes.map(meme => html`
                                <p class="user-meme-title">${meme.title}</p>
                                <img class="userProfileImage" alt="meme-img" src="${meme.imageUrl}">
                                <a class="button" href="/memes/${meme._id}">Details</a>
                            `)}
                        </div>
                    </div> 
                </section>
            `;
        }
    }

    render(profileTemplate(JSON.parse(sessionStorage.userData)), document.querySelector('main'));
}