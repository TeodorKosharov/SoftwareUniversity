import {html, render} from '../../node_modules/lit-html/lit-html.js';

export async function detailsPage(context) {
    const clickedShoesId = context.params.id;
    const clickedShoes = await (await fetch(`http://localhost:3030/data/shoes/${clickedShoesId}`)).json();
    let detailsTemplate;

    if (sessionStorage.userData !== undefined && JSON.parse(sessionStorage.userData).id === clickedShoes._ownerId) {
        detailsTemplate = html`
            <section id="details">
                <div id="details-wrapper">
                    <p id="details-title">Shoe Details</p>
                    <div id="img-wrapper">
                        <img src="${clickedShoes.imageUrl}" alt="example1" />
                    </div>
                    <div id="info-wrapper">
                        <p>Brand: <span id="details-brand">${clickedShoes.brand}</span></p>
                        <p>
                            Model: <span id="details-model">${clickedShoes.model}</span>
                        </p>
                        <p>Release date: <span id="details-release">${clickedShoes.release}</span></p>
                        <p>Designer: <span id="details-designer">${clickedShoes.designer}</span></p>
                        <p>Value: <span id="details-value">${clickedShoes.value}</span></p>
                    </div>

                    <!--Edit and Delete are only for creator-->
                    <div id="action-buttons">
                        <a href="/edit/${clickedShoesId}" id="edit-btn">Edit</a>
                        <a href="/delete/${clickedShoesId}" id="delete-btn">Delete</a>
                    </div>
                </div>
            </section>
            
        `;
    }
    else {
        detailsTemplate = html`
            <section id="details">
                <div id="details-wrapper">
                    <p id="details-title">Shoe Details</p>
                    <div id="img-wrapper">
                        <img src="${clickedShoes.imageUrl}" alt="example1" />
                    </div>
                    <div id="info-wrapper">
                        <p>Brand: <span id="details-brand">${clickedShoes.brand}</span></p>
                        <p>
                            Model: <span id="details-model">${clickedShoes.model}</span>
                        </p>
                        <p>Release date: <span id="details-release">${clickedShoes.release}</span></p>
                        <p>Designer: <span id="details-designer">${clickedShoes.designer}</span></p>
                        <p>Value: <span id="details-value">${clickedShoes.value}</span></p>
                    </div>
                </div>
            </section>
            
        `;
    }

    render(detailsTemplate, document.querySelector('main'));
}
