"""
This code is released under the MIT License. Copyright © 2023 Henrik Kühnemann.
"""
from typing import Optional

from .webservice import webservice_factory


class PlunetAPI:
    def __init__(
        self, base_url: str, cache_wsdl: bool = True, options: Optional[dict] = None
    ):
        """
        :param base_url: Base URL for the Plunet instance.  For example, 'https://plunet_sandbox.companyname.se'
        """
        self.base_url = base_url
        self.caching_client = cache_wsdl
        self._services = {}
        self.session_uuid = None
        self.options = options if options else {}

    def __repr__(self) -> str:
        """
        :returns: A str representing the Plunet instance.
        """
        return f"{self.__class__.__qualname__}(base_url='{self.base_url}')"

    def __str__(self) -> str:
        """
        Returns user-readable str with version and base url of the Plunet instance.
        :returns: A user-readable str with version and base url of the Plunet instance.
        """
        try:
            return f"Plunet v{self.plunet_version} @ {self.base_url}"
        except:
            return f"PlunetAPI v{self.api_version} @ {self.base_url} - BusinessManager 8.20 or older"

    @property
    def api_version(self) -> float:
        """
        Exposing the version of the PlunetAPI
        :return: Float representing the version the PlunetAPI
        """
        return self.PlunetAPI.getVersion()

    @property
    def plunet_version(self) -> float:
        """
        Exposing the version of the Plunet BusinessManager
        :return: Float representing the version the PlunetAPI
        """
        return self.PlunetAPI.getPlunetVersion().data

    @property
    def PlunetAPI(self):
        """
        Methods: getVersion(), login(user, pw), logout(uuid), validate(uuid, user, pw)

        :return: PlunetAPI service.
        """
        name = "PlunetAPI"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataAdmin30(self):
        """
        Check Plunet API docs for methods.

        :return: DataAdmin30 service.
        """
        name = "DataAdmin30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataCreditNote30(self):
        """
        Check Plunet API docs for methods.

        :return: DataCreditNote30 service.
        """
        name = "DataCreditNote30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataCustomer30(self):
        """
        Check Plunet API docs for methods.

        :return: DataCustomer30 service.
        """
        name = "DataCustomer30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataCustomerAddress30(self):
        """
        Check Plunet API docs for methods.

        :return: DataCustomerAddress30 service.
        """
        name = "DataCustomerAddress30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataCustomerContact30(self):
        """
        Check Plunet API docs for methods.

        :return: DataCustomerContact30 service.
        """
        name = "DataCustomerContact30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataCustomFields30(self):
        """
        Check Plunet API docs for methods.

        :return: DataCustomFields30 service.
        """
        name = "DataCustomFields30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataDocument30(self):
        """
        Check Plunet API docs for methods.

        :return: DataDocument30 service.
        """
        name = "DataDocument30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataItem30(self):
        """
        Check Plunet API docs for methods.

        :return: DataItem30 service.
        """
        name = "DataItem30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataJob30(self):
        """
        Check Plunet API docs for methods.

        :return: DataJob30 service.
        """
        name = "DataJob30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataJobRound30(self):
        """
        Check Plunet API docs for methods.

        :return: DataJobRound30 service.
        """
        name = "DataJobRound30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataOrder30(self):
        """
        Check Plunet API docs for methods.

        :return: DataOrder30 service.
        """
        name = "DataOrder30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataOutgoingInvoice30(self):
        """
        Check Plunet API docs for methods.

        :return: DataOutgoingInvoice30 service.
        """
        name = "DataOutgoingInvoice30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataPayable30(self):
        """
        Check Plunet API docs for methods.

        :return: DataPayable30 service.
        """
        name = "DataPayable30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataQuote30(self):
        """
        Check Plunet API docs for methods.

        :return: DataQuote30 service.
        """
        name = "DataQuote30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataRequest30(self):
        """
        Check Plunet API docs for methods.

        :return: DataRequest30 service.
        """
        name = "DataRequest30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataResource30(self):
        """
        Check Plunet API docs for methods.

        :return: DataResource30 service.
        """
        name = "DataResource30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataResourceAddress30(self):
        """
        Check Plunet API docs for methods.

        :return: DataResourceAddress30 service.
        """
        name = "DataResourceAddress30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataResourceContact30(self):
        """
        Check Plunet API docs for methods.

        :return: DataResourceContact30 service.
        """
        name = "DataResourceContact30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def DataUser30(self):
        """
        Check Plunet API docs for methods.

        :return: DataUser30 service.
        """
        name = "DataUser30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def ReportCustomer30(self):
        """
        Use factory.SearchFilter_Customer() to return a SearchFilter_Customer object for use in search() method.
        :return: ReportCustomer30 service
        """
        name = "ReportCustomer30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def ReportJob30(self):
        """
        Check Plunet API docs for methods.

        :return: ReportJob30 service.
        """
        name = "ReportJob30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]

    @property
    def RequestDocText30(self):
        """
        Check Plunet API docs for methods.

        :return: RequestDocText30 service.
        """
        name = "RequestDocText30"
        try:
            return self._services[name]
        except KeyError:
            self._services[name] = webservice_factory(
                self.base_url, name, self.caching_client, **self.options
            )
            return self._services[name]
