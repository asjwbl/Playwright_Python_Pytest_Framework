from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class LabelComponent(BaseComponent):
    """
    Handles interactions with label elements on a web page.
    """

    def __init__(self, page: Page, locator: str | Locator):
        """
        Initializes the LabelComponent.

        Args:
            page (Page): The Playwright Page object representing the browser tab.
            locator (str | Locator): The locator for the label element.
        """
        super().__init__(page, locator)

    def get_text(self) -> str:
        """
        Retrieves the text content of the label.

        Returns:
            str: The text inside the label. Defaults to an empty string if not found.
        """
        return self.locator.text_content() or ""

    def is_visible(self) -> bool:
        """
        Checks if the label is visible on the page.

        Returns:
            bool: True if the label is visible, False otherwise.
        """
        return self.locator.is_visible()

    def click(self) -> None:
        """
        Clicks on the label element.
        """
        self.locator.click()
