# node base image
FROM node:14

# copy in package json
COPY package*.json ./

# isnstall dependencies
RUN npm install

# build
RUN npm run build

# copy setup
COPY --from=0 /app/build /usr/share/nginx/html

# start nginx
CMD ["nginx", "-g", "daemon off;"]
