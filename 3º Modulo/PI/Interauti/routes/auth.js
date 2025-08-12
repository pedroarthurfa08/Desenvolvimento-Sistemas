const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');
const { auth } = require('../middleware/auth');
const multer = require('multer');
const path = require('path');

// Configuração do multer para upload de fotos
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, path.join(__dirname, '../public/images/profiles'));
    },
    filename: function (req, file, cb) {
        const ext = path.extname(file.originalname);
        cb(null, 'user-' + req.user.id + '-' + Date.now() + ext);
    }
});
const upload = multer({ storage });

// Rotas de autenticação
router.get('/login', authController.getLogin);
router.post('/login', authController.postLogin);
router.get('/register', authController.getRegister);
router.post('/register', authController.postRegister);
router.get('/logout', authController.logout);

router.get('/profile', auth, (req, res) => {
    try {
        console.log('Acessando perfil do usuário:', req.user.id);
        
        const user = req.user || {};
        
        // Garantir que settings existe e tem valores padrão
        if (!user.settings) {
            user.settings = { theme: 'dark', notifications: false, language: 'pt-BR' };
        } else if (typeof user.settings === 'string') {
            try {
                user.settings = JSON.parse(user.settings);
            } catch (e) {
                user.settings = { theme: 'dark', notifications: false, language: 'pt-BR' };
            }
        }
        
        // Garantir que todos os campos de settings existem
        user.settings.theme = user.settings.theme || 'dark';
        user.settings.notifications = user.settings.notifications || false;
        user.settings.language = user.settings.language || 'pt-BR';
        
        // Garantir compatibilidade photoUrl
        if (user.photo_url && !user.photoUrl) {
            user.photoUrl = user.photo_url;
        }
        
        console.log('Settings do usuário:', user.settings);
        
        // Pegar mensagens de sucesso/erro da query string
        const success = req.query.success || null;
        const error = req.query.error || null;
        
        res.render('auth/profile', { user, success, error });
    } catch (error) {
        console.error('Erro ao carregar perfil:', error);
        res.status(500).render('error', { message: 'Erro ao carregar perfil' });
    }
});

router.post('/profile/photo', auth, upload.single('photo'), authController.uploadPhoto);
router.post('/profile/photo/remove', auth, authController.removePhoto);
router.post('/profile', auth, authController.updateProfile);

module.exports = router; 