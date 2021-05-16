from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Plot
from bson.objectid import ObjectId
from .plotter import plotter
from .dataAPI import data_API
from json import dumps


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
        update_data = data_API(request.POST)
        Plot.objects.filter(_id=ObjectId(graphId)).update(**update_data)
        return redirect(reverse('create') + f"?graph-type={graphType}&id={graphId}&edit=true")

    if plot[0]:
        jsonData = dumps(plot[0]['data'])
    else:
        jsonData = dumps({})

    context = {
        "graphType": graphType,
        "graphId": graphId,
        "edit": isedit,
        "plot": div,
        "graphData": plot[0],
        "data": jsonData,
    }
    return render(request, 'main/createPlot.html', context)


def delete(request):
    Id = request.GET.get('id')
    res = Plot.objects.get(_id=ObjectId(Id)).delete()
    return redirect('home')


def add(request):
    data = data_API(request.POST, request.user)
    uploaded = Plot.objects.create(**data)
    return redirect('home')
