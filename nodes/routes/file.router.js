const fileService = require('../services/file.service');
const router = require('express').Router();
const { config } = require('../config');
const multer = require('multer');

const upload = multer({
  dest: `${config.appStatic}/${config.appFiles}`,
});

router.get('/', async (req, res) => {
  try {
    const file = await fileService.getFileInfo();
    res.status(200).json(file);
  } catch (error) {
    console.error(error);
  }
});

router.post('/', upload.single('file'), (req, res) => {
  console.log(req, res);
});

module.exports = router;
