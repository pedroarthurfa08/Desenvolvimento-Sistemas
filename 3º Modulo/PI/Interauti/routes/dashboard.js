const express = require('express');
const router = express.Router();
const taskController = require('../controllers/taskController');
const { auth } = require('../middleware/auth');

router.use(auth);

router.get('/dashboard', taskController.dashboard);

module.exports = router; 