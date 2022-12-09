import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

export async function editPage(context) {
    const clickedPostId = context.params.id;
    const clickedPost = await (await fetch(`http://localhost:3030/data/offers/${clickedPostId}`)).json();

    const editTemplate = (onSubmit) => html`
        <section id="edit">
            <div class="form">
                <h2>Edit Offer</h2>
                <form class="edit-form" @submit="${onSubmit}">
                    <input
                            type="text"
                            name="title"
                            id="job-title"
                            placeholder="Title"
                            value="${clickedPost.title}"
                    />
                    <input
                            type="text"
                            name="imageUrl"
                            id="job-logo"
                            placeholder="Company logo url"
                            value="${clickedPost.imageUrl}"
                    />
                    <input
                            type="text"
                            name="category"
                            id="job-category"
                            placeholder="Category"
                            value="${clickedPost.category}"
                    />
                    <textarea
                            id="job-description"
                            name="description"
                            placeholder="Description"
                            rows="4"
                            cols="50">${clickedPost.description}</textarea>
                    <textarea
                            id="job-requirements"
                            name="requirements"
                            placeholder="Requirements"
                            rows="4"
                            cols="50"
                    >${clickedPost.requirements}</textarea>
                    <input
                            type="text"
                            name="salary"
                            id="job-salary"
                            placeholder="Salary"
                            value="${clickedPost.salary}"
                    />
                    <button type="submit">post</button>
                </form>
            </div>
        </section>
    `;

    render(editTemplate(onSubmit), document.querySelector('main'));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const title = formData.get('title');
        const imageUrl = formData.get('imageUrl');
        const category = formData.get('category');
        const description = formData.get('description');
        const requirements = formData.get('requirements');
        const salary = formData.get('salary');
        event.target.reset();

        if (title === '' || imageUrl === '' || category === '' || description === '' || requirements === '' || salary === '') {
            return alert('All fields are required!');
        }
        await fetch(`http://localhost:3030/data/offers/${clickedPostId}`, {
            method: 'put', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }, body: JSON.stringify({title, imageUrl, category, description, requirements, salary})
        });
        page.redirect(`/details/${clickedPostId}`);
    }
}
