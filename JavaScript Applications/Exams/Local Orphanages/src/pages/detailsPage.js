import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function detailsPage(context) {
    const clickedPostId = context.params.id;
    const clickedPost = await(await fetch(`http://localhost:3030/data/posts/${clickedPostId}`)).json();
    let detailsTemplate;

    if (sessionStorage.userData !== undefined && JSON.parse(sessionStorage.userData).id === clickedPost._ownerId) {
        detailsTemplate = html`
            <section id="details-page">
                <h1 class="title">Post Details</h1>

                <div id="container">
                    <div id="details">
                        <div class="image-wrapper">
                            <img src="${clickedPost.imageUrl}" alt="Material Image" class="post-image">
                        </div>
                        <div class="info">
                            <h2 class="title post-title">${clickedPost.title}</h2>
                            <p class="post-description">Description: ${clickedPost.description}</p>
                            <p class="post-address">Address: ${clickedPost.address}</p>
                            <p class="post-number">Phone number: ${clickedPost.phone}</p>
                            <p class="donate-Item">Donate Materials: 0</p>

                            <!--Edit and Delete are only for creator-->
                            <div class="btns">
                                <a href="/edit/${clickedPost._id}" class="edit-btn btn">Edit</a>
                                <a href="/deleting/${clickedPost._id}" class="delete-btn btn">Delete</a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        `;
    } else {
        detailsTemplate = html`
            <section id="details-page">
                <h1 class="title">Post Details</h1>
                <div id="container">
                    <div id="details">
                        <div class="image-wrapper">
                            <img src="${clickedPost.imageUrl}" alt="Material Image" class="post-image">
                        </div>
                        <div class="info">
                            <h2 class="title post-title">${clickedPost.title}</h2>
                            <p class="post-description">Description: ${clickedPost.description}</p>
                            <p class="post-address">Address: ${clickedPost.address}</p>
                            <p class="post-number">Phone number: ${clickedPost.phone}</p>
                            <p class="donate-Item">Donate Materials: 0</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        
        `;
    }

    render(detailsTemplate, document.querySelector('main'));
}
