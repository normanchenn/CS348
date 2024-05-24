# node base image
FROM node:14

# copy in package json
COPY package*.json ./

# isnstall dependencies
RUN npm install

# build
# RUN npm run build

# start nginx
CMD ["nginx", "-g", "daemon off;"]
