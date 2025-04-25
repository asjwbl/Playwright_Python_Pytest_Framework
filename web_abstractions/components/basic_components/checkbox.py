from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class CheckboxComponent(BaseComponent):
    """
    CheckboxComponent class to handle interactions with checkbox elements on a web page.

    This class provides methods to check, uncheck, and interact with checkbox elements
    using Playwright locators. It inherits from the BaseComponent class, allowing flexible
    element location strategies such as CSS selectors, XPath, or Playwright's get_by_* methods.
    """

    def __init__(self, page: Page, selector: str | Locator):
        """
        Initializes the CheckboxComponent with a locator for the checkbox element.

        :param page: The Playwright Page object representing the browser tab.
        :param selector: The CSS or XPath selector, or an existing Locator object to locate the checkbox element.
        """
        super().__init__(page, selector)

    def check(self) -> None:
        """
        Checks the checkbox if it is not already checked.

        This method ensures that the checkbox is checked. If the checkbox is already checked,
        no action will be taken.
        """
        if not self.locator.is_checked():
            self.locator.check()

    def uncheck(self) -> None:
        """
        Unchecks the checkbox if it is currently checked.

        This method ensures that the checkbox is unchecked. If the checkbox is already unchecked,
        no action will be taken.
        """
        if self.locator.is_checked():
            self.locator.uncheck()
