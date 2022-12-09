import {template} from "./contactTemplate.js";
import {contacts} from "./contacts.js";
import {render} from "../../../node_modules/lit-html/lit-html.js";

const contactsDiv = document.getElementById('contacts');
const result = contacts.map(contact => template(contact));
render(result, contactsDiv);


