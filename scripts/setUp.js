#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

function generateApiKey(size){
    return crypto.randomBytes(size).toString('hex');
}

const main = async () => {
    // Set the path and content for the .env file
    const envDirectory = path.resolve(__dirname, '..');
    const envPath = path.join(envDirectory, '.env');
    const envContent = `
SECRET_KEY_PROD=${generateApiKey(180)}
SECRET_KEY_DEV=${generateApiKey(180)}
LOCAL_DB_NAME=note_taker
APP_NAME=note taker
    `;
    await fs.promises.writeFile(envPath, envContent);
};


if (require.main === module) {
    main();
}
