import ast


def data_API(data, user):
    if user:
        cleaned = {
            "name": data['graphTitle'],
            "user": user,
            "description": data['graphDescription'],
            "xAxis": {
                "name": data["xAxisName"],
                "unit": data["xAxisUnit"],
                "minRange": data["xAxisMinRange"],
                "maxRange": data["xAxisMaxRange"]
            },
            "yAxis": {
                "name": data["yAxisName"],
                "unit": data["xAxisUnit"],
                "minRange": data["yAxisMinRange"],
                "maxRange": data["yAxisMaxRange"]
            },
            "data": ast.literal_eval(data["data"]),
        }
    else:
        cleaned = {
            "name": data['graphTitle'],
            "description": data['graphDescription'],
            "xAxis": {
                "name": data["xAxisName"],
                "unit": data["xAxisUnit"],
                "minRange": data["xAxisMinRange"],
                "maxRange": data["xAxisMaxRange"]
            },
            "yAxis": {
                "name": data["yAxisName"],
                "unit": data["xAxisUnit"],
                "minRange": data["yAxisMinRange"],
                "maxRange": data["yAxisMaxRange"]
            },
            "data": ast.literal_eval(data["data"]),
        }

    return cleaned
