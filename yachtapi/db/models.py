import uuid


class Yacht:
    SAS_FOR_IMAGES = '?sp=r&st=2021-10-25T16:16:44Z&se=2021-11-26T00:16:44Z&spr=https&sv=2020-08-04&sr=c&sig=3hbQPrDRdCISge3GtwTPfhHD8Ry3D32sP%2FJneHRC4v4%3D'
    SAS_FOR_THUMBNAILS = '?sp=r&st=2021-10-25T16:19:30Z&se=2021-11-26T00:19:30Z&spr=https&sv=2020-08-04&sr=c&sig=fHdo0tbqKRowulpHVej%2FPwMvfTugtFBDHH6%2B7PW5mtw%3D'

    def __init__(
            self,
            name,
            length,
            length_waterline,
            width,
            precipitation,
            displacement,
            engine,
            sleeping_places,
            water_volume,
            fuel_volume,
            sailing_area,
            id=None
    ):
        self.name = name
        self.length = length
        self.length_waterline = length_waterline
        self.width = width
        self.precipitation = precipitation
        self.displacement = displacement
        self.engine = engine
        self.sleeping_places = sleeping_places
        self.water_volume = water_volume
        self.fuel_volume = fuel_volume
        self.sailing_area = sailing_area
        self.front_photo = ''
        self.side_photo = ''
        self.front_photo_thumbnail = ''
        self.side_photo_thumbnail = ''
        if id:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'length': self.length,
            'length_waterline': self.length_waterline,
            'width': self.width,
            'precipitation': self.precipitation,
            'displacement': self.displacement,
            'engine': self.engine,
            'sleeping_places': self.sleeping_places,
            'water_volume': self.water_volume,
            'fuel_volume': self.fuel_volume,
            'sailing_area': self.sailing_area,
            'front_photo': self.front_photo,
            'side_photo': self.side_photo,
            'front_photo_thumbnail': self.front_photo_thumbnail,
            'side_photo_thumbnail': self.side_photo_thumbnail
        }
    
    @classmethod
    def from_form(cls, form, id=None):
        new_pet = cls(
            name=form.name.data,
            length=form.length.data,
            length_waterline=form.length_waterline.data,
            width=form.width.data,
            precipitation=form.precipitation.data,
            displacement=form.displacement.data,
            engine=form.engine.data,
            sleeping_places=form.sleeping_places.data,
            water_volume=form.water_volume.data,
            fuel_volume=form.fuel_volume.data,
            sailing_area=form.sailing_area.data,
            id=id)
        return new_pet

    def set_images(self, front_image_url, side_image_url):
        self.front_photo = front_image_url + self.SAS_FOR_IMAGES
        self.side_photo = side_image_url + self.SAS_FOR_IMAGES
        self.front_photo_thumbnail = front_image_url.replace('/images/', '/thumbnails/') + self.SAS_FOR_THUMBNAILS
        self.side_photo_thumbnail = side_image_url.replace('/images/', '/thumbnails/') + self.SAS_FOR_THUMBNAILS
