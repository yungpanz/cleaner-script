/**
* Paolo Anzani <p.anzani@campus.unimib.it> 10-07-2021
* UI
*/

/* Open Dialog GUI */

async function getFolder() {
    const url = 'http://127.0.0.1:5000/dialog';

    const response = await fetch(url, { method: 'POST' });

    const data = await response.json();

    console.log(data);
};
