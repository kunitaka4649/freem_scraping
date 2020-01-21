import os

# absolute path
driver_path = os.path.dirname(os.path.abspath(__file__)) + '/../chrome_driver/chromedriver'
csv_path = os.path.dirname(os.path.abspath(__file__)) + '/../csv/ranking_data'
csv_path_all_data = os.path.dirname(os.path.abspath(__file__)) + '/../csv/deep_date'
# personal information
my_id = 'kunetpoint@gmail.com'
my_pw = 'lemon232'
# url
freem_login_page = 'https://www.freem.ne.jp/account/login'
freem_ranking_page = 'https://www.freem.ne.jp/win/ranking/download/weekly/page-'
# xpath
freem_login_id_xpath = '//*[@id="UserEmailPc"]'
freem_login_pw_xpath = '//*[@id="UserPassword"]'
freem_login_done_xpath = '/html/body/div/div/div/section/form/div[1]/input'
freem_game_list_xpath = '/html/body/div/div[1]/div/section[1]/ul/li'
freem_rank_and_name_xpath = 'pc'
freem_plays_xpath = 'game-list-review'
freem_caption_xpath = 'game-list-sub pc'
# selector
game_list_selector = 'body > div > div.main-content.col > div > section.new-free-game.underline > ul'
# csv ranking_data info
csv_ranking_data_url = 5 # +1 列目