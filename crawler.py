from base import GartentechnikScraper

class KeywordInserter(GartentechnikScraper):
    def __init__(self):
        super().__init__()

    def get_input_field(self):
        input_field = self.driver.find_element(By.CSS_SELECTOR, paths.keyword_input_field_css_selector)
        return input_field
    
    def get_name_off_produkt(self) -> str:
        name = self.driver.find_element(By.CSS_SELECTOR, paths.produkt_name)
        name = name.get_attribute('value')
        return name

    def try_func(self, func : str, is_return : bool):
        while True:
            try:
                if is_return:
                    return eval(func)
                eval(func)
                return

            except Exception as e:
                print(e)

    def insert_keyword(self, name):
        # Keyword Input field
        input_field = self.try_func("self.get_input_field()", True)

        # Click Element and Enter text
        #self.try_clicking_input_field()
        input_field.send_keys(name + Keys.ENTER)
        time.sleep(2)


    def clear_textfield(self):
        input_field = self.try_func("self.get_input_field()", True)

        for i in range(3):
            self.try_func("self.get_input_field().click()", False)
            input_field.send_keys(Keys.BACK_SPACE)

    def check_keyword_score(self) -> int:
        score = str(self.driver.find_element(By.CSS_SELECTOR, paths.keyword_score).text)
        score = score.split(" / ")[0]
        return int(score)
    
    def safe_the_word(self, keyword):

        for i in range(3):
            self.try_func("self.get_input_field().click()", False)
        
        input_field = self.try_func("self.get_input_field()", True)
        input_field.send_keys(keyword + Keys.ENTER)

        self.scroll_up()
        time.sleep(1)
        self.try_func("self.driver.find_element(By.XPATH, paths.safe_produkt).click()", False)
        time.sleep(5)
        
    def delete_link_from_file(self, file_path, link_to_delete):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = [line for line in lines if line.strip() != link_to_delete]

        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
    
    def try_keywords(self) -> None:
        name = self.try_func("self.get_name_off_produkt()", True)
        self.scroll_to_bottom()
        word_list = name.split(" ")
        
        current_score = 0
        highest_score = self.check_keyword_score()
        
        # Maybe there is no existing keyword
        try:
            best_keyword = self.get_current_keyword()
        except:
            pass

        loop_count = 0
        idx_left = 0
        idx_right = len(word_list) - 1

        ### Loop Algorithm to test each possible keyword ###

        while idx_right >= 0:

            while idx_right < len(word_list):
                current_keyword = " ".join(word_list[idx_left:idx_right + 1])
                current_keyword = current_keyword.replace(',', '')
                
                self.insert_keyword(current_keyword)
                current_score = self.check_keyword_score()
                self.clear_textfield()

                if current_score > highest_score:
                    highest_score = current_score
                    best_keyword = current_keyword

                idx_left += 1
                idx_right += 1
                
            loop_count += 1
            idx_left = 0
            idx_right = len(word_list) - loop_count - 1 

        self.safe_the_word(best_keyword)
        time.sleep(5)
        self.delete_link_from_file(self.filePath, self.currentLink)

    def get_current_keyword(self):
        keyword = self.driver.find_element(By.CLASS_NAME, 'tagify__tag-text')
        return keyword.text

    def try_keywords_only1(self):
        name = self.try_func("self.get_name_off_produkt()", True)
        self.scroll_to_bottom()
        word_list = name.split(" ")
        current_score = 0
        highest_score = self.check_keyword_score()
        try:
            best_keyword = self.get_current_keyword()
        except:
            pass

        for current_keyword in word_list:
            current_keyword.replace(',', '')

            self.insert_keyword(current_keyword)
            current_score = self.check_keyword_score()
            self.clear_textfield()

            if current_score > highest_score:

                highest_score = current_score
                best_keyword = current_keyword

        self.safe_the_word(best_keyword)
        time.sleep(5)
        self.delete_link_from_file(self.filePath, self.currentLink)

    def loop_produkts(self, path_to_links) -> None:
        with open(path_to_links, "r") as file:
            lines = file.read().split("\n")

        for link in lines:
            self.currentLink = link
            
            for _ in range(3):
                try:
                    self.driver.get(self.currentLink)
                    break
                except Exception as e:
                    time.sleep(3)
                    print(e)

 
            self.try_keywords()
            time.sleep(2)
            print(f"{self.currentLink} Done!!!")
    
    def scroll_to_bottom(self) -> None:
        get_height = lambda driver: driver.execute_script("return document.documentElement.scrollHeight")
        current_scroll_height = get_height
        last_scroll_height = -1

        while current_scroll_height != last_scroll_height:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            last_scroll_height = current_scroll_height
            current_scroll_height = get_height(self.driver)
            time.sleep(0.5)
        
        print("Scrolled to Bottom")
        time.sleep(1)

    def safe_word_again(self, file_path):
        time.sleep(5)
        with open(file_path, "r") as file:
            lines = file.read().split("\n")

        for link in lines:
            try:
                self.driver.get(link)
            except Exception as e:
                print(e)
            
            time.sleep(2)
            while True:
                try:
                    self.driver.find_element(By.XPATH, paths.safe_produkt).click()
                    break
                except:
                    time.sleep(2)
            time.sleep(5)
            print(link + " Done !!!")

def main():
    Crawler = KeywordInserter()
    Crawler.loop_produkts(Crawler.filePath)

    #Crawler.safe_word_again("all_links.txt")

    ### for testing ###
    #link = 'https://www.faraguna-gartentechnik.de/wp-admin/post.php?post=10549&action=edit'
    #Crawler.driver.get(link)
    #Crawler.currentLink = link
    #Crawler.try_keywords()

if __name__ == "__main__":
    main()
