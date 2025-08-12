const express = require('express');
const router = express.Router();

router.get('/contato', (req, res) => {
    res.render('contato', { user: req.user });
});

module.exports = router;