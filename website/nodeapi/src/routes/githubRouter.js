const express = require('express');
const { fetchRepositoryData } = require('../controllers/githubController');
const Repository = require('../models/Repository');

const router = express.Router();

// Fetch repository data and store in DB
router.get('/fetch/:repoName', async (req, res) => {
    const { repoName } = req.params;
    try {
        const repo = await fetchRepositoryData(repoName);
        res.status(200).json(repo);
    } catch (error) {
        res.status(404).json({ error: error.message });
    }
});

// Get all repositories
router.get('/repositories', async (req, res) => {
    const repos = await Repository.find({}, 'id name stars owner description forks');
    res.status(200).json(repos);
});

// Get repository by name or ID
router.get('/repository/:identifier', async (req, res) => {
    const { identifier } = req.params;
    const repo = await Repository.findOne({ $or: [{ id: identifier }, { name: identifier }] });
    if (repo) {
        res.status(200).json(repo);
    } else {
        res.status(404).json({ error: 'Repository not found' });
    }
});

module.exports = router;
