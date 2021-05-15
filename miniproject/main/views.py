from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Plot
from bson.objectid import ObjectId


@login_required
def home(request):
    # {
    #     "type": "B",
    #     "name": "Graph",
    #     "yAxis": {
    #         "name": "Y Axis",
    #         "unit": "kg",
    #         "minRange": "0",
    #         "maxRange": "10",
    #     },
    #     "xAxis": {
    #         "name": "X axis",
    #         "unit": "time",
    #         "minRange": "0",
    #         "maxRange": "20",
    #     },
    #     "data": [
    #         {
    #             "name": "Apple",
    #             "value": "10",
    #             "color": "red",
    #         },
    #         {
    #             "name": "Orange",
    #             "value": "15",
    #             "color": "red",
    #         }
    #     ]
    # }
    plots = Plot.objects.filter(
        user=request.user).values_list('_id', "name", "type")
    data = map(lambda x: {"id": x[0],
               "name": x[1], "type": x[2]}, plots)
    return render(request, 'main/home.html', {"plots": data})


@login_required
def plot(request, plotId):
    plot = Plot.objects.get(_id=ObjectId(plotId))
    return render(request, 'main/plot.html', {"plot": plot})


@login_required
def create(request):
    graphType = request.GET.get('graph-type')
    graphId = request.GET.get('id', "")
    isedit = request.GET.get('edit', "false")
    print(graphType, graphId)
    context = {
        "graphType": graphType,
        "graphId": graphId,
        "edit": isedit,
    }
    return render(request, 'main/createPlot.html', context)
