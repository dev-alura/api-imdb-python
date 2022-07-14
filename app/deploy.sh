#!/bin/zsh
python -m pip install --upgrade pip
pip install -r app/requirements.txt

if [ ! -f app/.env ]; then
    touch app/.env
    echo 'HOST_IMDB=https://imdb-api.com' >> app/.env
    echo 'API_KEY=' >> app/.env
fi