import json

from lib.action import InfobloxBaseAction
from st2client.client import Client
from st2client.models import KeyValuePair


class InfobloxBaseGetAction(InfobloxBaseAction):
    """Base get action"""

    def run(self, endpoint_uri, **kwargs):
        """Base get action
        endpoint_uri is pased from metadata file
        """
        return self.get(endpoint_uri, **kwargs)
