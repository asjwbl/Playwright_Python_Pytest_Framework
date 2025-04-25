from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class LinkComponent(BaseComponent):
    """
    LinkComponent class to handle link interactions such as clicking and retrieving the URL.
    It extends BaseComponent and adds functionality specific to link elements.
    """

    def __init__(self, page: Page, locator: str | Locator):
        """
        Initializes the LinkComponent with a locator.

        Args:
            page (Page): The Playwright Page object representing the browser tab.
            locator (str | Locator): The locator for the link element.
        """
        super().__init__(page, locator)

    def click(self) -> None:
        """
        Clicks the link. Playwright automatically waits for the link to be visible and enabled.
        """
        self.locator.click()

    def get_href(self) -> str:
        """
        Retrieves the 'href' attribute (URL) of the link.

        Returns:
            str: The URL of the link.

        Raises:
            ValueError: If the href attribute is missing.
        """
        href = self.locator.get_attribute("href")
        if href is None:
            raise ValueError("The href attribute is missing from the link.")
        return href

    def get_text(self) -> str:
        """
        Retrieves the text content of the link.

        Returns:
            str: The text content of the link.
        """
        return self.locator.inner_text()

    def right_click(self) -> None:
        """
        Performs a right-click action on the link.
        """
        self.locator.click(button="right")
