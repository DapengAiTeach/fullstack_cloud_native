import axios from 'axios';

// axios 实例，配置基础 URL 和超时时间
const http = axios.create({
  baseURL: 'http://localhost:8000', // 后端 API 的基础 URL
  timeout: 5000,
});


// 用户注册
export const registerUser = async (username, password) => {
  const response = await http.post('/register/', { 
    username, 
    password,
  });
  return response.data;
}

// 用户登录
export const loginUser = async (username, password) => {
  const response = await http.post('/login/', { 
    username, 
    password,
  });
  return response.data;
}