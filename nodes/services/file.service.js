const { config } = require('../config');
const fs = require('fs');

class FileService {
  constructor() {
    this.filePath = `./${config.appStatic}/${config.appFiles}`;
  }

  async getFiles() {
    const files = await fs.readdirSync(this.filePath);
    return files;
  }

  async getFileInfo() {
    const files = await this.getFiles();
    const info = [];

    files.forEach((file) => {
      const data = fs.statSync(`${this.filePath}/${file}`);
      info.push({
        size: castToBytes(data.size),
        name: file,
      });
    });

    return info;
  }
}

function castToBytes(bytes) {
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];

  if (bytes == 0) {
    return 'n/a';
  }

  const byte = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));

  if (byte == 0) {
    return bytes + ' ' + sizes[byte];
  }

  return (bytes / Math.pow(1024, byte)).toFixed(1) + ' ' + sizes[byte];
}

module.exports = new FileService();
