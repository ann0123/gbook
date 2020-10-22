from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('你好')

    def menu(req):
        meals =['三明治套餐','鬆餅套餐', '漢堡套餐']
        return render(req,'menu.html',{'meal_list':meals})

        def  food1(req,):
            return render 