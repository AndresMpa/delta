const { logError, errorHandler } = require('./middlewares/error.handler');
const socket = require('./config/socket');
const { config } = require('./config');
const endpoint = require('./routes');
const express = require('express');
const chalk = require('chalk');
const cors = require('cors');

// Express istance
const app = express();

// Middlewares
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(cors());

// HTTP server
const server = require('http').Server(app);

// Initialization of sockets
socket.connect(server);

// Paths
endpoint(app);

// Static files
app.use(`${config.appPublic}`, express.static(`./${config.appStatic}`));

// Errors handlers
app.use(logError);
app.use(errorHandler);

// App port
app.set('port', config.port);

// Server runner
server.listen(app.get('port'), () => {
  console.log(
    `${chalk.green('[SERVER]:')} App running on port ${chalk.green(
      `${app.get('port')}`
    )}`
  );
});