const router = require('express').Router();
const { config } = require('../config');

// Routers
const filesRouter = require('./file.router');

function endpoint(app) {
  // Over writting efault base path
  app.use(`${config.appRoute}`, router);

  // Base path routes
  router.use('/files', filesRouter);
}

module.exports = endpoint;
