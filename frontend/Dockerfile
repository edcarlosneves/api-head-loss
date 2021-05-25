
FROM node:lts

RUN mkdir /app/
WORKDIR /app/
COPY package.json /app
RUN npm install
ADD . /app/

CMD ["npm", "run", "start"]