# Notebook

This is my approach to building a local notebook (or one for github-pages), that can be used in day-to-day work.

> IMPORTANT! I'm actively working on the scripts to support this (marp, encode), and they may not behave as expected!! I would recommend avoiding marp for now.

## Setup

```shell
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## For marp support

```shell
pip install -e .
npm install -g @marp-team/marp-cli
```

## mkdocs

To execute the mkdocs notebook for development of content:

```shell
mkdocs serve
```
The build the site for rendering through a web server, or to use with the FastAPI runner:

```shell
mkdocs build
```

## FastAPI

A minimal FastAPI script (`main.py`) is provided to serve the site directory after the site is built.

```shell
fastapi dev main.py
```