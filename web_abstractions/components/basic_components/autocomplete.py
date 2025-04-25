from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class AutocompleteComponent(BaseComponent):
    """
    Represents an autocomplete component on a web page.
    """

    def __init__(
            self,
            page: Page,
            locator: str | Locator,
            suggestion_selector: str | None = None,
            sleep_time_before_click: int | None = None,
            sleep_time_before_opening: int | None = None,
    ):
        """
        Initializes the AutocompleteComponent with optional suggestion handling.

        Args:
            page (Page): The Playwright Page object representing the browser tab.
            locator (str | Locator): The locator for the autocomplete input field.
            suggestion_selector (str | None): Optional selector for the suggestions list.
            sleep_time_before_click (int | None): Optional delay before selecting a suggestion.
            sleep_time_before_opening (int | None): Optional delay before opening the autocomplete.
        """
        super().__init__(page, locator)
        self.suggestion_selector = (
            page.locator(suggestion_selector) if suggestion_selector else None
        )
        self.sleep_time_before_click = sleep_time_before_click
        self.sleep_time_before_opening = sleep_time_before_opening

    def set_value(self, value: str) -> None:
        """
        Sets the value of the autocomplete field and optionally waits before and after input.

        Args:
            value (str): The value to enter into the autocomplete field.
        """
        if self.sleep_time_before_opening:
            self.page.wait_for_timeout(self.sleep_time_before_opening)

        self.locator.fill(value)

        if self.sleep_time_before_click:
            self.page.wait_for_timeout(self.sleep_time_before_click)

        self.locator.press("Enter")  # Simulates pressing Enter after input

    def wait_for_suggestions(self, timeout: int = 1000) -> None:
        """
        Waits for autocomplete suggestions to appear.

        Args:
            timeout (int): Timeout in milliseconds to wait for suggestions.
        """
        if self.suggestion_selector:
            self.suggestion_selector.wait_for(state="visible", timeout=timeout)
        else:
            print("Warning: Suggestion selector not provided, skipping wait.")

    def select_suggestion(self, suggestion_text: str) -> None:
        """
        Selects a suggestion from the autocomplete dropdown by matching the text.

        Args:
            suggestion_text (str): The text of the suggestion to select.
        """
        suggestion = self.page.locator(f"text={suggestion_text}")
        suggestion.click()

    def clear_input(self) -> None:
        """
        Clears the input field by selecting all text and deleting it.
        """
        value = self.locator.input_value()
        if value:
            self.locator.press("Control+A")  # Select all text
            self.locator.press("Backspace")  # Delete text

    def dismiss_suggestions(self) -> None:
        """
        Dismisses the autocomplete suggestions by pressing the Escape key.
        """
        self.locator.press("Escape")
