from flask import Flask, render_template, request
import requests

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

@app.route('/get/')
def get_result():
    url = "https://api.twitter.com/2/users/by/username/" + request.args.get("usernames")
    response = requests.request("GET", url, headers=headers, data=payload)
    # jsonResponse = response.json
    # data = JSON.parse(jsonResponse.data)
    # if "errors" in jsonResponse:
    #     return str(response.text)
    # else:
    #     return str(response["data"])

    return str(response.text)

if __name__ == "__main__":
    app.run(debug=True)