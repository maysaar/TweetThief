from flask import Flask, render_template, request
import requests
import gpt_2_simple as gpt2
from datetime import datetime
from generateTweet import *


app = Flask(__name__)

payload={}
headers = {
  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMNNZQEAAAAAOGQZ3ErmQqqkvKKbvs%2FTnVwE51I%3D4VHazaBOjRjYQg8thhuj94iSEqNEO88yuBJHcl0CYtGr8iKnnh',
  'Cookie': 'guest_id=v1%3A164789191823222308; guest_id_ads=v1%3A164789191823222308; guest_id_marketing=v1%3A164789191823222308; personalization_id="v1_HjdCxxcRURZKj1h2kRJDKA=="'
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tweet', methods=["GET", "POST"])
def tweet():
    returntext = ''
    username = request.form.get("usernames")
    if username == "@LindseyGrahamSC":
        returntext = generator('lg')
    elif username == "@AOC":
        returntext = generator('aoc')
    elif username == "@BernieSanders":
        returntext = generator('bernie')
    elif username == "@BarackObama":
        returntext = generator('obama')
    elif username == "@BillGates":
        returntext = generator('bill')
    elif username == "@LeoDiCaprio":
        returntext = generator('leo')
    elif username == "@VanderbiltU":
        returntext = generator('vandy')
    elif username == "@melindagates":
        returntext = generator('melinda')
    elif username == "@MarshaBlackburn":
        returntext = generator('marsha')
    elif username == "@SpeakerPelosi":
        returntext = generator('nancy')
    elif username == "@BorisJohnson":
        returntext = generator('boris')
    elif username == "@GavinNewsom":
        returntext = generator('gavin')

    data = {
        "username" : username,
        "tweet" : returntext
    }
    return render_template('tweet.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)