import os

# APP_ENV environment variable determines environment
# (development, staging, production)
app_env = os.getenv("APP_ENV", "development")
# TODO, raise custom exception rather than having a default.

# Common settings always applied
from proj.settings.common import *

# Apply environment specific settings
if app_env == "development":
	from proj.settings.development import *
elif app_env == "staging":
	from proj.settings.staging import *
elif app_env == "production":
	from proj.settings.production import *
else:
	pass
	# TODO raise invalid environment variable value exception.

