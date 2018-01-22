from lib.action import InfobloxBaseAction


class InfobloxBasePatchAction(InfobloxBaseAction):
    """Base patch action"""

    def run(self, endpoint_uri, **kwargs):
        """Base patch action
        endpoint_uri is pased from metadata file
        """
        return self.patch(endpoint_uri, **kwargs)
