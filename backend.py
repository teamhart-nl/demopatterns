from requests import Session
import requests
from registerer import register

class BackendHandler:
    """Handles the encoding of the current entries."""
  
    # Settings
    update_hz = 1 # Per second
    port = 8000
    debug = False

    # Session
    __session__ = Session()
    __session__.headers.update({'Content-Type' : 'application/json'})	

    def __init__(self, **kwargs):

        # Check connection
        try:
            register(api_url = "http://localhost:" + str(self.port) + "/patterns")
        except Exception as e:
            print("BackendHandler Setup Failed: " + str(e))
            input("Press enter to retry starting BackendHandler...")
            self.__init__(**kwargs)
            return

    def send(self, name: str):
        """Updates the active encodings.

        Args:
            active_encodings (list[str]): The active encodings.
        """
        try:
            if self.debug:
                print("BackendHandler Transmitting Encoding: " + str(name))
            r = self.__session__.post('http://localhost:{}/devices/pattern/'.format(self.port), json={'pattern_name': name})
            if r.status_code != requests.codes.ok:
                print("BackendHandler Error: " + str(r.status_code))
        except Exception as e:
            print("BackendHandler Error: " + str(e))
            input("Press enter to continue updating BackendHandler...")