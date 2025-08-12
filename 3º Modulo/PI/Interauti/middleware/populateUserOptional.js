const jwt = require('jsonwebtoken');
const User = require('../models/User');

const populateUserOptional = async (req, res, next) => {
    try {
        const token = req.cookies.token;
        if (token) {
            const decoded = jwt.verify(token, process.env.JWT_SECRET || 'seu_segredo_jwt');
            const user = await User.findById(decoded.userId);
            if (user) {
                // Converter photo_url para photoUrl para compatibilidade com a view
                if (user.photo_url) {
                    user.photoUrl = user.photo_url;
                }
                req.user = user;
            }
        }
    } catch (error) {
        // Não faz nada, apenas segue sem usuário
    }
    next();
};

module.exports = populateUserOptional; 