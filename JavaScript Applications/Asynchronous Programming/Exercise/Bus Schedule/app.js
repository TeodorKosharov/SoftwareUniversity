function solve() {

    const infoField = document.querySelector('#info span');
    const departButton = document.getElementById('depart');
    const arriveButton = document.getElementById('arrive');
    let stop = {
        name: 'Depot', next: 'depot'
    };

    async function depart() {
        const url = `http://localhost:3030/jsonstore/bus/schedule/${stop.next}`;
        const response = await fetch(url);   // Правим заявката
        const busData = await response.json();
        stop = busData;
        infoField.textContent = `Next stop ${stop.name}`;
        departButton.disabled = true;
        arriveButton.disabled = false;
    }

    function arrive() {
        departButton.disabled = false;
        arriveButton.disabled = true;
        infoField.textContent = `Arriving at ${stop.name}`;
    }

    return {
        depart, arrive
    };
}

let result = solve();