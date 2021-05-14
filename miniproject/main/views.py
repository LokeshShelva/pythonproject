from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Plot
from bson.objectid import ObjectId


@login_required
def home(request):
    # p = Plot.objects.create(
    #     user=request.user,
    #     type="B",
    #     name="Graph 2",
    #     yAxis={
    #         "name": "Axis",
    #         "unit": "kg",
    #         "minRange": "0",
    #         "maxRange": "10",
    #     },
    #     xAxis={
    #         "name": "X axis",
    #         "unit": "time",
    #         "minRange": "0",
    #         "maxRange": "20",
    #     },
    #     data=[
    #         {
    #             "name": "lime",
    #             "value": "10",
    #             "color": "#fc0303",
    #         },
    #         {
    #             "name": "tomata",
    #             "value": "15",
    #             "color": "#0367fc",
    #         },
    #         {
    #             "name": "idk",
    #             "value": "17",
    #             "color": "#03fc5e",
    #         },
    #         {
    #             "name": "hello",
    #             "value": "7",
    #             "color": "#b503fc",
    #         }
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
