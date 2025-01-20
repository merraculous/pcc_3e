Projects with PCC 
===

Python practice through pcc. Accidentally used previous version repo to 
work through PCC text so few projects can be found elsewhere. Previous 
repo found [here](https://github.com/merraculous/pcc).

While an accident to use pcc repo instead of pcc_3e, it gave me an 
opportunity to consolidate the missing gaps between versions and gave 
me more focus to notice differences in code. Definitely a worthwhile 
challenge, though unintentional. 

Downloading Data
---

Load and extract data from CSV files and create visualizations based on 
information. In this project, used weather information for both Sitka 
and Death Valley cities. Exercises show comparisons between the two as 
well. `sitka_highs_lows.py` and `death_valley_highs_lows.py` will show 
graphs for individual cities while `exercises.py` will show comparison 
charts as well as precipitation levels for Sitka. 

Visulization & APIs
---

Use APIs to access data from GitHub and HackerNews. `repo_visual.py` 
prompts user for language they would like to explore and shows graph of 
most starred repositories on GitHub for that language. `hn_submissions.py` 
shows most active discussions on HackerNews by looking at articles with 
most comments.

Django App
---

Web app called Learning Log that allows users to log the topics they’re 
interested in and make journal entries as they learn about each topic. 
The Learning Log home page will describe the site and invite users to 
either register or log in. Once logged in, a user can create new topics, 
add new entries, and read and edit existing entries.

Uses a virtual environment, django 4.2.18, and django_bootstrap5. 
`learning_logs` and `accounts` created apps using django. `accounts` 
uses default django standards. `learning_logs` defines topics and 
their entries in models and creates forms appropriately. Views for topics
and entries are login required otherwise website will prompt user to 
register.

Run site with:

    python manage.py runserver

Credits Python Crash Course - Third Edition
===

A Hands-On, Project-Based Introduction to Programming
---

This is a collection of resources for [Python Crash Course, Third Edition](https://nostarch.com/python-crash-course-3rd-edition), an introductory programming book from [No Starch Press](https://nostarch.com) by Eric Matthes. Click here for a [much cleaner version](https://ehmatthes.github.io/pcc_3e/) of these online resources.

If you have any questions about Python Crash Course, feel free to get in touch:

Email: ehmatthes@gmail.com

Twitter: [@ehmatthes](http://twitter.com/ehmatthes/)