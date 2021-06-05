import secrets
import requests

from flask import Blueprint, request, make_response, jsonify, redirect


shortlinks_blueprint = Blueprint('shortlinks', __name__, url_prefix='/shortlinks')
LINKS = {}
URL = "http://127.0.0.1:5000/shortlinks/link/"

def is_valid_url(url):
    if "http://" not in url:
        url = "http://"+url
    request = requests.get(url)
    if request.status_code == 200:
        return True
    else:
        return False


def generate_slug():
    return secrets.token_hex(3)


@shortlinks_blueprint.route('/',methods=['GET','POST'])
def shortlinks():

    # handle create shortener URL
    if request.method == 'POST':
        
        slug = generate_slug()
        LINKS[slug] = request.get_json().get('link')
        
        if not is_valid_url(LINKS[slug]):
            response = {
                "status": "fail",
                "message": "Please add a valid Link"
                }
            return make_response(jsonify(response)), 400
        
        response = {
                "status": "success",
                "message": "The short link has generated successfully",
                "link": URL + slug
                }   
        return make_response(jsonify(response))
    
    else:
        # Get all links
        links = []
        for slug in LINKS.keys():
            links.append(URL + slug)
        response = {
                "status": "success",
                "message": "All Links",
                "links": links 
                }
        return make_response(jsonify(response))


@shortlinks_blueprint.route('/link/<slug>')
def user_link(slug):
    # redirect user
    link = LINKS.get(slug)
    if link:
        
        return redirect(link, code=301)

    response = {
                "status": "fail",
                "message": "Not a valid Link"
                }
    return make_response(jsonify(response)), 404
