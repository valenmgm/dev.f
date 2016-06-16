
import urllib

def generate_link(user):
    return 'http://www.codewars.com/users/' + urllib.quote(user)
