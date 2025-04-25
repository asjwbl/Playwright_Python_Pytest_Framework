from playwright.sync_api import Page, Locator
from typing import Type, TypeVar, Optional

T = TypeVar("T", bound="BaseComponent")


class BaseComponent:
    """
    BaseComponent class provides a flexible way to locate elements on a web page using
    different strategies such as CSS selectors, XPath, and Playwright's get_by_* methods.
    It serves as the foundation for building basic components, which are then used to create composite components.
    """

    def __init__(self, page: Page, selector: str | Locator):
        """
        Initializes the BaseComponent with a locator.

        :param page: The Playwright Page object representing the browser tab.
        :param selector: The CSS or XPath selector, or an existing Locator object to locate the element.
        """
        self.page = page

        if isinstance(selector, str):
            if selector.startswith("//"):  # XPath Selector
                self.locator = self.page.locator(selector)
            else:  # CSS Selector
                self.locator = self.page.locator(selector)
        elif isinstance(selector, Locator):
            self.locator = selector
        else:
            raise ValueError("Selector must be either a string or a Playwright Locator object.")

    @classmethod
    def by_role(cls: Type[T], page: Page, role: str, name: Optional[str] = None) -> T:
        """
        Creates an instance of a component by locating an element by its ARIA role.

        :param page: The Playwright Page object representing the browser tab.
        :param role: The ARIA role to search for (e.g., 'button', 'checkbox').
        :param name: The accessible name of the element to locate.
        :return: A new instance of the derived component class.
        """
        locator = page.get_by_role(role, name=name)
        return cls(page, locator)

    @classmethod
    def by_label(cls: Type[T], page: Page, label: str) -> T:
        """
        Creates an instance of a component by locating an element by its associated label.

        :param page: The Playwright Page object representing the browser tab.
        :param label: The label text associated with the element.
        :return: A new instance of the derived component class.
        """
        locator = page.get_by_label(label)
        return cls(page, locator)

    @classmethod
    def by_placeholder(cls: Type[T], page: Page, placeholder: str) -> T:
        """
        Creates an instance of a component by locating an element by its placeholder text.

        :param page: The Playwright Page object representing the browser tab.
        :param placeholder: The placeholder text of the element.
        :return: A new instance of the derived component class.
        """
        locator = page.get_by_placeholder(placeholder)
        return cls(page, locator)

    @classmethod
    def by_test_id(cls: Type[T], page: Page, test_id: str) -> T:
        """
        Creates an instance of a component by locating an element by its test ID.

        :param page: The Playwright Page object representing the browser tab.
        :param test_id: The test ID of the element.
        :return: A new instance of the derived component class.
        """
        locator = page.get_by_test_id(test_id)
        return cls(page, locator)

    @classmethod
    def by_alt_text(cls: Type[T], page: Page, alt_text: str) -> T:
        """
        Creates an instance of a component by locating an element by its alt text (commonly used for images).

        :param page: The Playwright Page object representing the browser tab.
        :param alt_text: The alt text associated with the element.
        :return: A new instance of the derived component class.
        """
        locator = page.get_by_alt_text(alt_text)
        return cls(page, locator)

    @classmethod
    def by_title(cls: Type[T], page: Page, title: str) -> T:
        """
        Creates an instance of a component by locating an element by its title attribute.

        :param page: The Playwright Page object representing the browser tab.
        :param title: The title attribute of the element.
        :return: A new instance of the derived component class.
        """
        locator = page.get_by_title(title)
        return cls(page, locator)

