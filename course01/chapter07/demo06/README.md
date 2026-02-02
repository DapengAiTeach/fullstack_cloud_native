# Docker+JavaScript+Vue3项目

## Docker部署
构建：
```bash
docker build -t vue3 .
```

启动容器：
```bash
docker run -d -p 8080:80 vue3
```