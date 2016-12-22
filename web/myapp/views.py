import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Weather

def append_data(request):
    weather_data = Weather(
        nodeid  = request.GET['nodeid'],
        temp    = float(request.GET['temp']),
        humi    = float(request.GET['humi']),
        israin  = (request.GET['israin'] == "True")
    )
    weather_data.save()
    return HttpResponse("Recieved", content_type='text/plain')


def show_table(request, nodeid):
    weather_data = Weather.objects.all()
    #.order_by('-nodeid')[:10][::-1]
    data = []
    real_data = {}

    # Reformat data from DB to format that template can understand.
    for row in weather_data:
        data.append({
            'time'	:row.time,
            'nodeid':row.nodeid,
            'temp'	:row.temp,
            'humi'	:row.humi,
            'israin':row.israin
        })

    chart_data = []
    node_ids = []
    for i in weather_data:
        # Collect node_id.
        node_ids.append(i.nodeid)

        if int(i.nodeid) is int(nodeid):
            real_data = i

            # Create chart data.
            chart_data.append({
                #'date'	: "%s %s %s %s %s"%(i.time.hour,i.time.minute,i.time.day,i.time.month,i.time.year),
                'date'	: "%02d %02d %d"%(i.time.day, i.time.month,i.time.year),
                'temp'	: float(i.temp)
            })

    # Use only unique id.
    node_ids = list(set(node_ids))
    node_ids.sort()

    return render(request, "myapp/home.html", {
        'data': data,
        'real_data': real_data,
        'nodeid_array': node_ids,
        'chart_data': json.dumps(chart_data).replace('\"', '\'')
    })

def show_home(request):
    return show_table(request, 1)


def data_exchanger(request):
    print request.GET
    nodeid=json.loads(request.GET.get('nodeid'))
    print nodeid
    server_data = {'server_data':[
        {'key':'value0'},
        {'key':'value1'},
    ]}
    return JsonResponse(server_data)
