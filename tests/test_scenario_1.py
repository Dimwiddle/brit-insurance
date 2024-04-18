from playwright.sync_api import Page, expect
import pytest
from utilities.web import BritHomePage

SEARCH_CRITERIA = {
    'IFRS 17': {
        'Financials': '/financials-and-governance/financials',
        'Interim results for the six months ended 30 June 2022': '/news/interim-results-2022',
        'Results for the year ended 31 December 2023': '/news/results-for-the-year-ended-31-december-2023',
        'Interim Report 2023': '/news/interim-report-2023',
        'Kirstin Simon': '/culture/kirstin-simon'
    }
}

@pytest.fixture()
def brit_driver(page: Page) -> BritHomePage:
    driver = BritHomePage(page)
    driver.go_to_homepage()
    return driver

def test_search_count(brit_driver: BritHomePage):
    """Scenario 1a: Verify the search bar in the BRIT insurance website is returning the expected number of results."""
    for search, titles in SEARCH_CRITERIA.items():
        actual_results = brit_driver.get_search_results(search)
        assert len(titles) == 5, f"5 titles are expected to be returned for '{search}'"
        expect(actual_results, "Results is not the expected amount").to_have_count(len(titles))

def test_search_content_links(brit_driver: BritHomePage):
    """Scenario 1b: Verify the search results content has the expected titles and hyperlinks."""
    for search, criteria in SEARCH_CRITERIA.items():
        actual_results = brit_driver.get_search_results(search)
        for row in actual_results.all():
            row_text = row.text_content().strip()
            assert row_text in criteria.keys(), f"Unexpected search result in criteria"
            href = row.get_by_role('link')
            expect(href).to_have_attribute('href', criteria[row_text], ignore_case=True)