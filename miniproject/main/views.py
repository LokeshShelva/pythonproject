from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Plot
from bson.objectid import ObjectId


@login_required
def home(request):
    # p = Plot.objects.create(
    #     user=request.user,
    #     type="C",
    #     name="Compound Bar graph 1",
    #     yAxis={
    #         "name": "weight",
    #         "unit": "kg",
    #         "minRange": "0",
    #         "maxRange": "25",
    #     },
    #     xAxis={
    #         "name": "fruits",
    #         "unit": "",
    #         "minRange": "5",
    #         "maxRange": "25",
    #     },
    #     data=[
    #         {
    #             "name": "Apple",
    #             "value": ["10", "15", "11"],
    #             "color": ["#fc0303", "#3c32a8", "#32a87b"],
    #             "field": ["April", "May", "June"]
    #         },
    #         {
    #             "name": "Orange",
    #             "value": ["5", "12", "17"],
    #             "color": ["#fc0303", "#3c32a8", "#32a87b"],
    #             "field": ["April", "May", "June"]
    #         },
    #         {
    #             "name": "Banana",
    #             "value": ["11", "10", "17"],
    #             "color": ["#fc0303", "#3c32a8", "#32a87b"],
    #             "field": ["April", "May", "June"]
    #         },
    #         {
    #             "name": "Mango",
    #             "value": ["5", "20", "17"],
    #             "color": ["#fc0303", "#3c32a8", "#32a87b"],
    #             "field": ["April", "May", "June"]
    #         },
    #     ]
    # )
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
    plots = Plot.objects.filter(user=request.user).values()
    data = map(lambda x: {"id": x["_id"],
                          "name": x["name"], "type": x["type"]}, plots)
    return render(request, 'main/home.html', {"plots": data})


@login_required
def plot(request, plotId):
    plot = Plot.objects.get(_id=ObjectId(plotId))
    return render(request, 'main/plot.html', {"plot": plot})


@login_required
def create(request):
    return render(request, 'main/createPlot.html')
