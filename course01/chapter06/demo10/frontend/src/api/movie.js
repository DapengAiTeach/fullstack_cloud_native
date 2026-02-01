import http from "@/utils/http";

// 获取电影列表
export function fetchMovieList(params) {
    return http.get("/movies/", { params });
}

// 新增电影
export function addMovie(data) {
    return http.post("/movies/", data);
}

// 更新电影
export function updateMovie(id, data) {
    return http.put(`/movies/${id}/`, data);
}

// 删除电影
export function deleteMovie(id) {
    return http.delete(`/movies/${id}/`);
}

// 获取单个电影详情
export function fetchMovieDetail(id) {
    return http.get(`/movies/${id}/`);
}