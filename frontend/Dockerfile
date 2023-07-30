FROM node:20.2.0-alpine3.17 as build

WORKDIR /frontend

COPY package*.json /frontend/

RUN npm install

COPY ./ /frontend/

RUN npm run build

FROM nginx:1.23.0-alpine

COPY --from=build /frontend/build/ /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY ../nginx/nginx.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]