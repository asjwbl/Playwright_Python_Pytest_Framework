from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class InputComponent(BaseComponent):
    """
    InputComponent class to encapsulate interactions with input elements.
    Supports initialization with any locator type (CSS/XPath/getBy* methods).
    """

    def __init__(self, page: Page, selector: str | Locator):
        """
        Initializes the InputComponent using different locators.

        :param page: The Playwright Page object representing the browser tab.
        :param selector: The CSS or XPath selector, or an existing Locator object.
        """
        super().__init__(page, selector)

    def fill(self, value: str) -> None:
        """
        Fills the input field with a value.

        :param value: The value to enter into the input field.
        """
        self.locator.fill(value)

    def clear(self) -> None:
        """
        Clears the input field.
        """
        self.locator.fill("")  # Clears the input field

    def get_value(self) -> str:
        """
        Gets the current value of the input field.

        :return: The current value of the input field.
        """
        return self.locator.input_value()

    def is_enabled(self) -> bool:
        """
        Checks if the input field is enabled.

        :return: True if the input is enabled, False otherwise.
        """
        return self.locator.is_enabled()

    def is_disabled(self) -> bool:
        """
        Checks if the input field is disabled.

        :return: True if the input is disabled, False otherwise.
        """
        return not self.locator.is_enabled()

    def focus(self) -> None:
        """
        Focuses on the input field.
        """
        self.locator.focus()
