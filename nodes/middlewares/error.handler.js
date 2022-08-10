const chalk = require('chalk');

function logError(error, req, res, next) {
  `${chalk.red('[SERVER ERROR]:')} ${error}`;
  next(error);
}

function errorHandler(error, req, res, next) {
  res.status(500).json({
    message: error.message,
    stack: error.stack,
  });
}

module.exports = {
  errorHandler,
  logError,
};
