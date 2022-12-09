import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

const createMemeTemplate = (onSubmit) => html`
    <section id="create-meme">
        <form id="create-form" @submit="${onSubmit}">
            <div class="container">
                <h1>Create Meme</h1>
                <label for="title">Title</label>
                <input id="title" type="text" placeholder="Enter Title" name="title">
                <label for="description">Description</label>
                <textarea id="description" placeholder="Enter Description" name="description"></textarea>
                <label for="imageUrl">Meme Image</label>
                <input id="imageUrl" type="text" placeholder="Enter meme ImageUrl" name="imageUrl">
                <input type="submit" class="registerbtn button" value="Create Meme">
            </div>
        </form>
    </section>`;

export function createPage() {
    render(createMemeTemplate(onSubmit), document.querySelector('main'));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const title = formData.get('title');
        const description = formData.get('description');
        const imgUrl = formData.get('imageUrl');
        event.target.reset();

        if (title === '' || description === '' || imgUrl === '') {
            return alert('All fields are required!');
        }

        const data = {title, description, imageUrl :imgUrl};
        await fetch('http://localhost:3030/data/memes', {
            method: 'post', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }, body: JSON.stringify(data)
        });
        page.redirect('/memes');
    }
}
