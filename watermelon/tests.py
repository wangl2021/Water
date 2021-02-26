from django.test import TestCase

# Create your tests here.

jira_id=1
summer=2
sql = ('select * from info where jira_id like "%'+str(jira_id)+'" and summer like %'+str(summer))
print(sql)
print(sql)