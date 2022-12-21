from django.shortcuts import render, redirect
import requests
from django.contrib import messages

def clima(request):

    if 'city' in request.POST:

        city = request.POST['city']

    else:

        city = 'Playa Del Carmen'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&lang=es&units=metric&appid=dab3655a33d81ea60ef2ad0d2a4071ce'


    r = requests.get(url.format(city)).json()

    try:

        clima = {

            'city' : city.title(),

            'descripcion' : r['weather'][0]['description'],

            'temperatura' : r['main']['temp'],

            'icon' : r['weather'][0]['icon'],
            
        }

    except KeyError:

        messages.error(request, 'Verifique el nombre de la ciudad')

        return redirect('clima')

        

    ctx = {'clima' : clima}

    return render(request, 'clima/index.html', ctx )


