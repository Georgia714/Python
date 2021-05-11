from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return """<h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friends:</p>
  <ul><li><a href='/animals/dogs'>Dogs</a></li><li><a href='/animals/cats'>Cats</a></li><li><a href ='/animals/rabbits'>Rabbits</a></li></ul>"""

@app.route('/animals/<pet_type>')
#@app.route('/animals/<pet_type>/<int:index>')
def animals(pet_type):
  html = f"List of {pet_type}"
  html += "<ul>"
  for count, value in enumerate(pets[pet_type]):
    pet_id = count
    pet_name = value['name'] 
    html += f"<li><a href = '/animals/{pet_type}/{pet_id}'>{pet_name}</a></li>"
  html += "</ul>"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  pet_name = pet['name']
  return f"""<h1>{pet['name']}</h1><p>{pet['description']}</p><ul><li>Age: {pet['age']}</li><li>Breed: {pet['breed']}</li></li></ul><img src={pet['url']}>"""

