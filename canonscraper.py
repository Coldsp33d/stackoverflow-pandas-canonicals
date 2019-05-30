"""Retrieve vote score (in sorted order by post type) for all posts listed in README.md."""
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import html 

user_id = '4909087'
user_url = f'https://api.stackexchange.com/2.2/users/{user_id}?order=desc&sort=reputation&site=stackoverflow'
username = requests.get(user_url).json()['items'][0]['display_name']

repo = 'https://github.com/Coldsp33d/stackoverflow-pandas-canonicals/blob/master/README.md'
posts_url = 'https://api.stackexchange.com/2.2/posts/{}?pagesize=100&order=desc&sort=votes&site=stackoverflow'
url = {
    'question': 'https://api.stackexchange.com/2.2/questions/{}?order=desc&sort=activity&site=stackoverflow',
    'answer': 'https://api.stackexchange.com/2.2/answers/{}?order=desc&sort=activity&site=stackoverflow&filter=!-*jbN.OXJB.4&pagesize=100'
}

soup = BeautifulSoup(requests.get(repo).text, 'lxml')

ids = set()
for tag in soup.find_all(href=re.compile('stackoverflow.com/.*')):
    ids = ids.union(re.findall(r"\b\d+\b", tag['href']))

ids -= {user_id}


data = requests.get(posts_url.format(';'.join(ids))).json()['items']
df = pd.DataFrame([
      {'post_id': str(p['post_id']), 'type': p['post_type']} 
      for p in data if p['owner']['display_name'] == username
    ]
)
# Get the answers to all my questions.
canonq_answers = (df.query('type == "question"')['post_id']
                    .astype(int)
                    .add(1)
                    .astype(str)
                    .to_frame()
                    .assign(type='answer'))
df = pd.concat([df, canonq_answers], ignore_index=True)

data = (df.groupby('type')[['post_id']]
          .agg(';'.join)
          .apply(lambda x: requests.get(url[x.name].format(x['post_id'])).json()['items'], axis=1)
          .to_frame('post_info')
          .apply(lambda x: [{
                f'post_id': str(p[f'{x.name}_id']), 
                'title': html.unescape(p['title']), 
                'score': p['score'], 
                'link': p['link']
              } for p in x['post_info']
            ], axis=1)
          .sum())

print(df.merge(pd.DataFrame(data), on='post_id')
        .sort_values(['type', 'score'], ascending=[1, 0])
        .reset_index(drop=1)
        .set_index('post_id')
        .to_string())


"""
              type                                               link  score                                              title
post_id                                                                                                                        
53645883    answer  https://stackoverflow.com/questions/53645882/p...    162                                 Pandas Merging 101
54028200    answer  https://stackoverflow.com/questions/54028199/f...     73        For loops with pandas - When should I care?
53954986    answer  https://stackoverflow.com/questions/20625582/h...     45  How to deal with SettingWithCopyWarning in Pan...
50444347    answer  https://stackoverflow.com/questions/50444346/f...     45               Fast punctuation removal with pandas
53779987    answer  https://stackoverflow.com/questions/53779986/d...     35  Dynamic Expression Evaluation in pandas using ...
...
53645882  question  https://stackoverflow.com/questions/53645882/p...    139                                 Pandas Merging 101
54028199  question  https://stackoverflow.com/questions/54028199/f...     60        For loops with pandas - When should I care?
50444346  question  https://stackoverflow.com/questions/50444346/f...     46               Fast punctuation removal with pandas
53927460  question  https://stackoverflow.com/questions/53927460/s...     34         Select rows in pandas MultiIndex DataFrame
53779986  question  https://stackoverflow.com/questions/53779986/d...     32  Dynamic Expression Evaluation in pandas using ...
...
"""
