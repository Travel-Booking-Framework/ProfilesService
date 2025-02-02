const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const UserModel = require('../models/userModel');

const JWT_SECRET = process.env.JWT_SECRET || 'default_secret';

const register = async (req, res) => {
    const { username, nationalCode, password, role } = req.body;

    if (!username || !nationalCode || !password || nationalCode.length !== 10 || !role) {
        return res.status(400).json({ message: "Invalid input" });
    }

    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const result = await UserModel.createUser(username, nationalCode, hashedPassword, role);
        res.status(201).json({ message: "User registered", user: result.rows[0] });
    } catch (err) {
        res.status(500).json({ message: "User already exists or error occurred", error: err.message });
    }
};

const login = async (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) return res.status(400).json({ message: "Invalid input" });

    try {
        const result = await UserModel.findUserByUsername(username);
        if (result.rowCount === 0) return res.status(401).json({ message: "User not found" });

        const user = result.rows[0];
        const validPassword = await bcrypt.compare(password, user.hashedpassword);
        if (!validPassword) return res.status(401).json({ message: "Invalid credentials" });

        const token = jwt.sign({ id: user.id, username: user.username, role: user.role }, JWT_SECRET, { expiresIn: '1h' });
        res.json({ token });
    } catch (err) {
        res.status(500).json({ message: "Error occurred", error: err.message });
    }
};

module.exports = { register, login };
