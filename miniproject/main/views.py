from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Plot
from bson.objectid import ObjectId
from .plotter import plotter
from .dataAPI import data_API


@login_required
def home(request):
    # list1 = []
    # list2 = []

    # for i in range(50):
    #     list1.append([str(random.randint(5, 100)),
    #                  str(random.randint(500, 5000))])
    #     list2.append([str(random.randint(5, 100)),
    #                  str(random.randint(500, 5000))])

    # Plot.objects.create(
    #     user=request.user,
    #     type="S",
    #     name="Scatter plot",
    #     xAxis={
    #         "name": "X axis",
    #         "unit": "cm",
    #         "minRange": "0",
    #         "maxRange": "125",
    #     },
    #     yAxis={
    #         "name": "Y axis",
    #         "unit": "plot",
    #         "minRange": "100",
    #         "maxRange": "6000",
    #     },
    #     data=[
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

    if graphId != "":
        plot = Plot.objects.filter(_id=ObjectId(graphId)).values()
        div = plotter(plot[0])
    else:
        div = None
        plot = [""]

    if request.method == "POST":
        print(data_API(request.POST))

    context = {
        "graphType": graphType,
        "graphId": graphId,
        "edit": isedit,
        "plot": div,
        "graphData": plot[0],
    }
    return render(request, 'main/createPlot.html', context)
