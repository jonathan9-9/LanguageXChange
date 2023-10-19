# base image
FROM node:14

# working dir
WORKDIR /ghi

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
