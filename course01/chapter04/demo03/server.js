const http = require('http');
const server_port = 3000;

// 创建HTTP服务器
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, World!\n');
});

// 监听指定端口
server.listen(server_port, () => {
    console.log(`Server is running at http://localhost:${server_port}/`);
});