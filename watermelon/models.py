# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Peony(models.Model):
    create_time = models.IntegerField()
    jira_id = models.CharField(max_length=64)
    commit_id = models.CharField(max_length=128)
    summary = models.CharField(max_length=128, blank=True, null=True)
    back_developer = models.CharField(max_length=16, blank=True, null=True)
    tester = models.CharField(max_length=16, blank=True, null=True)
    client_developer = models.CharField(db_column='Client_developer', max_length=16, blank=True, null=True)  # Field name made lowercase.
    web_developer = models.CharField(max_length=16, blank=True, null=True)
    producter = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peony'


class UseInfos(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'use_infos'


class UserInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user_info'
