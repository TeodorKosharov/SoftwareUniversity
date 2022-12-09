import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

export async function editPage(context) {
    const clickedShoes = await (await fetch(`http://localhost:3030/data/shoes/${context.params.id}`)).json();
    const editTemplate = (onSubmit) => html`
        <section id="edit">
            <div class="form">
                <h2>Edit item</h2>
                <form class="edit-form" @submit="${onSubmit}">
                    <input
                            type="text"
                            name="brand"
                            id="shoe-brand"
                            placeholder="Brand"
                            value="${clickedShoes.brand}"
                    />
                    <input
                            type="text"
                            name="model"
                            id="shoe-model"
                            placeholder="Model"
                            value="${clickedShoes.model}"
                    />
                    <input
                            type="text"
                            name="imageUrl"
                            id="shoe-img"
                            placeholder="Image url"
                            value="${clickedShoes.imageUrl}"
                    />
                    <input
                            type="text"
                            name="release"
                            id="shoe-release"
                            placeholder="Release date"
                            value="${clickedShoes.release}"
                    />
                    <input
                            type="text"
                            name="designer"
                            id="shoe-designer"
                            placeholder="Designer"
                            value="${clickedShoes.designer}"
                    />
                    <input
                            type="text"
                            name="value"
                            id="shoe-value"
                            placeholder="Value"
                            value="${clickedShoes.value}"
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
        const brand = formData.get('brand');
        const model = formData.get('model');
        const imageUrl = formData.get('imageUrl');
        const release = formData.get('release');
        const designer = formData.get('designer');
        const value = formData.get('value');

        if (brand === '' || model === '' || imageUrl === '' || release === '' || designer === '' || value === '') {
            return alert('There must not be empty fields!');
        }

        await fetch(`http://localhost:3030/data/shoes/${context.params.id}`, {
            method: 'put',
            headers: {
                'content-type': 'application/json',
                'x-authorization': JSON.parse(sessionStorage.userData).token
            },
            body: JSON.stringify({brand, model, imageUrl, release, designer, value})
        });
        page.redirect(`/dashboard/${context.params.id}`);
    }
}
