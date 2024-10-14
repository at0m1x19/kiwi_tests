import os
from urllib.parse import urlparse

import allure


class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Hide cookie agreement banner")
    def hide_cookie_agreement_banner(self):
        self.page.context.add_cookies(
            [
                {
                    "name": "__kwc_agreed",
                    "value": 'true',
                    "domain": f"www.{urlparse(os.getenv('BASE_URL')).netloc}",
                    "path": "/",
                    "secure": True,
                }
            ]
        )

        return self
