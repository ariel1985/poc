const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World from Node.js!  🚀 - this is MS-FASTAPI-NODE-ANGULAR-MONGO app');
});

app.listen(port, () => {
  console.log(`Node.js service listening at http://localhost:${port}`);
});
