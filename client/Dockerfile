FROM node:20 AS development

WORKDIR /code

# Copy everything except the src directory, which will be accessed via a volume in compose.yml
COPY package.json .
COPY package-lock.json .
COPY vite.config.js .
COPY index.html .
COPY .eslintrc.cjs .
COPY public .
COPY .env.local .

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "dev"]
