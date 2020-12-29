from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from datetime import datetime
from mainsite.models import Post, AccessInfo, Branch, StoreIncome, Kindergarten, SchoolStu, Visitors, Asiacountry

def homepage(request):
    record = AccessInfo()
    record.save()
    visits = len(AccessInfo.objects.all())
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals())
    
def mychart(request, bid=0):
    now = datetime.now()
    branches = Branch.objects.all()

    if bid == 0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(branch=bid)
    title = "各分店營收情形"
    return render(request, "mychart.html", locals())

def chart(request, year=0, month=0):
    now = datetime.now()
    branches = Branch.objects.all()

    if year==0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(income_year=year)
        if month>0:
            data = data.filter(income_month=month)
    
    if year>0 and month>0:
        title = "{}年{}月各分店營收情形".format(year, month)
    elif year>0:
        title = "{}年各分店營收情形".format(year, month)
    else:
        title = "各分店營收情形"

    return render(request, "mychart.html", locals())

def kinderchart(request, bid=0):
    now = datetime.now()
    kindergartens = Kindergarten.objects.all()
    if bid == 0:
        data = SchoolStu.objects.all()
    else:
        data = SchoolStu.objects.filter(kindergarten=bid)
    return render(request, "kindergarten.html",locals())


def showpost(request, slug):
	now = datetime.now()
	try:
		post = Post.objects.get(slug=slug)
		return render(request, "post.html", locals())
	except:
		return redirect("/")   

def lotto(request):
    lucky = random.randint(1, 42)
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1, 42))
    
    return render(request, "lotto.html", locals())

def form(request):
    now = datetime.now()
    try:
        user_ids = request.GET['user_id']
        user_passes = request.GET['user_pass']
    except:
        user_ids = None
    return render(request, 'form.html', locals())

def asiavisitor(request, bid=0):
    now = datetime.now()
    asiavisitors = Asiacountry.objects.all()
    if bid == 0:
        data = Visitors.objects.all()
    else:
        data = Visitors.objects.filter(country=bid)
    
    return render(request, "asiavisitor.html",locals())