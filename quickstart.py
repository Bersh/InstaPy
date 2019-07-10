""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=".")

# get an InstaPy session!
session = InstaPy(username="tera.fufad",
                  password="sandhusohal12345",
                  headless_browser=True)

with smart_run(session):
    """ Activity flow """
    session.accept_follow_requests(amount=50)

exit()
