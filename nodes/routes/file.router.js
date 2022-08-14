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
  /*
  controller
    .addMessage(req.body.chat, req.body.user, req.body.message, req.file)
    .then((data) => {
      success(req, res, data, 201);
    })
    .catch((err) => {
      error(req, res, `Error creating message ${err}`, 400);
    });
  */
});

module.exports = router;
