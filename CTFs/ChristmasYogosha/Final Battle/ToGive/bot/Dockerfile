FROM ubuntu:18.04

RUN apt update && apt install -y xvfb curl wget software-properties-common unzip
RUN add-apt-repository ppa:canonical-chromium-builds/stage
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt install -y ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils 
RUN apt install -y nodejs
RUN npm install npm@latest -g

# ^^^ chromium-browser=91.0.4472.101-0ubuntu0.18.04.1
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -

RUN useradd bot
RUN mkdir -p /bot
RUN chown bot:bot /bot

WORKDIR /bot
COPY ./bot/bot.js .
COPY ./bot/package.json .
RUN npm install
CMD xvfb-run node bot.js
