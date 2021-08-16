from django.shortcuts import render,HttpResponse,redirect
from watermelon.utils import SqlInfo
from watermelon import models
from django.http import JsonResponse
from django.core import serializers
import json
# Create your views here.
def runoob(request):
    request.encoding='utf-8'
    if request.method == "GET":
        jira_id=request.GET.get("jira_id")
        summer=request.GET.get("summer")
        print("--------",summer,jira_id)
        if jira_id == None and summer==None:
            sql="select * from info limit 10;"
        elif jira_id != None and summer!=None:
            sql = ('select * from info where jira_id like "%' + str(jira_id) + '" and summary like "%' + str(summer)+'";')
        elif jira_id != None and summer == None:
            sql = ('select * from info where jira_id like "%' + str(jira_id)+'";')
        elif jira_id == None and summer != None:
            sql = ('select * from info where summary like "%' + str(summer)+'";')
        print(sql)
        info= SqlInfo.sqlInfo('local', sql, 1)
    return render(request, 'runoob.html',{"info": info})



def seleinfo(requrest):
    user_list = models.UseInfos.objects.all()
    data = serializers.serialize("json", user_list)
    print(data)
    return JsonResponse(json.loads(data), safe=False,json_dumps_params={'ensure_ascii':False})


def search(requrest):
    print("hello")
    return HttpResponse("hello")