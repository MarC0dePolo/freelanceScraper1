import paths
from crawler import *

class GetProduktLinks(GartentechnikScraper):
    def __init__(self):
        super().__init__()
    
    def get_all_links(self, link) -> None:
        self.driver.get(link)
        for i in range(6):
            myList = self.try_func("self.driver.find_element(By.XPATH, paths.produkt_list)", True)
            self.scroll_to_bottom()
            myList = self.driver.find_elements(By.CLASS_NAME, 'row-title')
            time.sleep(2)
            for elem in myList:
                with open("all_links.txt", "a") as file:
                    file.write(elem.get_attribute('href') + '\n')

            time.sleep(0.5)
            self.driver.find_element(By.CSS_SELECTOR, 'a.next-page:nth-child(5)').click()
            time.sleep(5)

def main():
    script = GetProduktLinks()
    link = "https://www.faraguna-gartentechnik.de/wp-admin/edit.php?s&post_status=all&post_type=product&action=-1&product_cat&product_type&stock_status&seo-filter=good-seo&schema-filter=none&paged=7&action2=-1"
    script.get_all_links(link)

if __name__ == "__main__":
    main()
