import json
from openai import OpenAI
from django.conf import settings
client = OpenAI(api_key=settings.OPENAI_KEY)


def generate_answers(title, artist_title, date_display, place_of_origin):
    """
    Sends correct quiz answers to OpenAI to generate additional wrong choices.

    Args: title, artist_title, date_display, place_of_origin

    Returns : JSON object of choices, including the original.
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a multiple choice generator. You will be given a title, artist_title, date_display, and place_of_origin all separated by commas. You will then give me a list of 3 additional choices for each field given, including the original. Make key names singular. The keys must be: title, artist_title, date_display, and place_of_origin"},
            {
                "role": "user",
                "content": f'{title}, {artist_title}, {date_display}, {place_of_origin} json.'
            }
        ],
        response_format = { "type": "json_object" }
    )
    return json.loads(completion.choices[0].message.content)
