import json
import requests
import random



# Class to make API calls to Art Institute of Chicago
class AIC_Client :
    # Returns id, title, image_id, artist display, 
    #         artist_title, description, date_display, 
    #         place_of_origin, artist_id for a random art piece.
    @staticmethod
    def get_artwork_details():
        response = requests.post('https://api.artic.edu/api/v1/artworks/search', json={
                                                                    "resources": "artworks",
                                                                    "fields": [
                                                                        "id",
                                                                        "title",
                                                                        "artist_title",
                                                                        "image_id",
                                                                        "date_display",
                                                                        "description",
                                                                        "place_of_origin",
                                                                    ],
                                                                    "boost": False,
                                                                    "limit": 1,
                                                                    "query": {
                                                                        "function_score": {
                                                                        "query": {
                                                                            "bool": {
                                                                            "filter": [
                                                                                {
                                                                                "exists": {
                                                                                    "field": "image_id"
                                                                                }
                                                                                },
                                                                                {
                                                                                "exists": {
                                                                                    "field": "thumbnail.width"
                                                                                }
                                                                                },
                                                                                {
                                                                                "exists": {
                                                                                    "field": "thumbnail.height"
                                                                                }
                                                                                }
                                                                            ]
                                                                            }
                                                                        },
                                                                        "boost_mode": "replace",
                                                                        "random_score": {
                                                                            "field": "id",
                                                                            "seed": [random.randint(1,999999)]
                                                                        }
                                                                        }
                                                                    }
                                                                    })
        return response.json()['data'][0]
    
    # Takes query argument
    # Returns artworks based on query
    @staticmethod
    def get_artworks_by_query(query):
        response = requests.get(f'https://api.artic.edu/api/v1/artworks/search?q={query}&limit=5&fields=title,image_id,id,description,date_display,artist_title')
        return response.json()['data']