const express = require('express');
const { getProfile, changePassword } = require('../controllers/userController');
const authenticateToken = require('../middleware/authMiddleware');
const authorize = require('../middleware/roleMiddleware');
const UserModel = require('../models/userModel');

const router = express.Router();

// Get authenticated user's profile
router.get('/profile', authenticateToken, getProfile);

// Change password (Authenticated users)
router.post('/change-password', authenticateToken, changePassword);

// Admin-only: Get all users
router.get('/users', authenticateToken, authorize('view_users'), async (req, res) => {
    try {
        const result = await UserModel.getAllUsers();
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ message: "Error fetching users", error: err.message });
    }
});

// Admin-only: Delete a user
router.delete('/users/:id', authenticateToken, authorize('delete_user'), async (req, res) => {
    try {
        const { id } = req.params;
        await UserModel.deleteUser(id);
        res.json({ message: "User deleted successfully" });
    } catch (err) {
        res.status(500).json({ message: "Error deleting user", error: err.message });
    }
});

module.exports = router;
