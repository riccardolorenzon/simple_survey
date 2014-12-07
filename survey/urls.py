from django.conf.urls import patterns, include, url

from django.contrib import admin

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name= "root"),
    url(r'^survey_load/$', views.load_survey, name = "load-survey"),
    url(r'^survey/(P<survey_id>\d+)/$', views.survey_view, name ="survey-detail"),
    url(r'^admin_login/$', views.admin_login, name="admin-login"),
    url(r'^admin_panel/$', views.admin_panel, name="admin-panel"),
    url(r'^admin_panel/survey_delete/$', views.survey_delete, name="admin-survey-delete")
)
