const fs = require('fs');
const roles = JSON.parse(fs.readFileSync('config/roles.json', 'utf-8'));

const authorize = (permission) => {
    return (req, res, next) => {
        const userRole = req.user.role;

        if (!roles[userRole] || !roles[userRole].includes(permission)) {
            return res.status(403).json({ message: "Forbidden: Insufficient permissions" });
        }

        next();
    };
};

module.exports = authorize;
