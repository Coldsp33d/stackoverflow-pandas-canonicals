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

data = pd.DataFrame(df.groupby('type')[['post_id']]
                      .agg(';'.join)
                      .apply(lambda x: requests.get(url[x.name].format(x['post_id'])).json()['items'], axis=1)
                      .to_frame('post_info')
                      .apply(lambda x: [{
                            f'post_id': str(p[f'{x.name}_id']), 
                            'title': html.unescape(p['title']), 
                            'score': p['score'], 
                            'link': p['link'],
                            'creation_date': p['creation_date'],
                          } for p in x['post_info']
                        ], axis=1)
                      .sum())
# Get the age of each post.
days_since_creation = (pd.Timestamp('today') - pd.to_datetime(data.pop('creation_date'), unit='s', origin='unix')).dt.days
# How many votes you're expected to get in a year. This is expected to change with age, number of votes, and (for answers) position on the page.
data.insert(data.columns.get_loc('score') + 1,
            'passive_rep_rate', 
            (data['score'] / days_since_creation * 365.25).astype(int))

print(df.merge(data, on='post_id')
        .sort_values(['type', 'passive_rep_rate'], ascending=[1, 0])
        .reset_index(drop=1)
        .set_index('post_id')
        .to_string())


"""
              type                                                                           title  score  passive_rep_rate                                                                                                                                        link
post_id                                                                                                                                                                                                                                                                
55557758    answer                               How to iterate over rows in a DataFrame in Pandas    576               430                            https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas/55557758#55557758
53645883    answer                                                              Pandas Merging 101    571               341                                                           https://stackoverflow.com/questions/53645882/pandas-merging-101/53645883#53645883
54508052    answer                                         Convert pandas dataframe to NumPy array    269               178                                      https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array/54508052#54508052
61922965    answer                                pandas GroupBy columns with NaN (missing) values     35               161                               https://stackoverflow.com/questions/18429491/pandas-groupby-columns-with-nan-missing-values/61922965#61922965
56746204    answer                            Creating an empty Pandas DataFrame, then filling it?    175               155                           https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it/56746204#56746204
...
53645882  question                                                              Pandas Merging 101    395               236                                                                             https://stackoverflow.com/questions/53645882/pandas-merging-101
53927460  question                                      Select rows in pandas MultiIndex DataFrame    147                90                                                     https://stackoverflow.com/questions/53927460/select-rows-in-pandas-multiindex-dataframe
54432583  question                       When should I ever want to use pandas apply() in my code?    109                71                                         https://stackoverflow.com/questions/54432583/when-should-i-ever-want-to-use-pandas-apply-in-my-code
54028199  question                         Are for-loops in pandas really bad? When should I care?    104                65                                          https://stackoverflow.com/questions/54028199/are-for-loops-in-pandas-really-bad-when-should-i-care
53779986  question                         Dynamic Expression Evaluation in pandas using pd.eval()     57                34                                          https://stackoverflow.com/questions/53779986/dynamic-expression-evaluation-in-pandas-using-pd-eval
...
"""
