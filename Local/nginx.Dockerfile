FROM nginx:1.21.1-alpine
COPY website/ /usr/share/nginx/html
COPY nginx-conf/nginx.conf /etc/nginx/nginx.conf