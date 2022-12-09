import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

const createTemplate = (onSubmit) => html`
    <section id="create-page" class="auth">
        <form id="create" @submit="${onSubmit}">
            <h1 class="title">Create Post</h1>

            <article class="input-group">
                <label for="title">Post Title</label>
                <input type="title" name="title" id="title">
            </article>

            <article class="input-group">
                <label for="description">Description of the needs </label>
                <input type="text" name="description" id="description">
            </article>

            <article class="input-group">
                <label for="imageUrl"> Needed materials image </label>
                <input type="text" name="imageUrl" id="imageUrl">
            </article>

            <article class="input-group">
                <label for="address">Address of the orphanage</label>
                <input type="text" name="address" id="address">
            </article>

            <article class="input-group">
                <label for="phone">Phone number of orphanage employee</label>
                <input type="text" name="phone" id="phone">
            </article>

            <input type="submit" class="btn submit" value="Create Post">
        </form>
    </section>
`;

export function createPage() {
    render(createTemplate(onSubmit), document.querySelector('main'));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const title = formData.get('title');
        const description = formData.get('description');
        const imageUrl = formData.get('imageUrl');
        const address = formData.get('address');
        const phone = formData.get('phone');

        if (title === '' || description === '' || imageUrl === '' || address === '' || phone === '') {
            return alert('All fields are required!');
        }

        await fetch('http://localhost:3030/data/posts', {
            method: 'post', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }, body: JSON.stringify({title, description, imageUrl, address, phone})
        });

        page.redirect('/dashboard');
    }
}
