// Teste de conexão com PostgreSQL
const { Client } = require('pg');

const client = new Client({
    user: 'postgres', // Altere para seu usuário do PostgreSQL
    host: 'localhost',
    database: 'interauti', // Altere para o nome do seu banco
    password: 'postgres', // Altere para sua senha
    port: 5432,
});

client.connect()
    .then(() => {
        console.log('Conexão bem-sucedida com o PostgreSQL!');
        return client.end();
    })
    .catch(err => {
        console.error('Erro ao conectar ao PostgreSQL:', err);
        client.end();
    }); 