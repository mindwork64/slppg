import requests
from bs4 import BeautifulSoup
from flask import request

from app import app


@app.route('/slppg/<string:avatar_uuid>', methods=['GET'])
def getpic(avatar_uuid):
    profile_url = 'http://world.secondlife.com/resident/' + avatar_uuid
    req = requests.get(profile_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return str(soup.find("meta", {"name":"imageid"})['content'])
