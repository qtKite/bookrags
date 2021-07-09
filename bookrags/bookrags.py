import re
import requests
from bookrags import urls
from bookrags import product
from bookrags.lens import Lens
from bookrags.product import ProductType, Product

# Automatically navigate to the study guide page
# Query what pages there are


class BookRags:
    """
    Interface class for communicating with the API
    """

    def __init__(self, username, password) -> None:
        self.__details = {
            'edEmailOrName': username,
            'edPW': password
        }
        self.__session = requests.Session()
        self.__login()

    def __login(self):
        """
        Authenticates the current session using the given details
        """
        self.__session.post(
            urls.LOGIN_URL,
            data=self.__details)

    def is_logged_in(self):
        """
        Checks if the current session is signed in
        """
        check = self.__session.get(
            urls.ACCOUNT_URL,
            allow_redirects=False)
        return len(check.text) > 1

    def get_session(self):
        return self.__session

    def logout(self):
        """
        Signs out of the user account from the active session
        """
        self.__session.get(urls.LOGOUT_URL)

    def resolve_link(self, link):
        """
        Given a link, it will resolve it into the study guide page
        """
        if not re.search('bookrags.com', link):
            print('bad link')
            return None
        
        print('link is valid')

        # read product type
        page = self.__session.get(link).text
        product_type = re.search('', page)

        # if we can't then this page isnt supported :c
        if not product_type:
            return None

        # we are already on the page
        if product_type == 'lens':
            return Lens()

        # visit page
        # read prodtype

    def search(self, query):
        """
        Perform a search query and return the results
        """
        pass
