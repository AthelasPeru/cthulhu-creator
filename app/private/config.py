import os

# base dir el proyecto
BASEDIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'lsadjsa345534GERse#"$FDf'
CSRF_SECRET_KEY = 'salkddk3445sdfsd$W3$'

FACEBOOK_APP_ID = '1532899883594349'
FACEBOOK_APP_SECRET = '014b09274f5945ef03353fa9ec064d00'


# '6965526825-k5bt3od3ej9nirhvqhtv6stgolbitrie.apps.googleusercontent.com'
GOOGLE_CLIENT_ID = '473899503710-absulm8qgh0dr22vgvtsmgo0n60huva0.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '4eRKkEeFoMdaNMCneCXMqlf5'


STORMPATH_API_KEY_FILE = BASEDIR + '/apiKey.properties'
