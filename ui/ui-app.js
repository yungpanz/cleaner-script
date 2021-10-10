/**
* Paolo Anzani <p.anzani@campus.unimib.it> 10-07-2021
* UI
*/

// Global variables

let n = 0;

/* Open Dialog GUI */

async function getFolder() {
    /* Post request to server.py dialog endpoint */
    const url = 'http://localhost:5000/dialog';

    const response = await fetch(url, { method: 'GET' });

    const data = await response.json();

    console.log(data);

    /* Show selected folder */
    const { folder, status } = data;
    if(status == 'success') {
	addToList(folder);
    };
    
};

/* Add select folders to the list */
function addToList(folder) {
    const list = document.querySelector('#folder-list');
    const entry = document.createElement('p');
    entry.textContent = folder;
    entry.setAttribute('id', `e${n}`);
    list.appendChild(entry);

    const rbutton = document.createElement('button');
    rbutton.textContent = 'delete';
    rbutton.setAttribute('onClick', `removeEntry('e${n}')`);
    entry.appendChild(rbutton);
    n += 1;
};

/* Remove folder from the list */
function removeEntry(id) {
    const entry = document.querySelector(`#${id}`);
    entry.remove();
};


/* Export selected folders to a JSON file */
function dumpJson() {
    const list = document.getElementById('folder-list').childNodes;
    
    let folderList = Array.from(list, (e) => e.textContent.slice(0, -6).replace(/\s/g, '\\ '));
    // Remove first always empty element
    folderList.shift();
    console.log(folderList);

    const data = {
	"folders": folderList
    };

    jsonExport(JSON.stringify(data));

};

/* POST request to server endpoint to export json config */
async function jsonExport(data) {
    const url = 'http://localhost:5000/export';
    const header = new Headers({ 'Content-Type': 'application/json' });
    const response = await fetch(url, {
	method: 'POST',
	headers: header,
	body: data
    });

    console.log(response);
};
