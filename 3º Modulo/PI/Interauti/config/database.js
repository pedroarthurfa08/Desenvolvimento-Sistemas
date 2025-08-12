// Configuração de conexão com PostgreSQL
const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
    user: process.env.PGUSER || 'seu_usuario',
    host: process.env.PGHOST || 'localhost',
    database: process.env.PGDATABASE || 'interauti',
    password: process.env.PGPASSWORD || 'sua_senha',
    port: process.env.PGPORT ? parseInt(process.env.PGPORT) : 5432,
});

pool.on('connect', () => {
    console.log('Conectado ao PostgreSQL');
});

pool.on('error', (err) => {
    console.error('Erro na conexão com o PostgreSQL:', err);
});

module.exports = pool; 