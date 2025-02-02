const pool = require('../config/db');

const UserModel = {
    createUser: async (username, nationalCode, hashedPassword, role) => {
        return pool.query(
            'INSERT INTO users (username, nationalCode, hashedPassword, role) VALUES ($1, $2, $3, $4) RETURNING id, username, role',
            [username, nationalCode, hashedPassword, role]
        );
    },

    findUserByUsername: async (username) => {
        return pool.query('SELECT * FROM users WHERE username = $1', [username]);
    },

    getUserById: async (id) => {
        return pool.query('SELECT id, username, nationalCode, hashedpassword, role FROM users WHERE id = $1', [id]);
    },

    updatePassword: async (id, hashedPassword) => {
        return pool.query('UPDATE users SET hashedPassword = $1 WHERE id = $2', [hashedPassword, id]);
    },

    deleteUser: async (id) => {
        return pool.query('DELETE FROM users WHERE id = $1', [id]);
    },

    getAllUsers: async () => {
        return pool.query('SELECT id, username, nationalCode, role FROM users');
    }
};

module.exports = UserModel;
