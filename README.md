# FastAPI and Svelte tutorial

## Introduction and Motivation
This is a simple example of using FastAPI with an ML model. Our actual implementation will vary from it, but this is a good starting point. By the end of this tutorial, you should be comfortable with FastAPI and Svelte.

We'll build a simple website that takes in some text and returns whether that text was positive or negative (sentiment analysis). Note that there are significantly simpler ways of doing this (using Streamlit, for instance). However, those easier methods won't work for our actual project (which requires a much higher level of customization), so we'll use Svelte and FastAPI.

- FastAPI is a python framework for building APIs. It's fast, easy to use, and has great documentation. It's also very popular, so there are a lot of resources online. 

- Svelte is a javascript framework for building websites. Svelte is easy to use and really fast. It has great documentation available as well. More importantly, Svelte is much more recent than React or Vue - meaning that most Svelte code available online is written either by the svelte team or by early adopters that write good code. For us, this means tools like ChatGPT are much more likely to spit out correct Svelte code than React or Vue code. It took 3 prompts to get the Svelte code for this website, compared to over 5 for React which still messed up. (Note: I'm not saying React or Vue are bad, just that GPT is better at Svelte)

## Setup
Setup a python virtual environment and install the requirements:

- <code>python3 -m venv venv</code>
- <code>source venv/bin/activate</code>
- <code>pip install -r requirements.txt</code>

Note: At this point, everyone must be comfortable with python, pip, and venv. If you're not, just search it up online. We'll be using python 3.11, but any version of python 3 should work. 

Make sure you have svelte installed. It's pretty simple to install, just follow the instructions [here](https://svelte.dev/blog/svelte-for-new-developers).


## Model - sentiment analysis

We'll use an out of the box sentiment analysis model - [VADER sentiment analysis](https://github.com/cjhutto/vaderSentiment). Given a sentence, we'll simply return it's compound score. The implementation can be found in <code>sentiment.py</code>. This is not really the important part of this example - we'll be working with much more sophisticated models in our actual project.

## Backend - FastAPI

The backend is a FastAPI server. The code for the backend can be found in <code>main.py</code>. It imports the sentiment analysis model from <code>sentiment.py</code>. Note that for our website, we'll take in a sentence, and output the sentiment scores in a bar-style fashion. So, the frontend only needs access to the sentiment scores for a particular sentence - this can be done via a single GET request.

In python: we can write a function that, given a sentence, returns the sentiment score for that sentence.  If we just decorate this function with <code>app.get(route)</code>, we've created a GET endpoint. The route is the url that we'll use to access the endpoint. For example, if we set the route to <code>/sentiment</code>, we can access the endpoint at <code>[some IP address]/sentiment</code>. For our function, since it takes in a variable (the sentence), we'll have to add a path parameter to the route. This is done by adding <code>{sentence}</code> to the route. So, our final route will be <code>/sentiment/{sentence}</code>. The variable name in the route must match the variable name in the function definition - this is how FastAPI knows what to pass to the function.

Note: In the implementation, I've wrapped the score in a pydantic object. You could also just return a dictionary, but FastAPI has some nice features (like automatic data validation and json conversion) for pydantic objects - we will be using pydantic (and typing!) in our actual project as well.

## Frontend - Svelte

The advantage of using svelte is that the templates are great and ChatGPT becomes a really useful resource. To start a svelte project, run <code>npx degit sveltejs/template [svelte project name]</code>. Correctly prompting ChatGPT will give you most of the code you can see inside the svelte-sentiment-app directory. I won't pretend to be an expert on it - I have very limited frontend experience but for 5 minutes of work, the website doesn't look bad.


## Run
1. To run the backend, run <code>uvicorn main:app --reload</code>. 
2. In a separate terminal, <code>cd</code> to <code>svelte-sentiment-app</code>. Run <code>npm run dev</code>. This will start the frontend server.

Note that we call <code>main:app</code> in the command above because we called the FastAPI instance <code>app</code> in <code>main.py</code>. The colon kind of works similar to an import statement (this would be analogous to <code>from main import app</code> in python). If you change the name of the FastAPI instance, you'll have to change the command above. 

Optional Note: FastAPI utilizes uvicorn to run it's server. Uvicorn is a fast ASGI server. ASGI is a protocol that allows for asynchronous communication between the server and the client. This is important because it allows for the server to handle multiple requests at once. This is important for our actual project because we'll be using a recommendation enginer, which can take a long time to run. If we didn't use ASGI, the server would be blocked while the model was running, and no other requests could be handled. This comes in clutch especially when we're handling multiple users at once.