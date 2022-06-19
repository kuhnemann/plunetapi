from urllib.parse import urljoin

from zeep import CachingClient


def webservice_factory(base_url: str, wsdl_name: str):
    return WebService(base_url=base_url, wsdl_name=wsdl_name)


class WebService:
    """
    Class to expose Plunet Web Service API Services.
    """

    def __init__(self, wsdl_name: str, base_url: str):
        """
        :param base_url: Base URL of the Plunet Web Service API, as a string.
        """
        self.base_url = base_url
        self.service_url = urljoin(self.base_url, f"/{wsdl_name}?wsdl")
        self._client = CachingClient(wsdl=self.service_url)

    def __dir__(self) -> list:
        """
        Replacing to forward attribute lookups to the underlying CachingClient, hence making attributes of the client available.
        :returns: Attributes, as list of strings.
        """
        return sorted(set(list(self.__dict__.keys()) + self._client.service.__dir__()))

    def __getattr__(self, item):
        """
        For forwarding attribute lookups to the underlying client service.
        :param item: Attribute to fetch.
        """
        return getattr(self._client.service, item)

    @property
    def factory(self):
        """
        Method to expose the zeep factory from the underlying client as a property of the service instance.

        Useful both for exploration and in controllers.
        :return: Zeep type factory for the WSDL.
        """
        return self._client.type_factory("ns0")
