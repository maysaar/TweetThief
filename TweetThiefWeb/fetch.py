import requests

url = "https://api.twitter.com/2/users/by/username/aoc"

payload={}
headers = {
  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMNNZQEAAAAAOGQZ3ErmQqqkvKKbvs%2FTnVwE51I%3D4VHazaBOjRjYQg8thhuj94iSEqNEO88yuBJHcl0CYtGr8iKnnh',
  'Cookie': 'guest_id=v1%3A164789191823222308; guest_id_ads=v1%3A164789191823222308; guest_id_marketing=v1%3A164789191823222308; personalization_id="v1_HjdCxxcRURZKj1h2kRJDKA=="'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)