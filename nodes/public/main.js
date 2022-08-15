const reload = document.querySelector('#reload');
const box = document.querySelector('.server--box');
const title = document.querySelector('.server--banner__title');

/*
Send a request to server host to get files
*/

const getFiles = async () => {
  const path = `http://${location.host}/api/v1/files`;
  return fetch(path, {
    method: 'GET',
  })
    .then((response) => response.json())
    .then((data) => {
      return data;
    })
    .catch((error) => console.error(error));
};

/*
Get information from getFiles(), then use that
information to created nodes with it in them
*/

const showFileInfo = async () => {
  const information = await getFiles() || [];

  const table = document.querySelector('.server--table tbody');

  information.forEach((item) => {
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

const reloadQuery = async () => {
  await showFileInfo();

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

window.onload = () => {
  reload.textContent += `: ${location.port}`;
  const content = title.textContent;

  title.textContent = `${content.slice(0, content.indexOf(' '))} ${
    location.port
  }${content.slice(content.indexOf(' '), content.length)}`;
};

reload.onmouseleave = () =>
  reload.classList.remove('animate__animated', 'animate__pulse');
reload.onmouseover = () =>
  reload.classList.add('animate__animated', 'animate__pulse');
reload.onclick = async () => await reloadQuery();
