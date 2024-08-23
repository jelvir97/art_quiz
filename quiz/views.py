from django.http import HttpResponse
from .aic_client import AIC_Client
from .openai_client import generate_answers
import json

# Create your views here.

def generate_artwork_questions(request):
    """
        View function for /quiz

        Returns: artwork details
    """

    # Requests Random Artwork from AIC
    artwork_details = AIC_Client.get_artwork_details()

    # Requests answer choices form OpenAI,
    answer_options = generate_answers(artwork_details['title'], artwork_details['artist_title'], artwork_details['date_display'], artwork_details['place_of_origin'])
    artwork = {
        "details": artwork_details,
        "answers": answer_options
    }
    return HttpResponse(json.dumps(artwork))

def artwork_by_query(request, query):
    """
        View function for /search/:query

        Returns 5 artworks based on query
    """
    artworks =  AIC_Client.get_artworks_by_query(query)
    
    return HttpResponse(json.dumps(artworks))