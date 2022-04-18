from pyowm import OWM

owm = OWM('bea3a86964e0b0e3e38b675d924fa732')
reg = owm.city_id_registry()
list_of_geopoints = reg.geopoints_for('Rome', matching='exact')
















