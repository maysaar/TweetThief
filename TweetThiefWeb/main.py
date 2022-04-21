from flask import Flask, render_template, request
import requests
# import gpt_2_simple as gpt2
# from datetime import datetime
# from google.colab import files


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
    username = request.form.get("usernames")
    data = {
        "username" : username
    }
    return render_template('tweet.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)