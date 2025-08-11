FROM node

WORKDIR /app

COPY package.json .

RUN npm install

ARG DEFAULT_PORT=80

COPY . .

ENV PORT=${DEFAULT_PORT}

EXPOSE ${PORT}

CMD ["node", "server.js"]