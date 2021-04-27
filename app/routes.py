import requests
from bs4 import BeautifulSoup
from flask import request
from app import app


@app.route('/<string:avatar_uuid>', methods=['POST'])
def getpic(avatar_uuid):    
    profile_url = 'http://world.secondlife.com/resident/' + avatar_uuid
    
    req = requests.get(profile_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    pic_uuid = soup.find("meta", {"name":"imageid"})['content']
    return str(pic_uuid)