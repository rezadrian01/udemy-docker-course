FROM node

WORKDIR /app

COPY package.json .

RUN npm install

ARG DEFAULT_PORT=8080

ENV PORT=${DEFAULT_PORT}

COPY . .

CMD [ "npm", "start" ]