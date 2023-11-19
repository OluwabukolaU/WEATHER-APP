from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
       
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'groningen'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a41a74f3931a4382181c6d96f01f18dc'
    PARAMS = {'units':'metric'}
    
    API_KEY = 'AIzaSyCFg9QeL8Z1n4-Lzbzt7Wl9uTBpMcmd7e8'
    SEARCH_ENGINE_ID = 'f4ac752e0b9da40aa'
    
    query = city + "1920*1080"
    page = 1
    start = (page-1)*10 + 1
    searchType = "image"
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
    
    data=requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]["link"]
    
    try:
        data = requests.get(url,PARAMS).json()
    
        descripton = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
    
        day = datetime.date.today()
        return render(request,'weatherapp/index.html', {'description':descripton,'icon':icon,'temp':temp,'day':day, 'city':city, 'exception_occured':False, 'image_url':image_url})
    
    except:
        exception_occured = True
        messages.error(request, 'City Not Found in my API')
        day=datetime.date.today()
        
        return render(request,'weatherapp/index.html', {'description':'clear sky','icon':'01d','temp':25,'day':day, 'city':city, 'exception_occured':True})

    
   