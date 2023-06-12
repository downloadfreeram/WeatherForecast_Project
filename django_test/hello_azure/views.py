from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import requests
import datetime
def hisdata(request):
    template = loader.get_template('hisdata.html')
    if request.method == "POST":
        api = "93b8d4523a104f9d9325366e22a459af"
        city = request.POST["city"]
        code = request.POST["code"]
        start = int(datetime.datetime.timestamp(datetime.datetime.strptime(request.POST["start"],'%Y-%m-%d')))
        end = int(datetime.datetime.timestamp(datetime.datetime.strptime(request.POST["end"],'%Y-%m-%d')))
        url = "https://history.openweathermap.org/data/2.5/history/city?q="+city+","+code+"&type=day&start="+str(start)+"&end="+str(end)+"&appid="+api
        response = requests.get(url)
        data = response.json()
        if data["cod"] == "200":
            query2 = ""
            query3 = "<span class='txt'>Date</span><span class='txt'>Temperature</span><span class='txt'>Description</span><span class='txt'>Humidity</span><span class='txt'>Pressure</span>"
            for i in range(0,data['cnt']-1):
                query2 += '<div class="res"><span class="time">'+str(datetime.datetime.fromtimestamp(data['list'][i]['dt']))+"</span><span class='val'>"+str(round(data['list'][i]['main']['temp']-273.15,1))+"</span><span class='weatherInfo'>"+data['list'][i]['weather'][0]['main']+"</span><span class='humidity'>"+str(data['list'][i]['main']['humidity'])+"</span><span class='pressure'>"+str(data['list'][i]['main']['pressure'])+"</span></div>"
            return render(request, 'hisdata.html',{"query2":query2,"query3":query3})
        else:
            print("Error"+str(data["cod"]))
            return render(request, 'hisdata.html',{})
    else:
        return render(request, 'hisdata.html',{})
    
def index(request):
    template = loader.get_template('index.html')
    choice = 1
    if request.method == "POST":
        api = "29478dc229001c21ab8068cf86854d8f"
        city = request.POST["city"]
        choice = request.POST.get("choice")
        url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?q="+city+"&appid="+api
        response = requests.get(url)
        data = response.json()
        if data["cod"] == "404" or data["cod"] == "400":
            print("Error")
            alert="The city cannot be found"
            return render(request, 'index.html',{"alert":alert})
        else:
            alert = ""
            query = ""
            for i in range(0,int(choice)):   
                query += '<div class="res"><div class="dateBox">'+str(datetime.datetime.fromtimestamp((data['list'][i]['dt']-3600)+(data['city']['timezone']-3600)))+"</div><div class='tempBox'><img src='https://openweathermap.org/img/wn/"+data['list'][i]['weather'][0]['icon']+"@2x.png' alt='"+data['list'][i]['weather'][0]['main']+"'><br>Min temperature : <span class='val'>"+str(round(data['list'][i]['main']['temp_min']-273.15,1))+"</span>"+"<br>Max temperature : <span class='val'>"+str(round(data['list'][i]['main']['temp_max']-273.15,1))+"</span></div><div class='humBox'>Humidity: "+str(data['list'][i]['main']['humidity'])+"%</div><div class='windBox'>Wind: "+str(data['list'][i]['wind']['speed'])+" km/h</div><div class='presBox'>Pressure: "+str(data['list'][i]['main']['pressure'])+" hPa</div></div>"
            name = "Currently checking weather for: "+city+","+data["city"]["country"]
            return render(request, 'index.html',{"query":query,"name":name,"alert":alert})
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

