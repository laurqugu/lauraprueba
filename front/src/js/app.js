const URL_BASE = 'http://localhost:5000';

async function service(endpoint, number) {
    const response = await fetch(`${URL_BASE}/${endpoint}/${number}`);
    const json = await response.json();
    console.log(json);
    return json;
}
document.getElementById('form').addEventListener('submit', e => {
    e.preventDefault();
    this.service(
            document.getElementById('endpoint').value,
            document.getElementById('number').value
        )
        .then(res => {
            document.getElementById('response').value = JSON.stringify(res);
        })
        .catch(err => console.log('error', err));
});