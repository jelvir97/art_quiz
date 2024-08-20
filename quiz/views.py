from django.http import HttpResponse
from .aic_client import AIC_Client
from .openai_client import generate_answers
import json

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello WOrld! I'm Juan.")

def generate_artwork_questions(request):
    artwork_details = AIC_Client.get_artwork_details()
    answer_options = generate_answers(artwork_details['title'], artwork_details['artist_title'], artwork_details['date_display'], artwork_details['place_of_origin'])
    artwork = {
        "details": artwork_details,
        "answers": answer_options
    }
    return HttpResponse(json.dumps(artwork).encode('utf-8').decode('unicode-escape'))

def artwork_by_query(request, query):
    artworks =  AIC_Client.get_artworks_by_query(query)
    
    return HttpResponse(json.dumps(artworks).encode('utf-8').decode('unicode-escape'))