from private.config import (
    CSRF_SECRET_KEY,
    STORMPATH_API_KEY_FILE,
    FACEBOOK_APP_ID,
    FACEBOOK_APP_SECRET,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET
)

import os




class Config(object):
	DEBUG = True
	CSRF_SECRET_KEY = CSRF_SECRET_KEY
	

class DevConfig(Config):
	SECRET_KEY = "Mydevelopmentsecretkey"
	MONGODB_SETTINGS = {
		"db": "cthulhu_devel"
	}


class ProdConfig(Config):
	SECRET_KEY = os.environ.get("SECRET_KEY", "sdjsadd32332fdu398d3fjqf93qj0jfsalsjSDJQOWRJ3OFWQ")
	STORMPATH_API_KEY_FILE = STORMPATH_API_KEY_FILE
	FACEBOOK_APP_SECRET = FACEBOOK_APP_SECRET
	GOOGLE_CLIENT_SECRET = GOOGLE_CLIENT_SECRET
	GOOGLE_CLIENT_ID = GOOGLE_CLIENT_ID
	MONGODB_SETTINGS = {
		"db": "cthulhu"
	}


config = {
	"default": DevConfig,
	"dev": DevConfig,
	"Prod": ProdConfig
}
