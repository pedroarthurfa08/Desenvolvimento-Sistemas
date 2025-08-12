-- Inserir usuário de teste
INSERT INTO users (name, email, password, role)
VALUES ('Usuário Teste', 'teste@teste.com', '$2b$10$hashfakesenha', 'user')
ON CONFLICT (email) DO NOTHING;

-- Inserir três tarefas de exemplo para o usuário criado
INSERT INTO tasks (title, description, status, priority, date, time, duration, user_id, tags, deleted)
VALUES
('Primeira tarefa', 'Descrição da primeira tarefa', 'pendente', 'média', CURRENT_DATE, '09:00', 60, (SELECT id FROM users WHERE email = 'teste@teste.com'), ARRAY['importante'], false),
('Segunda tarefa', 'Descrição da segunda tarefa', 'em_andamento', 'alta', CURRENT_DATE + INTERVAL '1 day', '14:00', 30, (SELECT id FROM users WHERE email = 'teste@teste.com'), ARRAY['urgente'], false),
('Terceira tarefa', 'Descrição da terceira tarefa', 'concluída', 'baixa', CURRENT_DATE - INTERVAL '1 day', '16:30', 45, (SELECT id FROM users WHERE email = 'teste@teste.com'), ARRAY['rotina'], false); 