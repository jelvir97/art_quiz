import json
from openai import OpenAI
from django.conf import settings
client = OpenAI(api_key=settings.OPENAI_KEY)

def generate_answers(title, artist_title, date_display, place_of_origin):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a multiple choice generator. You will be given a title, artist_title, date_display, and place_of_origin all separated by commas. You will then give me a list of 3 additional choices for each field given, including the original. Make key names singular."},
            {
                "role": "user",
                "content": f'{title}, {artist_title}, {date_display}, {place_of_origin} json.'
            }
        ],
        response_format = { "type": "json_object" }
    )
    return json.loads(completion.choices[0].message.content)
