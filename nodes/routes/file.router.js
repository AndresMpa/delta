const router = require('express').Router();
const { config } = require('../config');
const multer = require('multer');

const upload = multer({
  dest: `${config.appStatic}/${config.appFiles}`,
});

router.get('/', (req, res) => {
  console.log(req, res);
  /*
  const filterMessage = req.query.chat || null;
  controller
    .listMessages(filterMessage)
    .then((messageList) => {
      success(req, res, messageList, 200);
    })
    .catch((err) => {
      error(req, res, `Unable to load messages ${err}`, 500);
    });
  */
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
