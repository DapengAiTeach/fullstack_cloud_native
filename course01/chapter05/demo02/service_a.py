from http.server import HTTPServer, BaseHTTPRequestHandler


class ServiceAHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """处理GET请求"""
        # 设置响应状态码
        self.send_response(200)
        self.end_headers()
        # 设置响应体
        self.wfile.write(b"service_a_ok")


if __name__ == "__main__":
    # 创建HTTP服务
    server = HTTPServer(("0.0.0.0", 9001), ServiceAHandler)
    # 启动HTTP服务
    server.serve_forever()