const express = require('express');
const server_port = 3000;

// 创建 Express 应用
const app = express();

// 定义一个简单的路由
app.get('/', (req, res) => {
    // 返回JSON数据
    res.json({ message: 'Hello, Fullstack Cloud Native!' });
});

// 启动服务器
app.listen(server_port, () => {
    console.log(`Server is running on http://localhost:${server_port}`);
});