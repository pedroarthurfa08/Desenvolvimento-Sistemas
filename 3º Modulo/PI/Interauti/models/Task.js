const pool = require('../config/database');

const Task = {
    async create({ title, description, status = 'pendente', priority = 'média', date, time, duration, user_id, tags = [], deleted = false }) {
        const result = await pool.query(
            `INSERT INTO tasks (title, description, status, priority, date, time, duration, user_id, tags, deleted)
             VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10) RETURNING *`,
            [title, description, status, priority, date, time, duration, user_id, tags, deleted]
        );
        return result.rows[0];
    },

    async findById(id) {
        const result = await pool.query('SELECT * FROM tasks WHERE id = $1', [id]);
        return result.rows[0];
    },

    async findAllByUser(user_id, filters = {}) {
        let query = 'SELECT * FROM tasks WHERE user_id = $1 AND deleted = false';
        const params = [user_id];
        if (filters.status) {
            params.push(filters.status);
            query += ` AND status = $${params.length}`;
        }
        if (filters.priority) {
            params.push(filters.priority);
            query += ` AND priority = $${params.length}`;
        }
        query += ' ORDER BY created_at DESC';
        const result = await pool.query(query, params);
        return result.rows;
    },

    async update(id, data) {
        // Atualização dinâmica dos campos
        const fields = [];
        const values = [];
        let idx = 1;
        for (const key in data) {
            fields.push(`${key} = $${idx}`);
            values.push(data[key]);
            idx++;
        }
        values.push(id);
        const result = await pool.query(
            `UPDATE tasks SET ${fields.join(', ')}, updated_at = CURRENT_TIMESTAMP WHERE id = $${idx} RETURNING *`,
            values
        );
        return result.rows[0];
    },

    async delete(id) {
        await pool.query('UPDATE tasks SET deleted = true WHERE id = $1', [id]);
    },

    // Estatísticas para o dashboard
    async getDashboardStats(user_id) {
        // Busca todas as tarefas do usuário
        const result = await pool.query('SELECT * FROM tasks WHERE user_id = $1 AND deleted = false', [user_id]);
        const tasks = result.rows;
        const now = new Date();
        const today = now.toISOString().substr(0, 10);
        const month = now.getMonth();
        const year = now.getFullYear();

        // Funções auxiliares
        function isToday(date) {
            return date && new Date(date).toISOString().substr(0, 10) === today;
        }
        function isThisMonth(date) {
            if (!date) return false;
            const d = new Date(date);
            return d.getMonth() === month && d.getFullYear() === year;
        }

        // Filtragens
        const dailyTasks = tasks.filter(t => isToday(t.date));
        const monthlyTasks = tasks.filter(t => isThisMonth(t.date));
        const completedDaily = dailyTasks.filter(t => t.status === 'concluída');
        const completedMonthly = monthlyTasks.filter(t => t.status === 'concluída');
        const totalCompleted = tasks.filter(t => t.status === 'concluída');
        const overdue = tasks.filter(t => t.status !== 'concluída' && t.date && new Date(t.date) < now);
        const onTime = totalCompleted.filter(t => t.date && new Date(t.updated_at) <= new Date(t.date));
        const late = totalCompleted.filter(t => t.date && new Date(t.updated_at) > new Date(t.date));
        const activeDays = new Set(totalCompleted.map(t => t.updated_at && new Date(t.updated_at).toISOString().substr(0,10)));
        const monthlyActiveDays = new Set(completedMonthly.map(t => t.updated_at && new Date(t.updated_at).toISOString().substr(0,10)));
        const avgDuration = totalCompleted.length > 0 ? Math.round(totalCompleted.reduce((sum, t) => sum + (t.duration || 0), 0) / totalCompleted.length) : 0;

        // Estatísticas
        return {
            daily: {
                completedPercent: dailyTasks.length ? Math.round((completedDaily.length / dailyTasks.length) * 100) : 0,
                punctuality: completedDaily.length ? Math.round((onTime.filter(t => isToday(t.date)).length / completedDaily.length) * 100) : 0,
                procrastination: completedDaily.length ? Math.round((late.filter(t => isToday(t.date)).length / completedDaily.length) * 100) : 0,
            },
            monthly: {
                completedPercent: monthlyTasks.length ? Math.round((completedMonthly.length / monthlyTasks.length) * 100) : 0,
                productivity: monthlyTasks.length ? Math.round((completedMonthly.length / monthlyTasks.length) * 100) : 0,
                activeDays: monthlyActiveDays.size,
                daysInMonth: new Date(year, month + 1, 0).getDate(),
                overduePercent: monthlyTasks.length ? Math.round((monthlyTasks.filter(t => t.status !== 'concluída' && t.date && new Date(t.date) < now).length / monthlyTasks.length) * 100) : 0,
            },
            general: {
                totalCompleted: totalCompleted.length,
                avgPunctuality: totalCompleted.length ? Math.round((onTime.length / totalCompleted.length) * 100) : 0,
                maxProductiveStreak: getMaxStreak(Array.from(activeDays)),
                avgDuration,
            }
        };

        // Função para maior sequência de dias produtivos
        function getMaxStreak(datesArr) {
            if (!datesArr.length) return 0;
            const days = datesArr.map(d => new Date(d)).sort((a, b) => a - b);
            let maxStreak = 1, streak = 1;
            for (let i = 1; i < days.length; i++) {
                const diff = (days[i] - days[i-1]) / (1000*60*60*24);
                if (diff === 1) streak++;
                else streak = 1;
                if (streak > maxStreak) maxStreak = streak;
            }
            return maxStreak;
        }
    }
};

module.exports = Task; 