from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SubmitField


class YachtForm(FlaskForm):
    name = StringField('Yacht name')
    length = IntegerField('Length ‎‎of yacht full')
    length_waterline = IntegerField('Length on waterline')
    width = IntegerField('‎‎Yacht ‎‎width')
    precipitation = IntegerField('‎‎Yacht precipitation')
    displacement = IntegerField('Water displacement')
    engine = StringField('Engine')
    sleeping_places = IntegerField('Sleeping places')
    water_volume = IntegerField('Water tank volume')
    fuel_volume = IntegerField('Fuel tank volume')
    sailing_area = IntegerField('Total sailing area')
    front_photo = FileField('Front photo')
    side_photo = FileField('Side photo‎')
    submit = SubmitField('Submit')
