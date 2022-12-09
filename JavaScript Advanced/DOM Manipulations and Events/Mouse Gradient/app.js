function attachGradientEvents() {

    document.getElementById('gradient').addEventListener('mousemove', onMouseOver)

    function onMouseOver(event) {
        let percentage = Math.floor(event.offsetX / event.target.clientWidth * 100);
        console.log(percentage);
        document.getElementById('result').textContent = `${percentage}%`;
    }

}