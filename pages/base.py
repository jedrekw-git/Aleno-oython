from pages.page import Page

class BasePage(Page):

    _base_url = "http://test.aleno.me/"

    @property
    def header(self):
        from pages.regions.header_region import HeaderRegion
        return HeaderRegion(self.get_driver())