from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class ClickableComponent(BaseComponent):
    """
    Represents a clickable component on a web page, such as buttons or links,
    with additional actions like hover, double-click, and right-click.
    """

    def __init__(self, page: Page, selector: str | Locator):
        """
        Initializes the ClickableComponent with a locator for the clickable element.

        :param page: The Playwright Page object representing the browser tab.
        :param selector: The CSS or XPath selector, or an existing Locator object to locate the clickable element.
        """
        super().__init__(page, selector)

    def click(self) -> None:
        """
        Clicks on the element after ensuring it is visible.
        """
        self.locator.wait_for(state="visible")
        self.locator.click()

    def hover(self) -> None:
        """
        Hovers over the element after ensuring it is visible.
        """
        self.locator.wait_for(state="visible")
        self.locator.hover()

    def double_click(self) -> None:
        """
        Double-clicks on the element after ensuring it is visible.
        """
        self.locator.wait_for(state="visible")
        self.locator.dblclick()

    def right_click(self) -> None:
        """
        Performs a right-click on the element after ensuring it is visible.
        """
        self.locator.wait_for(state="visible")
        self.locator.click(button="right")

    def focus(self) -> None:
        """
        Focuses on the element after ensuring it is visible.
        """
        self.locator.wait_for(state="visible")
        self.locator.focus()

    def is_disabled(self) -> bool:
        """
        Checks if the element is disabled by checking the 'disabled' attribute.

        :returns: A boolean indicating whether the element is disabled.
        """
        return self.locator.get_attribute("disabled") is not None
