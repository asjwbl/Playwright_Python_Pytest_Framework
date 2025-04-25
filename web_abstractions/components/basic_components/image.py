from playwright.sync_api import Page, Locator
from components.basic_components.base_component import BaseComponent

class ImageComponent(BaseComponent):
    """Encapsulates interactions with an image element on a web page."""

    def __init__(self, page: Page, locator: str | Locator):
        super().__init__(page, locator)

    def get_src(self) -> str:
        """Gets the 'src' attribute (image URL) of the image."""
        return self.locator.get_attribute("src")

    def get_alt_text(self) -> str:
        """Gets the 'alt' attribute (alternative text) of the image."""
        return self.locator.get_attribute("alt")

    def is_visible(self) -> bool:
        """Checks if the image is visible on the page."""
        return self.locator.is_visible()

    def click(self):
        """Clicks on the image element."""
        self.locator.click()
