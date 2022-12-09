import {html, render} from "../../../node_modules/lit-html/lit-html.js";

async function solve() {
    document.querySelector('#searchBtn').addEventListener('click', onClick);
    const tableBody = document.querySelector('tbody');
    const searchField = document.getElementById('searchField');
    render(await getData(searchField.value), tableBody);

    async function onClick() {
        render(await getData(searchField.value), tableBody);
        searchField.value = '';
    }
}

function template(obj, searchValue) {
    if (rowContains(obj, searchValue) === true) {
        return html`
            <tr class="select">
                <td>${obj.firstName} ${obj.lastName}</td>
                <td>${obj.email}</td>
                <td>${obj.course}</td>
            </tr>
        `;
    } else {
        return html`
            <tr>
                <td>${obj.firstName} ${obj.lastName}</td>
                <td>${obj.email}</td>
                <td>${obj.course}</td>
            </tr>
        `;
    }
}

function rowContains(obj, searchValue) {
    const searchText = searchValue.toLowerCase();
    if ((obj.firstName.toLowerCase().includes(searchText) ||
            obj.lastName.toLowerCase().includes(searchText) ||
            obj.email.toLowerCase().includes(searchText) ||
            obj.course.toLowerCase().includes(searchText))
        && searchValue !== '') return true;

}

async function getData(searchText) {
    const response = await fetch('http://localhost:3030/jsonstore/advanced/table');
    const data = Object.entries(await response.json()).map(arr => arr[1]);
    return data.map(obj => template(obj, searchText));
}

await solve()
