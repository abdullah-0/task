# Job Task

## !!!Note!!!

Task is not completed. I tried my best to complete it only in Today. The thing which was not understand by me was to
write a queryset which group_by columns and generate their specific sums of impressions and clicks. Because django does
not has .group_by and .aggregate work on whole column. It is my humble request that 1: Please review my code and suggest
improvements. 2: Share with me the code base of solved task. Thanks.

## Urls

Send a post request with dataset file to upload data.

Send get request to send all data.

http://127.0.0.1:8000/api/metrics/

## Case URLs

1: http://127.0.0.1:8000/api/metrics?date_before=2017-06-01&order_by=clicks&order=des&group_by=channel,country,impressions,clicks

2: http://127.0.0.1:8000/api/metrics?date_before=2017-06-01&order_by=date&order=asc&group_by=date,installs

3:http://127.0.0.1:8000/api/metrics?order_by=revenue&order=des&date=2017-06-01&group_by=os,revenue

4:http://127.0.0.1:8000/api/metrics?order_by=cpi&order=des&group_by=country,spend,cpi&country=CA

## Project Setup

1: Clone the repo.

2: Setup environment using virtualenv or any other

3: Get into the project folder and run commands:

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py runserver`

