FROM node:18.14.2-alpine3.17

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

# Build-time variable
ARG REACT_APP_MOVIE_API_URL
ENV REACT_APP_MOVIE_API_URL=$REACT_APP_MOVIE_API_URL

# Build React app (env injected here)
RUN npm run build

RUN npm install -g serve

EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
