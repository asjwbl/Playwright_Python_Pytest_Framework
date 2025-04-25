from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class RadioButtonComponent(BaseComponent):
    """
    Handles interactions with radio button elements on a webpage.
    """

    def __init__(self, page: Page, locator: str | Locator):
        """
        Initializes the RadioButtonComponent.

        Args:
            page (Page): The Playwright Page object representing the browser tab.
            locator (str | Locator): The locator for the radio button element.
        """
        super().__init__(page, locator)

    def select(self) -> None:
        """
        Selects the radio button if it is not already selected.
        """
        if not self.is_selected():
            self.locator.click()

    def is_selected(self) -> bool:
        """
        Checks if the radio button is currently selected.

        Returns:
            bool: True if the radio button is selected, False otherwise.
        """
        return self.locator.is_checked()
