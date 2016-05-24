import os
from sauceclient import SauceClient

USERNAME = os.environ.get('SAUCE_USERNAME', "testuj")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "0029898f-54be-48b2-9166-9306282bef0c")
sauce = SauceClient(USERNAME, ACCESS_KEY)

USER = "patryk.bader@testuj.pl"
PASSWORD = "tester777"

USER2 = "aleksandra.mika@vazco.eu"
PASSWORD2 = "aleno101"

CHANGE_PASSWORD_USER = "testujpl@go2.pl"

# browsers = [{"platform": "Windows 8.1",
#              "browserName": "internet explorer",
#              "version": "8"},
#             {"platform": "Windows 8.1",
#              "browserName": "firefox",
#              "version": "35"}]