import axios from 'axios';

// axios 实例，配置基础 URL 和超时时间
const http = axios.create({
  baseURL: 'http://localhost:8000', // 后端 API 的基础 URL
  timeout: 5000,
});


// 获取商品列表
export const fetchItems = async () => {
  const response = await http.get('/items/');
  return response.data;
};