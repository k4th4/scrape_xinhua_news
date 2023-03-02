import lxml
import datetime as dt
import requests
import urllib
import json
import re

def scrape_xinhua_news (target_day: dt.datetime, search_term: str) -> list:
  '''Description: This function scrapes the Xinhua News Agency website 'http://so.news.cn/' for news articles containing a specified search term published on a specified day. The function retrieves search results from the first three pages of the website's search results. If a search result is more than 10 days old from the specified day, the function will stop iterating through the search results. The function returns a list of dictionaries containing the title, link, and date-time of each article found.

Function Inputs:
target_day (dt.datetime): A datetime object representing the day on which to search for articles. The function will retrieve articles published on this day.
search_term (str): A string representing the search term to search for on 'http://so.news.cn/'.

Function Outputs:
result_list (list): A list of dictionaries. Each dictionary contains information about a news article matching the search criteria. The dictionary has three keys: 'title', 'link', and 'date_time'. 'title' contains the title of the article, 'link' contains the URL of the article, and 'date_time' contains a datetime object representing the date and time the article was published.

Function Logic:
1. Initialize an empty list called result_list to store the search results.
2. Iterate through the first three search result pages on Xinhua News Agency's website.
3. Convert the search term into a Chinese topic in code by encoding the search_term with urllib.parse.quote() method.
4. Construct the URL to access Xinhua News Agency's search results page for the given search term and page number.
5. Use the requests.get() method to access the webpage and retrieve its JSON data.
6. Extract the list of search results from the JSON data.
7. For each search result, extract the title, link, and date-time.
8. Stop iterating through the search results if a search result is more than 10 days old from the specified target day.
9. If a search result matches the target day, add the result to result_list as a dictionary containing the title, link, and date-time.
10. Return result_list with all matching articles.'''
  
  result_list = []
  # how many search pages should be accessed
  for page in [1,2,3]:#,2,3,4,5,6,7,8]:
    # e.g. turn '中共' into ''%E4%B8%AD%E5%85%B1'
    chinese_topic_in_code = urllib.parse.quote(search_term, safe='')
    url = f'https://so.news.cn/getNews?sortField=0&searchFields=1&keyword={chinese_topic_in_code}&curPage={page}&lang=cn'
    # access xinhuanet and retrieve the json
    response = requests.get(url)
    json_data = json.loads(response.text)
    results = json_data['content']['results']
    if results:
      for result in results:
         # get the title and link of the result
        title = re.sub(re.compile('<.*?>'), '', result['title']).replace('&nbsp;', ' ')
        link = result['url']
        # get the date of the result
        date_string = result['pubtime'].split(' ')[0]
        date_time = dt.datetime.strptime(date_string, '%Y-%m-%d')
        # stop if search results are more than 10 days older than the target day
        if (target_day - date_time).days >= 10:
            break
        if date_time.day == target_day.day and date_time.month == target_day.month and date_time.year == target_day.year:
                    result_list.append({'title': title, 'link': link, 'date_time': date_time})
    return result_list

# example
today = dt.datetime.today()
scrape_xinhua_news (today, '中共')
#print(scrape_xinhua (today, '中共'))

"--> [{'title': '中共代表团访问乌干达', 'link': 'http://www.news.cn/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}, {'title': '中共代表团访问乌干达', 'link': 'http://m.news.cn/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}, {'title': '中共代表团访问乌干达', 'link': 'http://www.news.cn/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}, {'title': '中共代表团访问乌干达', 'link': 'http://www.news.cn/world/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}]"