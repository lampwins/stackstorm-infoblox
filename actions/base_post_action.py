from lib.action import InfobloxBaseAction


class InfobloxBasePostAction(InfobloxBaseAction):
    """Base post action"""

    def run(self, endpoint_uri, **kwargs):
        """Base post action
        endpoint_uri is pased from metadata file
        """
        return self.post(endpoint_uri, **kwargs)
