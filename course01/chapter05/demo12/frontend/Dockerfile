FROM zhangdapeng520/vue:node22.22.0-slim AS build

WORKDIR /app

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --prefer-offline

COPY . .
RUN pnpm run build


FROM nginx:1.26-alpine

# 覆盖 nginx 默认配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 拷贝构建后的前端文件
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
