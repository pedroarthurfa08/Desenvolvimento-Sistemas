const bcrypt = require('bcrypt');
const pool = require('../config/database');

const User = {
    async create({ name, email, password, role = 'user' }) {
        const hash = await bcrypt.hash(password, 10);
        const result = await pool.query(
            'INSERT INTO users (name, email, password, role) VALUES ($1, $2, $3, $4) RETURNING *',
            [name, email, hash, role]
        );
        return result.rows[0];
    },

    async findByEmail(email) {
        const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
        return result.rows[0];
    },

    async findById(id) {
        const result = await pool.query('SELECT * FROM users WHERE id = $1', [id]);
        return result.rows[0];
    },

    async updatePhoto(id, photoUrl) {
        await pool.query('UPDATE users SET photo_url = $1, updated_at = CURRENT_TIMESTAMP WHERE id = $2', [photoUrl, id]);
    },

    async updateProfile(id, { name, email, settings }) {
        try {
            console.log('Executando updateProfile para ID:', id);
            console.log('Dados a serem atualizados:', { name, email, settings });
            
            const result = await pool.query(
                'UPDATE users SET name = $1, email = $2, settings = $3, updated_at = CURRENT_TIMESTAMP WHERE id = $4 RETURNING *',
                [name, email, JSON.stringify(settings), id]
            );
            
            if (result.rowCount === 0) {
                throw new Error('Usuário não encontrado');
            }
            
            console.log('Perfil atualizado com sucesso:', result.rows[0]);
            return result.rows[0];
        } catch (error) {
            console.error('Erro no updateProfile:', error);
            throw error;
        }
    },

    async comparePassword(candidatePassword, hash) {
        return await bcrypt.compare(candidatePassword, hash);
    }
};

module.exports = User; 