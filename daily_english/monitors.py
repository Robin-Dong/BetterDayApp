import requests
import datetime
from .models import DailyEnglish,DailyImg,DailyQuote


def get_daily_english():
    headers = {
        'Host': 'm.weibo.cn',
        'Referer': 'https://m.weibo.cn/u/3802004551',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        'X-Requested-With': 'XMLHttpRequest',
    }
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076033802004551&page=1'
    re = requests.get(url, headers=headers)
    items = re.json().get('data').get('cards')
    target_title = "#每日三句地道表达#"
    for item in items:
        try:
            page_title = item['mblog']['page_info']['page_title']
            page_item = item['mblog']['pics']
            if page_title == target_title and len(page_item) >= 6:
                created_time = datetime.datetime.now().strftime("%y%m%d")
                pic_list = [pic['pid'] for pic in page_item]
                DailyEnglish.objects.get_or_create(pic_url=pic_list, created_time=created_time)
                print(created_time + 'ok')
        except:
            continue
    print("daily_english don't update ", datetime.datetime.now())


def get_daily_pic():
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    re = requests.get(url)
    if re.status_code == 200:
        img = re.json()['images'][0]['url']
        title = re.json()['images'][0]['title']
        DailyImg.objects.get_or_create(img_url=img, title=title)
        print('daily_pic done')
    print("daily_pic don't update ", datetime.datetime.now())


def get_daily_quote():
    url = 'http://open.iciba.com/dsapi'
    re = requests.get(url=url)
    if re.status_code == 200:
        content = re.json()['content']
        note = re.json()['note']
        DailyQuote.objects.get_or_create(quote=content, note=note)
        print('daily_quote done')
    print("daily_quote don't update",datetime.datetime.now())


def update_date():
    get_daily_english()
    get_daily_pic()
    get_daily_quote()


