const express = require('express');
const mysql = require('mysql2');
require('dotenv').config();
const path = require('path');

const app = express();
const port = 8080;

// 정적 파일 경로
app.use(express.static(path.join(__dirname, 'public')));
require('dotenv').config({ path: path.join(__dirname, '../../../.env') });

// DB 연결
const db = mysql.createConnection({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database,
    port: process.env.port,
});

db.connect((err) => {
    if (err) {
        console.error('❌ MySQL 연결 실패:', err);
        return;
    }
    console.log('✅ MySQL 연결 성공!');
});

// API: 데이터 응답
app.get('/st_info', (req, res) => {
    db.query('SELECT * FROM st_info', (err, rows) => {
        if (err) {
            console.error('쿼리 오류:', err);
            return res.status(500).send('DB 오류');
        }
        res.json(rows);
    });
});

app.listen(port, () => {
    console.log(`✅ 서버 실행 중: http://localhost:${port}`);
});
