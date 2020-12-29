from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from mainsite.views import homepage, lotto, form, showpost, mychart, kinderchart, chart, asiavisitor

urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('form/', form),
    path('asiavisitor/', asiavisitor),
    path('asiavisitor/<int:bid>/',asiavisitor),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('kindergarten/', kinderchart),
    path('kindergarten/<int:bid>/', kinderchart),
    path('chartbydate/<int:year>/<int:month>/',chart),
    path('chartbydate/<int:year>/',chart),
    path('', homepage),
]
