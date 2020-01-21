import time
import constant as c
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv # csvを扱うためのライブラリ
import pprint # 表示を見やすくするライブラリ
import re # 正規表現を扱うためのライブラリ
import datetime
import bot

def get_front_info_of_games(b, data_limit):
    datas = []
    index = 1
    while len(datas) < data_limit:
        b.get(c.freem_ranking_page + str(index))
        elements = b.driver.find_elements_by_xpath(c.freem_game_list_xpath)
        for element in elements:
            try:
                plays = element.find_element_by_class_name(c.freem_plays_xpath).get_attribute("textContent")
                rank_and_name = element.find_element_by_class_name(c.freem_rank_and_name_xpath).get_attribute("textContent").split(':')
                caption = element.find_element_by_css_selector('div.game-list-sub.pc > p').get_attribute("textContent")
                url = element.find_element_by_tag_name('a').get_attribute('href')
                datas.append([re.sub("\\D", "", plays), rank_and_name[0], rank_and_name[1], caption, len(caption), url])
            except:
                continue
        index += 1
        print(index)
    
    with open(c.csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(datas)

def get_deep_info_of_games(b):
    with open(c.csv_path) as f:
        reader = csv.reader(f)
        front_datas = [row for row in reader]

    new_datas = front_datas

    front_datas_T = [list(x) for x in zip(*front_datas)]

    index = 0

    genres = ['アクション', 'シューティング', 'アドベンチャー', 'ノベル', 'RPG', 'シミュレーション', 'パズル', 'テーブル', 'タイピング', 'その他']

    for url in front_datas_T[c.csv_ranking_data_url]:
        b.get(url)
        tags = b.driver.find_elements_by_xpath('/html/body/div/div[2]/div[1]/div[2]/section[1]/ul/li')
        slides = b.driver.find_element_by_xpath('//*[@id="js-gamezone"]/div[1]/div/div/div[3]').find_elements_by_tag_name('span')
        caption = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/section').get_attribute("textContent")
        file_name = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[1]/td').get_attribute("textContent")
        game_version = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[2]/td').get_attribute("textContent")
        size = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[3]/td').get_attribute("textContent")
        needed_run_time = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[4]/td').get_attribute("textContent")
        environment = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[5]/td').get_attribute("textContent")
        feature = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[6]/td').get_attribute("textContent")
        age = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[7]/td').get_attribute("textContent")
        registered_date = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[8]/td').get_attribute("textContent")
        registered_date_datetime = datetime.datetime.strptime(registered_date, '%Y-%m-%d')
        registered_date_difference = (datetime.date.today() - datetime.date(registered_date_datetime.year, registered_date_datetime.month, registered_date_datetime.day)).days
        updated_date = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[9]/td').get_attribute("textContent")
        updated_date_datetime = datetime.datetime.strptime(updated_date, '%Y-%m-%d')
        updated_date_difference = (datetime.date.today() - datetime.date(updated_date_datetime.year, updated_date_datetime.month, updated_date_datetime.day)).days
        info_updated_date = b.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[5]/div[1]/table/tbody/tr[10]/td').get_attribute("textContent")
        info_updated_date_datetime = datetime.datetime.strptime(info_updated_date, '%Y-%m-%d')
        info_updated_date_difference = (datetime.date.today() - datetime.date(info_updated_date_datetime.year, info_updated_date_datetime.month, info_updated_date_datetime.day)).days
        # caption length
        genres_detect = [0] * len(genres)
        # genre
        for tag in tags:
            tag_text = tag.get_attribute("textContent")
            genre_index = 0
            for genre in genres:
                if genre in tag_text:
                    genres_detect[genre_index] = 1
                genre_index += 1

        tmp = [len(tags), len(slides), len(caption), file_name, game_version, size, needed_run_time, environment, feature, age, re.sub("\\D", "", age), registered_date, registered_date_difference, updated_date, updated_date_difference, info_updated_date, info_updated_date_difference]
        tmp.extend(genres_detect)
        new_datas[index].extend(tmp)

        index += 1
        print(index)
        if index % 50 == 0:
            with open(c.csv_path_all_data, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(new_datas)

    with open(c.csv_path_all_data, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(new_datas)

def main():
    b = bot.Bot(c.driver_path)
    b.login(c.freem_login_page, c.freem_login_id_xpath, c.my_id, c.freem_login_pw_xpath, c.my_pw, c.freem_login_done_xpath)

    #get_front_info_of_games(b, 1000)
    print("start - search - all - data")
    get_deep_info_of_games(b)

    b.driver.quit()


if __name__ == "__main__":
    main()