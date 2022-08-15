const reload = document.querySelector('#reload');
const box = document.querySelector('.server--box');
const title = document.querySelector('.server--banner__title');

/*
Send a request to server host to get files
*/

const getFiles = async () => {
  const path = `${location.host}/api/v1/files`;
  fetch(path, {
    method: 'GET',
  })
    .then((response) => response.json())
    .then((data) => data)
    .catch((error) => console.error(error));
};

/*
Get information from getFiles(), then use that
information to created nodes with it in them
*/

const showFileInfo = () => {
  const information = getFiles() || [];

  const table = document.querySelector('.server--table tbody');

  [1, 2, 3].forEach((item) => {
    const newItem = document.createElement('tr');

    const file_name = document.createElement('td');
    const file_size = document.createElement('td');

    file_name.textContent = item.name || 'file.png';
    file_size.textContent = item.size || '80 KB';

    newItem.appendChild(file_name);
    newItem.appendChild(file_size);

    table.append(newItem);
  });
};

/*
Show a button to reload, if it is pressed;
it trigger a query
*/

const reloadQuery = () => {
  showFileInfo();

  const registers =
    document.querySelector('.server--table').lastChild.childNodes;

  if (registers.length <= 2) {
    box.style.display = 'none';
    title.style.display = 'none';
    reload.style.display = 'initial';
  } else {
    box.style.display = 'flex';
    reload.style.display = 'none';
    title.style.display = 'initial';
  }
};

window.onload = () => reload.textContent += `: ${location.port}`

reload.onmouseleave = () =>
  reload.classList.remove('animate__animated', 'animate__pulse');
reload.onmouseover = () =>
  reload.classList.add('animate__animated', 'animate__pulse');
reload.onclick = () => reloadQuery();
