import axios from "axios";

// 前端与后端交互的 HTTP 客户端
const http = axios.create({
    // 代理前缀
    baseURL: "/ch06_demo10_backend", 
    timeout: 10000,
});

// 响应拦截器
http.interceptors.response.use(
    (response) => {
        // 直接返回响应数据
        return response.data;
    },
    (error) => {
        // 处理响应错误
        return Promise.reject(error);
    }
);

export default http;