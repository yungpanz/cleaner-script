/**
* Paolo Anzani <p.anzani@campus.unimib.it> 10-07-2021
* UI
*/

/* Open Dialog GUI */

async function getFolder() {
    /* Post request to server.py dialog endpoint */
    const url = 'http://127.0.0.1:5000/dialog';

    const response = await fetch(url, { method: 'POST' });

    const data = await response.json();

    console.log(data);

    /* Show selected folder */
    const { folder, status } = data;
    if(status == 'success') {
	addToList(folder);
    };
    
};

function addToList(folder) {
    const sect = document.querySelector('#folder-list');
    const entry = document.createElement('p');
    entry.textContent = folder;
    sect.appendChild(entry);
};


