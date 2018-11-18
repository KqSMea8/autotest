import copy
from ApiHelp.config import conf

def get(key):
	r = copy.deepcopy(api[key])
	if 'http' in r['address']:
		return r
	r['address'] = conf.Domain + r['address']

	return r


api = {}
# api[''] = {'address':'','method':'post','desc':''}
api['GaHotelPolicy'] = {'address':'globalapibooking/GaHotelPolicy','method':'post','desc':'globalapibooking GaHotelPolicy'}
api['GaHotelSingle'] = {'address':'globalapibooking/GaHotelSingle','method':'post','desc':'globalapibooking GaHotelSingle'}
api['GaHotelSearch'] = {'address':'globalapibooking/GaHotelSearch','method':'post','desc':'globalapibooking GaHotelSearch'}
api['HotelSearchService'] = {'address':'GlobalAPIBooking/xml/HotelSearchService','method':'post','desc':'GlobalAPIBooking/xml/HotelSearchService'}
api['GaCreateOrder'] = {'address':'globalapibooking/GaCreateOrder','method':'post','desc':'GlobalAPIBooking/GaCreateOrder'}
api['GaHotelAvail'] = {'address':'globalapibooking/GaHotelAvail','method':'post','desc':'globalapibooking/GaHotelAvail'}
