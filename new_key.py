from django.core.management import utils

# generates a new session key for 
# django project , prints to console

print(utils.get_random_secret_key())