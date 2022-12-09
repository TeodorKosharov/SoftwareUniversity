import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function dashboardPage() {
    const posts = await (await fetch('http://localhost:3030/data/posts?sortBy=_createdOn%20desc')).json();
    let dashboardTemplate;

    if (posts.length > 0) {
        dashboardTemplate = (posts) => html`
            <section id="dashboard-page">
                <h1 class="title">All Posts</h1>
                <div class="all-posts">
                    ${posts.map(post => html`
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
        dashboardTemplate = (posts) => html`
            <section id="dashboard-page">
                <h1 class="title">All Posts</h1>
                <h1 class="title no-posts-title">No posts yet!</h1>
            </section>
        `;
    }

    render(dashboardTemplate(posts), document.querySelector('main'));
}
