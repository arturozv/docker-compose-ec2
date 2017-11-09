FROM node:alpine
RUN apk --no-cache add curl

ENV APP_DIR=/app
WORKDIR ${APP_DIR}
EXPOSE 8090
CMD ["npm","start"]

ADD src/package.json src/package-lock.json ${APP_DIR}/
RUN npm install

ADD src/*.js ${APP_DIR}/