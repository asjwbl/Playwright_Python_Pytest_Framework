from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent


class ToastComponent(BaseComponent):
    """
    Handles interactions with toast notifications.
    """

    def __init__(self, page: Page, locator: str | Locator):
        """
        Initializes the ToastComponent.

        Args:
            page (Page): The Playwright Page object representing the browser tab.
            locator (str | Locator): The locator for the toast notification element.
        """
        super().__init__(page, locator)

    def dismiss(self) -> None:
        """
        Dismisses the toast notification by clicking on it.
        """
        self.locator.click()

    def is_visible_with_message(self, message: str) -> bool:
        """
        Checks if a toast notification with the specified message is visible.

        Args:
            message (str): The expected message in the toast notification.

        Returns:
            bool: True if the toast notification is visible, False otherwise.
        """
        return self.page.locator(f"text={message}").is_visible()

    def has_error(self) -> bool:
        """
        Verifies if an error toast message is displayed.

        Returns:
            bool: True if an error toast is visible, False otherwise.
        """
        return self.page.locator('[data-testid="toast-error"]').is_visible()

    def wait_for_dismiss(self, timeout: int = 5000) -> None:
        """
        Waits for the toast notification to disappear from the page.

        Args:
            timeout (int): The maximum time (in milliseconds) to wait before considering the toast disappeared.
        """
        self.locator.wait_for(state="detached", timeout=timeout)
