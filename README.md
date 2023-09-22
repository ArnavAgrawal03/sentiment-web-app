# FastAPI and Svelte tutorial

This is a simple example of using FastAPI with an ML model. Our actual implementation will vary from it, but this is a good starting point. By the end of this tutorial, you should be comfortable with FastAPI and Svelte.

We'll build a simple website that takes in some text and returns whether that text was positive or negative (sentiment analysis). Note that there are significantly simpler ways of doing this (using Streamlit, for instance). However, those easier methods won't work for our actual project (which requires a much higher level of customization), so we'll use Svelte and FastAPI.

## Setup

Setup a python virtual environment and install the requirements.

Note: At this point, everyone is comfortable with python, pip, and venv. If you're not, just search it up online. We'll be using python 3.11, but any version of python 3 should work.

## Model - sentiment analysis

We'll use an out of the box sentiment analysis model. The [VADER sentiment analysis](https://github.com/cjhutto/vaderSentiment) model. Given a sentence, we'll simply return it's compound score. The implementation can be found in <code>sentiment.py</code>.
