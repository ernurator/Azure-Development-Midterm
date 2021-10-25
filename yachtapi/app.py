import json

from flask import Flask, redirect, request, render_template

from forms.yacht import YachtForm
from db import client as cosmos_client, blob_storage, models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'APP_SECRET_KEY'


@app.route('/yachts', methods=['GET'])
def get_yachts():
    yachts = cosmos_client.get_yachts()
    return json.dumps(yachts)


@app.route('/yachts/add', methods=['POST'])
def create_yacht():
    form = YachtForm()
    if form.validate_on_submit() or 1:
        yacht = models.Yacht.from_form(form)
        front_image_url = blob_storage.upload_image(request.files['front-photo'])
        side_image_url = blob_storage.upload_image(request.files['side-photo'])
        yacht.set_images(front_image_url, side_image_url)
        cosmos_client.create_yacht(yacht.to_dict())
        return str(yacht.to_dict())
    return redirect('/yachts')


@app.route('/yachts/<yacht_name>/<yacht_id>', methods=['GET'])
def get_yacht(yacht_name, yacht_id):
    yacht_id = str(yacht_id)
    yacht_json = cosmos_client.get_yacht(yacht_id, yacht_name)
    return render_template('yacht.html', yacht=yacht_json)
