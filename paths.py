
### Website Links ###
main_page_admin = "https://www.faraguna-gartentechnik.de/wp-admin"

produkt_link_keyword_not_set = "https://www.faraguna-gartentechnik.de/wp-admin/edit.php?s&post_status=all&post_type=product&action=-1&product_cat&product_type&stock_status&seo-filter=empty-fk&schema-filter=none&paged=1&action2=-1"

### XPath's ###
produkt_list = '//*[@id="the-list"]'
next_page_button = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form[1]/div[2]/div[3]/span[2]/a'
keyword_input_field_xpath = "./html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[5]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/tags"                                                       # first is [1] after that [3]
safe_produkt = '//*[@id="publish"]'

# CSS selectors
produkt_name = '#title'  
produkt_title_css_selector = "#post-930 > td:nth-child(3) > strong:nth-child(1) > a:nth-child(1)"
keyword_input_field_css_selector = '.tagify__input'                   
keyword_score = "div.rank-math-seo-score:nth-child(3) > span:nth-child(1)"
remove_keyword = '.tagify__tag__removeBtn'

# login
email_xpath = '//*[@id="user_login"]'
pw_xpath = '//*[@id="user_pass"]'
login_button_xpath = '//*[@id="wp-submit"]'
keyword_input_field_css_selector = '.tagify__input'                   

#xpaths for improvement
xpath_keywword_in_title = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[1]'
xpath_keyword_in_meta = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[2]'
xpath_keyword_in_url = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[3]'
xpath_keyword_in_beginning = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[4]'
xpath_keyword_in_content = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[5]'
xpath_keyword_in_length = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[6]'
xpath_keyword_schema = '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/form/div/div/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[7]'
