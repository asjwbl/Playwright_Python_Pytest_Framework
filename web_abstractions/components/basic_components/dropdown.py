from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class DropdownComponent(BaseComponent):
    """
    DropdownComponent class to handle dropdown interactions in a web page.
    Provides methods to select options by value, label, index, or text.
    """

    def __init__(self, page: Page, selector: str | Locator):
        """
        Initializes the DropdownComponent with a locator for the dropdown element.

        :param page: The Playwright Page object representing the browser tab.
        :param selector: The CSS or XPath selector, or an existing Locator object to locate the dropdown element.
        """
        super().__init__(page, selector)

    def select_option_by_value(self, value: str) -> None:
        """
        Selects an option from the dropdown by its value attribute.

        :param value: The value of the option to select.
        """
        self.locator.select_option(value)

    def select_option_by_label(self, label: str) -> None:
        """
        Selects an option from the dropdown by its visible text.

        :param label: The visible text of the option to select.
        """
        self.locator.select_option(label)

    def select_option_by_index(self, index: int) -> None:
        """
        Selects an option from the dropdown by its index (0-based).

        :param index: The index of the option to select.
        """
        self.locator.select_option(index=index)

    def select_option_by_text(self, text: str) -> None:
        """
        Selects an option from the dropdown by its visible text.

        :param text: The text of the option to select.
        :raises ValueError: If the option with the specified text is not found.
        """
        options = self.locator.locator("option").all_inner_texts()
        if text in options:
            self.select_option_by_label(text)
        else:
            raise ValueError(f'Option with text "{text}" not found in dropdown.')

    def get_selected_option_value(self) -> str | None:
        """
        Gets the currently selected option's value from the dropdown.

        :returns: The value of the currently selected option or None if not found.
        """
        return self.locator.input_value()

    def get_selected_option_text(self) -> str:
        """
        Gets the text of the currently selected option from the dropdown.

        :returns: The visible text of the currently selected option.
        """
        return self.locator.evaluate("dropdown => dropdown.options[dropdown.selectedIndex].text")
