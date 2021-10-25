
FROM python:3.9.7-slim-buster AS development_build

# System deps
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    firefox-esr \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN adduser app
WORKDIR /home/app/code
RUN chown app:app /home/app/code
USER app

ENV PATH="/home/app/.poetry/bin:/home/app/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
RUN mkdir /home/app/bin

# Installing `poetry` package manager:
# https://github.com/python-poetry/poetry
RUN curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
  && poetry --version

# Installing geckodriver
RUN curl -sL https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz -o geckodriver-v0.30.0-linux32.tar.gz \
  && tar -xvf geckodriver-v0.30.0-linux32.tar.gz \
  && mv geckodriver /home/app/bin \
  && rm geckodriver-v0.30.0-linux32.tar.gz

COPY --chown=app:app . /home/app/code

RUN poetry install

ENV DISPLAY=:99

CMD bash -c 'export PATH="$PATH:$(poetry env info -p)/bin"; police_auction_watch'
