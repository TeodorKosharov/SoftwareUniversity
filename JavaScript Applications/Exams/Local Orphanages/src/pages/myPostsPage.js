import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function myPostsPage() {
    const userId = JSON.parse(sessionStorage.userData).id;
    const userPosts = await (await fetch(`http://localhost:3030/data/posts?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`)).json();
    let myPostsTemplate;

    if (userPosts.length > 0) {
        myPostsTemplate = html`
            <section id="my-posts-page">
                <h1 class="title">My Posts</h1>
                <div class="my-posts">
                    ${userPosts.map(post => html`
                        <div class="post">
                            <h2 class="post-title">${post.title}</h2>
                            <img class="post-image" src="${post.imageUrl}" alt="Material Image">
                            <div class="btn-wrapper">
                                <a href="/dashboard/${post._id}" class="details-btn btn">Details</a>
                            </div>
                        </div>
                    `)}
                </div>
            </section>

        `;
    } else {
        myPostsTemplate = html`
            <section id="my-posts-page">
                <h1 class="title">My Posts</h1>
                <h1 class="title no-posts-title">You have no posts yet!</h1>
            </section>
        `;
    }

    render(myPostsTemplate, document.querySelector('main'));
}
