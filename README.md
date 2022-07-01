<div id="top"></div>


<!-- PROJECT SHIELDS -->


[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->


<h3 align="center">PlunetAPI</h3>

  <p align="center">
    Thin wrapper for the Plunet SOAP API.
    <br />


  </p>
</div>







<!-- ABOUT THE PROJECT -->

## About The Project

A thin wrapper to facilitate interactions with the PlunetAPI.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [zeep](https://docs.python-zeep.org/en/master/)
* [Plunet](https://www.plunet.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

### Installation

Clone the repo

   ```sh
   git clone https://github.com/kuhnemann/plunetapi.git
   ```

Or install via pip

   ```sh
   pip install plunetapi
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

Install using pip like so:

```sh
pip install plunetapi
```

The wrapper is thin by design and intended to be used by a client. For example something along these lines:

```sh
from plunetapi import PlunetAPI
from typing import Union, Callable

class PlunetClient:
    def __init__(self, base_url: str):
        self.plunet = PlunetAPI(base_url=base_url)
        self.uuid = None

    def login(self, username: str, password: str):
        uuid = self.plunet.PlunetAPI.login(username, password)
        if uuid == "refused":
            raise ConnectionRefusedError("Login refused")
        else:
            self.uuid = uuid

    def _make_request(self, operation_proxy: Callable, argument: Union[dict, str, int, list]):
        result = operation_proxy(self.uuid, argument)
        if result.statusCode != 0:
            raise Exception(result.statusMessage)
        else:
            return result.data

    def get_customer_object(self, customer_id: int):
        data_item = self._make_request(self.plunet.DataCustomer30.getCustomerObject, customer_id)
        return data_item

```

As a complement to the Plunet JavaDocs, use the propagated zeep factory method to explore objects as definied in the different WSDLs. For example:

```sh
plunet = PlunetAPI(base_url=base_url)
plunet.DataJob30.factory.PriceLine()
{
    'amount': None,
    'amount_perUnit': None,
    'memo': None,
    'priceLineID': None,
    'priceUnitID': None,
    'sequence': None,
    'taxType': None,
    'time_perUnit': None,
    'unit_price': None
}

```

<p align="right">(<a href="#top">back to top</a>)</p>




See the [open issues](https://github.com/kuhnemann/plunetapi/issues) for a full list of proposed features (and known
issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Henrik Kühnemann - [@hkuhnemann](https://twitter.com/hkuhnemann) - [hello@yellownape.se](mailto:hello@yellownape.se)

Project Link: [https://github.com/kuhnemann/plunetapi](https://github.com/kuhnemann/plunetapi)

<p align="right">(<a href="#top">back to top</a>)</p>



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/kuhnemann/plunetapi.svg?style=for-the-badge

[contributors-url]: https://github.com/kuhnemann/plunetapi/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/kuhnemann/plunetapi.svg?style=for-the-badge

[forks-url]: https://github.com/kuhnemann/plunetapi/network/members

[stars-shield]: https://img.shields.io/github/stars/kuhnemann/plunetapi.svg?style=for-the-badge

[stars-url]: https://github.com/kuhnemann/plunetapi/stargazers

[issues-shield]: https://img.shields.io/github/issues/kuhnemann/plunetapi.svg?style=for-the-badge

[issues-url]: https://github.com/kuhnemann/plunetapi/issues

[license-shield]: https://img.shields.io/github/license/kuhnemann/plunetapi.svg?style=for-the-badge

[license-url]: https://github.com/kuhnemann/plunetapi/blob/main/LICENCE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/henrik-kuhnemann

[product-screenshot]: images/screenshot.png