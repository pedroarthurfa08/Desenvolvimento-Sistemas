const request = require('supertest');
const app = require('../app');
const mongoose = require('mongoose');
const User = require('../models/User');
const Task = require('../models/Task');

let agent;
let csrfToken;
let cookie;

beforeAll(async () => {
    // Conectar ao banco de dados de teste
    await mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/interauti_test', {
        useNewUrlParser: true,
        useUnifiedTopology: true
    });
    // Criar usuário de teste
    await User.deleteMany({ email: 'test@teste.com' });
    await Task.deleteMany({});
    await User.create({ name: 'Test', email: 'test@teste.com', password: '123456' });
    agent = request.agent(app);
});

afterAll(async () => {
    await mongoose.connection.close();
});

test('Login e criação de tarefa', async () => {
    // Login
    let res = await agent.get('/login');
    csrfToken = /name="_csrf" value="(.+?)"/.exec(res.text)[1];
    res = await agent
        .post('/login')
        .type('form')
        .send({ email: 'test@teste.com', password: '123456', _csrf: csrfToken });
    expect(res.header['set-cookie']).toBeDefined();
    // Nova tarefa
    res = await agent.get('/tasks/create');
    csrfToken = /name="_csrf" value="(.+?)"/.exec(res.text)[1];
    res = await agent
        .post('/tasks')
        .type('form')
        .send({ title: 'Tarefa Teste', description: 'Descrição', priority: 'alta', _csrf: csrfToken });
    expect(res.header['location']).toBe('/tasks');
    // Verificar se a tarefa foi criada
    const task = await Task.findOne({ title: 'Tarefa Teste' });
    expect(task).not.toBeNull();
    expect(task.description).toBe('Descrição');
}); 