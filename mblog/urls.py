from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, form, showpost, mychart, kinderchart


urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('form/', form),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('kindergarten/', kinderchart),
    path('kindergarten/<int:bid>/', kinderchart),
    path('', homepage),
]
