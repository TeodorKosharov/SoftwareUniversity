import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function detailsPage(context) {
    const clickedPostId = context.params.id;
    const clickedPost = await (await fetch(`http://localhost:3030/data/offers/${clickedPostId}`)).json();
    let detailsTemplate;

    if (JSON.parse(sessionStorage.userData).id === clickedPost._ownerId) {
        detailsTemplate = html`
            <section id="details">
                <div id="details-wrapper">
                    <img id="details-img" src="${clickedPost.imageUrl}" alt="example1" />
                    <p id="details-title">${clickedPost.title}</p>
                    <p id="details-category">
                        Category: <span id="categories">${clickedPost.category}</span>
                    </p>
                    <p id="details-salary">
                        Salary: <span id="salary-number">${clickedPost.salary}</span>
                    </p>
                    <div id="info-wrapper">
                        <div id="details-description">
                            <h4>Description</h4>
                            <span>${clickedPost.description}</span>
                        </div>
                        <div id="details-requirements">
                            <h4>Requirements</h4>
                            <span>${clickedPost.requirements}</span>
                        </div>
                    </div>
                    <p>Applications: <strong id="applications">1</strong></p>

                    <!--Edit and Delete are only for creator-->
                    <div id="action-buttons">
                        <a href="/edit/${clickedPostId}" id="edit-btn">Edit</a>
                        <a href="/delete/${clickedPostId}" id="delete-btn">Delete</a>
                    </div>
                </div>
            </section>
        `;
    }
    else {
        detailsTemplate = html`
            <section id="details">
                <div id="details-wrapper">
                    <img id="details-img" src="${clickedPost.imageUrl}" alt="example1" />
                    <p id="details-title">${clickedPost.title}</p>
                    <p id="details-category">
                        Category: <span id="categories">${clickedPost.category}</span>
                    </p>
                    <p id="details-salary">
                        Salary: <span id="salary-number">${clickedPost.salary}</span>
                    </p>
                    <div id="info-wrapper">
                        <div id="details-description">
                            <h4>Description</h4>
                            <span>${clickedPost.description}</span>
                        </div>
                        <div id="details-requirements">
                            <h4>Requirements</h4>
                            <span>${clickedPost.requirements}</span>
                        </div>
                    </div>
                    <p>Applications: <strong id="applications">1</strong></p>
                </div>
            </section>
        `;
    }

    render(detailsTemplate, document.querySelector('main'));
}
