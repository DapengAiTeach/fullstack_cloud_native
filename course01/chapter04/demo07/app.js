const http = require("http");
const server_port = 3000;

// 创建HTTP服务
const server = http.createServer((request, response) => {
  response.end("hello_from_docker\n");
});

// 启动HTTP服务
server.listen(server_port, () => {
  console.log(`server_listening_on_${server_port}`);
});