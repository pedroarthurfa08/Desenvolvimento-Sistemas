const express = require('express');
const router = express.Router();
const Task = require('../models/Task');

router.get('/agenda', async (req, res) => {
    let tasks = [];
    if (req.user) {
        tasks = await Task.findAllByUser(req.user.id);
    }
    res.render('agenda', { user: req.user, tasks });
});

module.exports = router; 