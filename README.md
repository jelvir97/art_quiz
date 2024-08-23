# Art Quiz App

Simple quiz app that asks what the place of origin, date created, artist, and title are for a random artwork. All artwork is sourced form the Art Institute of Chicago's *[API](https://api.artic.edu/docs/#get-vs-post)*.

## Back-End Stack

- Django
- OpenAI client

## Routes

### /quiz

Returns JSON object with artwork details and additional answer options

### /search/:query

Returns results 5 results based off of query as a JSON object.

## To Run

        pip install --user pipenv

        pipenv install

        pipenv shell

        python manage.py runserver
