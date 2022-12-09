import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

const createTemplate = (onSubmit) => html`
    <section id="create">
        <div class="form">
            <h2>Create Offer</h2>
            <form class="create-form" @submit="${onSubmit}">
                <input
                        type="text"
                        name="title"
                        id="job-title"
                        placeholder="Title"
                />
                <input
                        type="text"
                        name="imageUrl"
                        id="job-logo"
                        placeholder="Company logo url"
                />
                <input
                        type="text"
                        name="category"
                        id="job-category"
                        placeholder="Category"
                />
                <textarea
                        id="job-description"
                        name="description"
                        placeholder="Description"
                        rows="4"
                        cols="50"
                ></textarea>
                <textarea
                        id="job-requirements"
                        name="requirements"
                        placeholder="Requirements"
                        rows="4"
                        cols="50"
                ></textarea>
                <input
                        type="text"
                        name="salary"
                        id="job-salary"
                        placeholder="Salary"
                />

                <button type="submit">post</button>
            </form>
        </div>
    </section>

`;

export function createPage() {
    render(createTemplate(onSubmit), document.querySelector('main'));

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
        await fetch('http://localhost:3030/data/offers', {
            method: 'post', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }, body: JSON.stringify({title, imageUrl, category, description, requirements, salary})
        });
        page.redirect('/dashboard');
    }
}
