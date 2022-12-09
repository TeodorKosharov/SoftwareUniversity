import {html} from '../../../node_modules/lit-html/lit-html.js';

// export function template(contactObject) {
//     return html`
//         <div>
//             <i class="far fa-user-circle gravatar"></i>
//         </div>
//         <div class="info">
//             <h2>Name: ${contactObject.name}</h2>
//             <button class="detailsBtn">Details</button>
//             <div class="details" id="1">
//                 <p>Phone number: ${contactObject.phoneNumber}</p>
//                 <p>Email: ${contactObject.email}</p>
//             </div>
//         </div>
//         </div>
//     `;
// }

export const template = (contactObject) => {
    return html`
        <div class="contact card">
            <div>
                <i class="far fa-user-circle gravatar"></i>
            </div>
            <div class="info">
                <h2>Name: ${contactObject.name}</h2>
                <button class="detailsBtn" @click=${showMore}>Details</button>
                <div class="details" id="1">
                    <p>Phone number: ${contactObject.phoneNumber}</p>
                    <p>Email: ${contactObject.email}</p>
                </div>
            </div>
        </div>
        </div>
    `;
}

function showMore(event) {
    const parent = event.target.parentElement.querySelector('.details').style.display = 'inline-block';
}