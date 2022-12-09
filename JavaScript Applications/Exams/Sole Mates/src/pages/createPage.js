import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

const createTemplate = (onSubmit) => html`
    <section id="create">
        <div class="form">
            <h2>Add item</h2>
            <form class="create-form" @submit="${onSubmit}">
                <input
                        type="text"
                        name="brand"
                        id="shoe-brand"
                        placeholder="Brand"
                />
                <input
                        type="text"
                        name="model"
                        id="shoe-model"
                        placeholder="Model"
                />
                <input
                        type="text"
                        name="imageUrl"
                        id="shoe-img"
                        placeholder="Image url"
                />
                <input
                        type="text"
                        name="release"
                        id="shoe-release"
                        placeholder="Release date"
                />
                <input
                        type="text"
                        name="designer"
                        id="shoe-designer"
                        placeholder="Designer"
                />
                <input
                        type="text"
                        name="value"
                        id="shoe-value"
                        placeholder="Value"
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
        const brand = formData.get('brand');
        const model = formData.get('model');
        const imageUrl = formData.get('imageUrl');
        const release = formData.get('release');
        const designer = formData.get('designer');
        const value = formData.get('value');

        if (brand === '' || model === '' || imageUrl === '' || release === '' || designer === '' || value === '') {
            return alert('There must not be empty fields!');
        }

        await fetch('http://localhost:3030/data/shoes', {
            method: 'post',
            headers: {
                'content-type': 'application/json',
                'x-authorization': JSON.parse(sessionStorage.userData).token
            },
            body: JSON.stringify({brand, model, imageUrl, release, designer, value})
        });
        page.redirect('/dashboard');
    }
}
