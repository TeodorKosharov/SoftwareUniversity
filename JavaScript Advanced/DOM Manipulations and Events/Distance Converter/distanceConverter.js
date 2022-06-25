function attachEventsListeners() {
    const inputField = document.getElementById('inputDistance');
    const inputDistances = document.getElementById('inputUnits');
    const convertButton = document.getElementById('convert');
    const outputField = document.getElementById('outputDistance');
    const outputDistances = document.getElementById('outputUnits');

    convertButton.addEventListener('click', convert);

    const distancesInMeters = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254
    };

    function convert() {
        const inputValue = inputField.value;
        const selectedDistance = inputDistances.value;
        const outputDistance = outputDistances.value;
        const inputMeters = distancesInMeters[selectedDistance] * inputValue;
        const outputDistanceMeters = distancesInMeters[outputDistance];
        const result = inputMeters / outputDistanceMeters;
        outputField.value = result;
    }
}
