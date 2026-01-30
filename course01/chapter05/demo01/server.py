from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """处理GET请求"""
        # 设置响应状态码
        self.send_response(200)
        # 结束头部设置
        self.end_headers()
        # 写入body，设置响应体
        self.wfile.write(b"docker_windows_network_ok")


if __name__ == "__main__":
    # 创建HTTP服务
    server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
    # 启动HTTP服务
    server.serve_forever()