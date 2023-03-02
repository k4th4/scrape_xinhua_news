# scrape_xinhua_news Function

This repository contains a Python function called `scrape_xinhua` that scrapes the Xinhua News Agency website http://so.news.cn/ for news articles containing a specified search term published on a specified day. 

## How to use
1. Clone the repository to your local machine.
2. Import the `scrape_xinhua` function into your Python code.
3. Call the function with two parameters: `target_day` and `search_term`.
4. The function will return a list of dictionaries containing information about each article found.

```python
import datetime as dt
from scrape_xinhua_news import scrape_xinhua_news

target_day = dt.datetime(2023, 3, 2) # search articles published on March 2, 2023
search_term = '中共' # search for articles containing the term "中共"

results = scrape_xinhua_news(target_day, search_term)

results = [{'title': '中共代表团访问乌干达', 'link': 'http://www.news.cn/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}, {'title': '中共代表团访问乌干达', 'link': 'http://m.news.cn/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}, {'title': '中共代表团访问乌干达', 'link': 'http://www.news.cn/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}, {'title': '中共代表团访问乌干达', 'link': 'http://www.news.cn/world/2023-03/02/c_1129409165.htm', 'date_time': datetime.datetime(2023, 3, 2, 0, 0)}]

```

## Function inputs
- target_day (dt.datetime): A datetime object representing the day on which to search for articles on . The function will retrieve articles published on this day.
- search_term (str): A string representing the search term to look for in article titles.

## Function outputs
- result_list (list): A list of dictionaries. Each dictionary contains information about a news article matching the search criteria. The dictionary has three keys: 'title', 'link', and 'date_time'. 'title' contains the title of the article, 'link' contains the URL of the article, and 'date_time' contains a datetime object representing the date and time the article was published.

## Requirements
- Python 3.x
- requests module
- json module
- datetime module
- re module
- urllib.parse module

## License
This function is released under the MIT License.