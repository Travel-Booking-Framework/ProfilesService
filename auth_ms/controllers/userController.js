const UserModel = require('../models/userModel');
const bcrypt = require('bcryptjs');

const getProfile = async (req, res) => {
    try {
        const user = await UserModel.getUserById(req.user.id);
        res.json(user.rows[0]);
    } catch (err) {
        res.status(500).json({ message: "Error fetching profile", error: err.message });
    }
};

const changePassword = async (req, res) => {
    const { oldPassword, newPassword } = req.body;

    if (!oldPassword || !newPassword) {
        return res.status(400).json({ message: "Old and new passwords required" });
    }

    try {
        const userResult = await UserModel.getUserById(req.user.id);
        
        if (userResult.rowCount === 0) return res.status(404).json({ message: "User not found" });

        const user = userResult.rows[0];
        const storedHashedPassword = user.hashedpassword || user.hashedPassword; // Ensure correct column name

        if (!storedHashedPassword) {
            return res.status(500).json({ message: "Error: hashedPassword is missing" });
        }

        const validPassword = await bcrypt.compare(oldPassword, storedHashedPassword);
        if (!validPassword) return res.status(403).json({ message: "Incorrect old password" });

        const hashedNewPassword = await bcrypt.hash(newPassword, 10);
        await UserModel.updatePassword(req.user.id, hashedNewPassword);

        res.json({ message: "Password changed successfully" });
    } catch (err) {
        res.status(500).json({ message: "Error changing password", error: err.message });
    }
};

module.exports = { getProfile, changePassword };
