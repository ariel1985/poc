const mongoose = require('mongoose');

const repositorySchema = new mongoose.Schema({
    id: String,
    name: String,
    stars: Number,
    owner: String,
    description: String,
    forks: Number,
    languages: [String],
    topics: [String]
});

module.exports = mongoose.model('Repository', repositorySchema);
