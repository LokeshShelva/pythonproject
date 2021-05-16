
def data_API(data):
    cleaned = {
        "name": data['graphTitle'],
        "description": data['graphDescription'],
        "xAxis": {
            "name": data["xAxisName"],
            "minRange": data["xAxisMinRange"],
            "maxRange": data["xAxisMaxRange"]
        },
        "yAxis": {
            "name": data["yAxisName"],
            "minRange": data["yAxisMinRange"],
            "maxRange": data["yAxisMaxRange"]
        },
    }

    return cleaned
