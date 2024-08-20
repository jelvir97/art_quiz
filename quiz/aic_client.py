import json
import requests

# Class to make API calls to Art Institute of Chicago
class AIC_Client :
    # Returns id, title, image_id, artist display, 
    #         artist_title, description, date_display, 
    #         place_of_origin, artist_id for a random art piece.
    @staticmethod
    def get_artwork_details():
        response = requests.get('https://api.artic.edu/api/v1/artworks?limit=1&fields=id,title,image_id,artist_title,description,place_of_origin,artist_display,date_display,artist_id')
        return response.json()['data'][0]
    
    # Takes query argument
    # Returns artworks based on query
    @staticmethod
    def get_artworks_by_query(query):
        response = requests.get(f'https://api.artic.edu/api/v1/artworks/search?q={query}&limit=5&fields=title,image_id,id,description,date_display,artist_title')
        return response.json()['data']