const express = require('express');
const mongoose = require('mongoose');
const githubRoutes = require('./routes/githubRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

mongoose.connect('mongodb://localhost:27017/github', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.log(err));

app.use(express.json());
app.use('/api', githubRoutes);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
