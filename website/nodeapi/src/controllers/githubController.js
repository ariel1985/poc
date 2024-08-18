const axios = require('axios');
const Repository = require('../models/Repository');

const fetchRepositoryData = async (repoName) => {
    try {
        const response = await axios.get(`https://api.github.com/repos/${repoName}`);
        const data = response.data;

        const repository = new Repository({
            id: data.id,
            name: data.name,
            stars: data.stargazers_count,
            owner: data.owner.login,
            description: data.description,
            forks: data.forks_count,
            languages: Object.keys(data.languages),
            topics: data.topics
        });

        await repository.save();
        return repository;
    } catch (error) {
        throw new Error('Repository not found');
    }
};

module.exports = { fetchRepositoryData };
