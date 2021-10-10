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

    toggleTip(true);

    const response = await fetch(url, { method: 'GET' });

    toggleTip(false);

    const data = await response.json();

    console.log(data);

    /* Show selected folder */
    const { folder, status } = data;
    if(status == 'success') {
	addToList(folder);
    };
    
};

/* Show and hide suggestions */
function toggleTip(flag) {
    const element = document.getElementById('tip');
       
    element.setAttribute(
        'style', 
        flag ? ' ' : 'display: none;'
    );
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
    rbutton.setAttribute('class', 'rbutton');
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

/* Load config.json file in the UI */
async function loadJson() {
    const data = JSON.parse(await jsonImport());
    console.log(data);

    const { folders } = data;

    folders.forEach((entry) => addToList(entry));
};

/* Make GET request to /import end-point */
async function jsonImport() {
    const url = 'http://localhost:5000/import'
    const response = await fetch(url, { method: 'GET' });

    const data = await response.json();
    return data;
};

/** 
 * Dark and Light mode toggling and
 * make it persistent on refershing
*/

const checkbox = document.getElementById('checkbox');

// Run toggle function when checkbox is checked
checkbox.addEventListener('change', () => {
    // Apply .dark css class on body
    document.body.classList.toggle('dark');
    // Set cached value of dark-mode as on
    localStorage.setItem('dark-mode', 'on');
});

// Toggle is cached value of dark mode is on
if (localStorage.getItem('dark-mode') == 'on') {
    checkbox.checked = true;
    document.body.classList.toggle('dark');
};

// Update value in cache when toggle is set on light
checkbox.addEventListener('change', () => {
    if (checkbox.checked == false) {
        localStorage.setItem('dark-mode', 'off');
    };
});

console.log(checkbox.checked);

    
