async function getData() {
    const data = await fetch('http://127.0.0.1:8000/api/get-items/');
    const result = await data.json();
    console.log(result);
}
