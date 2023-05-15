from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from tabulate import tabulate
import requests

def index(request):
    template = loader.get_template('index.html')
    if request.method == "POST":
        api = "29478dc229001c21ab8068cf86854d8f"
        city = request.POST["city"]
        url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?q="+city+"&appid="+api
        response = requests.get(url)
        data = response.json()
        if data["cod"] == "404" or data["cod"] == "400":
            print("Error")
            return render(request, 'index.html',{})
        else:
            query = []
            for i in range(1,25):
                # query += data['list'][i]['dt_txt']+" - "+str(round(data['list'][i]['main']['temp']-273.15,1))+" C"+"\n"
                query.append([data['list'][i]['dt_txt'],data['list'][i]['weather'][0]['main'],str(round(data['list'][i]['main']['temp']-273.15,1))])
            name = ","+data["city"]["country"]
            tab = tabulate(query,headers=['Date','Weather','Temperature'],tablefmt='html')
            return render(request, 'index.html',{"query":tab,"c":city,"name":name})
    else:
        return render(request, 'index.html',{})

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello.html', context)
    else:
        return redirect('index')

