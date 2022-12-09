import {updateNavi} from "../app.js";

updateNavi();

document.querySelector('.add').disabled = sessionStorage.userData === undefined;

// Load catches:
async function loading() {
    const catches = await (await fetch('http://localhost:3030/data/catches')).json();
    const catchesDiv = document.getElementById('catches');
    catchesDiv.innerHTML = '';

    catches.forEach(loadedCatch => {
        const catchDiv = document.createElement('div');
        catchDiv.className = 'catch';
        catchDiv.innerHTML = `
                        <label>Angler</label>
                        <input type="text" class="angler" value="${loadedCatch.angler}">
                        <label>Weight</label>
                        <input type="text" class="weight" value="${loadedCatch.weight}">
                        <label>Species</label>
                        <input type="text" class="species" value="${loadedCatch.species}">
                        <label>Location</label>
                        <input type="text" class="location" value="${loadedCatch.location}">
                        <label>Bait</label>
                        <input type="text" class="bait" value="trolled pink">
                        <label>Capture Time</label>
                        <input type="number" class="captureTime" value="80">
                        <button class="update" data-id="${loadedCatch._id}">Update</button>
                        <button class="delete" data-id="${loadedCatch._id}">Delete</button>
        `;

        const updateButton = catchDiv.querySelector('.update');
        const deleteButton = catchDiv.querySelector('.delete');

        updateButton.addEventListener('click', async () => {
            const angler = catchDiv.querySelector('.angler').value;
            const weight = catchDiv.querySelector('.weight').value;
            const species = catchDiv.querySelector('.species').value;
            const location = catchDiv.querySelector('.location').value;
            const bait = catchDiv.querySelector('.bait').value;
            const captureTime = catchDiv.querySelector('.captureTime').value;

            if (angler === '' || weight === '' || species === '' || location === '' || bait === '' || captureTime === '') {
                return alert('All fields are required!');
            }

            await fetch(`http://localhost:3030/data/catches/${updateButton.dataset.id}`, {
                method: 'put', headers: {
                    'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
                }, body: JSON.stringify({angler, weight, species, location, bait, captureTime})
            });

            return loading();
        });

        deleteButton.addEventListener('click', async () => {
            await fetch(`http://localhost:3030/data/catches/${deleteButton.dataset.id}`, {
                method: 'delete', headers: {
                    'x-authorization': JSON.parse(sessionStorage.userData).token
                }
            });
            return loading();
        });

        let currentUserId;
        sessionStorage.userData !== undefined ? currentUserId = JSON.parse(sessionStorage.userData).id : currentUserId = {};

        if (currentUserId === loadedCatch._ownerId) {
            updateButton.disabled = false;
            deleteButton.disabled = false;
        } else {
            updateButton.disabled = true;
            deleteButton.disabled = true;
        }

        catchesDiv.appendChild(catchDiv);
    });
}

document.querySelector('.load').addEventListener('click', loading);

// Add:
document.getElementById('addForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const angler = formData.get('angler');
    const weight = formData.get('weight');
    const species = formData.get('species');
    const location = formData.get('location');
    const bait = formData.get('bait');
    const captureTime = formData.get('captureTime');
    const id = JSON.parse(sessionStorage.userData).id;
    event.target.reset();

    if (angler === '' || weight === '' || species === '' || location === '' || bait === '' || captureTime === '') {
        return alert('All fields are required!');
    }

    await fetch('http://localhost:3030/data/catches', {
        method: 'post', headers: {
            'content-type': 'application/json', 'x-authorization': JSON.parse(sessionStorage.userData).token
        }, body: JSON.stringify({_ownerId: id, angler, weight, species, location, captureTime})
    });
    return loading();
});
