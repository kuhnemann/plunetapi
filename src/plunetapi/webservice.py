from urllib.parse import urljoin

from zeep import CachingClient, Client


def webservice_factory(base_url: str, wsdl_name: str, caching_client: bool = True):
    return WebService(base_url=base_url, wsdl_name=wsdl_name, caching_client=caching_client)


class WebService:
    """
    Class to expose Plunet Web Service API Services.
    """

    def __init__(self, wsdl_name: str, base_url: str, caching_client: bool = True):
        """
        :param wsdl_name: Service name - for example DataItem30
        :param base_url: Base URL of the Plunet Web Service API, as a string.
        :param caching_client: Boolean to regulate use of CachingClient or Client. Default: True
        """
        self.base_url = base_url
        self.service_url = urljoin(self.base_url, f"/{wsdl_name}?wsdl")
        if caching_client is True:
            self._client = CachingClient(wsdl=self.service_url)
        else:
            self._client = Client(wsdl=self.service_url)

    def __dir__(self) -> list:
        """
        Replacing to forward attribute lookups to the underlying Client/CachingClient,
        hence making attributes of the client available.

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
