from playwright.sync_api import Page, expect, Locator


class HomePageLocators:
    
    def __init__(self, page: Page) -> None:
        self.page = page
        self.navigation_search_button = self.page.locator('.component--header__search')
        search_bar = self.page.locator('.component--header__navigation').locator('.header--search')
        self.search_box = search_bar.get_by_placeholder('Search')
        self.search_results = search_bar.locator('.header--search__results').locator('.result')
    
class BritHomePage:

    def __init__(self, page: Page) -> None:
        self.brit_url = "https://britinsurance.com"
        self.page = page
        self.locators = HomePageLocators(self.page)

    def go_to_homepage(self):
        """A repeatable step to navigate to the BRIT insurance homepage."""
        self.page.goto(self.brit_url)
        expect(self.page, "Page title is not as expected.").to_have_title("Brit Insurance")
    
    def get_search_results(self, search_text: str) -> Locator:
        """Search for a specifc text and return the top results found."""
        self.locators.navigation_search_button.click()
        self.locators.search_box.clear()
        self.locators.search_box.type(search_text) # Using 'type' as 'fill' method doesn't trigger the results list
        self.locators.search_results.first.wait_for()
        return self.locators.search_results