import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';

export async function editPage(context) {
    const editTemplate = (onSubmit, book) => html`
    <section id="edit-page" class="edit">
        <form id="edit-form" action="#" method="" @submit="${onSubmit}">
            <fieldset>
                <legend>Edit my Book</legend>
                <p class="field">
                    <label for="title">Title</label>
                    <span class="input">
                            <input type="text" name="title" id="title" value="${book.title}">
                        </span>
                </p>
                <p class="field">
                    <label for="description">Description</label>
                    <span class="input">
                            <textarea name="description"
                                      id="description">${book.description}</textarea>
                        </span>
                </p>
                <p class="field">
                    <label for="image">Image</label>
                    <span class="input">
                            <input type="text" name="imageUrl" id="image" value="${book.imageUrl}">
                        </span>
                </p>
                <p class="field">
                    <label for="type">Type</label>
                    <span class="input">
                            <select id="type" name="type" value="Fiction">
                                <option value="Fiction" selected>Fiction</option>
                                <option value="Romance">Romance</option>
                                <option value="Mistery">Mistery</option>
                                <option value="Classic">Clasic</option>
                                <option value="Other">Other</option>
                            </select>
                        </span>
                </p>
                <input class="button submit" type="submit" value="Save">
            </fieldset>
        </form>
    </section>
`;
    const clickedBookId = context.params.id;
    const clickedBookData = await(await fetch(`http://localhost:3030/data/books/${clickedBookId}`)).json();
    render(editTemplate(onSubmit, clickedBookData), document.querySelector('main'));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const title = formData.get('title');
        const description = formData.get('description');
        const imageUrl = formData.get('imageUrl');
        const type = formData.get('type');

        if (title === '' || description === '' || imageUrl === '') {
            return alert('All fields are required!');
        }

        const data = {title, description, imageUrl, type};
        await fetch(`http://localhost:3030/data/books/${clickedBookId}`, {
            method: 'put', headers: {
                'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
            }, body: JSON.stringify(data)
        });
        page.redirect(`/details/${clickedBookId}`);
    }
}
