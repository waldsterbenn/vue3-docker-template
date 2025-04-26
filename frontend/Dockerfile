FROM node:latest

WORKDIR /app
COPY package.json ./
RUN yarn install --ignore-engines

COPY . .

#EXPOSE 8080

CMD ["yarn", "serve"]