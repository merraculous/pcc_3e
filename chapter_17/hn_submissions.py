from operator import itemgetter
import plotly.express as px

import requests

'''
    hn_submissions:
        Display most active discussions on Hacker News via histogram.
'''

# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts, sub_links, full_titles, comments = [], [], [], []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    
    # create dictionary of submissions with comments
    try:   
        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        continue
    else:        
        submission_dicts.append(submission_dict)
        
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

#Process data after sorting
for sub_dict in submission_dicts:
    #used for x-axis
    short_title = sub_dict['title'][:20]
    sub_link = f"<a href='{sub_dict['hn_link']}'>{short_title}</a>"
    sub_links.append(sub_link)

    #used for hover
    full_titles.append(submission_dict['title'])
    comments.append(sub_dict['comments'])
    
#visualization
title = "Most Commented Articles on Hacker News"
labels = {'x': 'Submission', 'y': 'Number of Comments'}
fig = px.bar(x=sub_links, y=comments, title=title, labels=labels,
             hover_name=full_titles)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
