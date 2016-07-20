from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^login_page$', views.login_page),
    url(r'^add_course_and_student$', views.add_course_and_student),
    url(r'^deleteNewListUser/(?P<id>\d+)$', views.deleteNewListUser),
]