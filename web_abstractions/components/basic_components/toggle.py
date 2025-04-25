from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class ToggleComponent(BaseComponent):
    """
    Handles interactions with toggle switch elements on a webpage.
    """

    def __init__(self, page: Page, locator: str | Locator):
        """
        Initializes the ToggleComponent.

        Args:
            page (Page): The Playwright Page object representing the browser tab.
            locator (str | Locator): The locator for the toggle switch element.
        """
        super().__init__(page, locator)

    def turn_on(self) -> None:
        """
        Toggles the switch to the 'on' position if it is not already on.
        """
        if not self.is_checked():
            self.locator.click()

    def turn_off(self) -> None:
        """
        Toggles the switch to the 'off' position if it is not already off.
        """
        if self.is_checked():
            self.locator.click()

    def is_checked(self) -> bool:
        """
        Checks the current state of the toggle.

        Returns:
            bool: True if the toggle is in the 'on' position, False otherwise.
        """
        return self.locator.is_checked()
