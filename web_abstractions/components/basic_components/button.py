from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class ButtonComponent(BaseComponent):
    """
    ButtonComponent class to encapsulate interactions with button elements.
    This class supports initialization with any locator type (CSS/XPath/get_by* methods).
    """

    def __init__(self, page: Page, selector: str | Locator):
        """
        Initializes the ButtonComponent using different locators, including Playwright's get_by_* methods.

        :param page: The Playwright Page object representing the browser tab.
        :param selector: The locator for the button. It can be a string (CSS/XPath) or an existing Playwright Locator.
        """
        super().__init__(page, selector)

    def click(self) -> None:
        """
        Clicks on the button.
        """
        self.locator.click()

    def get_text(self) -> str:
        """
        Gets the text of the button.

        :return: The text content of the button.
        """
        return self.locator.text_content() or ""

    def is_enabled(self) -> bool:
        """
        Checks if the button is enabled.

        :return: True if the button is enabled, False otherwise.
        """
        return self.locator.is_enabled()
