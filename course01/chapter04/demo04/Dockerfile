FROM node:22.22.0-slim

WORKDIR /app

COPY package.json .
COPY server.js .
RUN npm install

CMD ["npm", "run", "start"]