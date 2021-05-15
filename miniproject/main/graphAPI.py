import pandas as pd
import ast
# API


def Bar_API(graph_data):
    dataSet = graph_data['data']
    df = pd.DataFrame()
    name, color, value = [], [], []
    for entry in dataSet:
        name.append(entry['name'])
        color.append(entry['color'])
        value.append(float(entry['value']))
    df['data'] = value
    df['label'] = name
    df['color'] = color
    graph_data['yAxis']['minRange'], graph_data['yAxis']['maxRange'] = float(
        graph_data['yAxis']['minRange']), float(graph_data['yAxis']['maxRange'])

    dictionary = {
        'type': graph_data['type'], 'dataFrame': df, 'title': graph_data['name'],
        'xAxis': graph_data['xAxis'], 'yAxis': graph_data['yAxis']
    }
    return dictionary


def Grouped_Bar_API(graph_data):
    df = pd.DataFrame()
    dataSet = graph_data['data']
    df['label'] = []
    color = dataSet[0]['color']
    graph_data['yAxis']['minRange'], graph_data['yAxis']['maxRange'] = float(
        graph_data['yAxis']['minRange']), float(graph_data['yAxis']['maxRange'])

    for f in dataSet[0]['field']:
        df[f] = []
    for entry in dataSet:
        row_val = [entry['name']]+[int(x)
                                   for x in ast.literal_eval(entry['value'])]
        new_row = {k: v for k, v in zip(df.columns, row_val)}
        df = df.append(new_row, ignore_index=True)
    dictionary = {
        'type': graph_data['type'], 'dataFrame': df, 'title': graph_data['name'], 'color': color,
        'xAxis': graph_data['xAxis'], 'yAxis': graph_data['yAxis']
    }
    return dictionary


def Scatter_API(graph_data):
    ds = graph_data['data']
    for entry in ds:
        x = [int(i[1]) for i in ast.literal_eval(entry['value'])]
        y = [int(i[0]) for i in ast.literal_eval(entry['value'])]
        new = {'x': x, 'y': y}
        entry.update(new)
    dictionary = {
        "type": graph_data['type'], 'title': graph_data['name'], 'dataSet': ds, 'xAxis': graph_data['xAxis'], 'yAxis': graph_data['yAxis']
    }
    return dictionary


def Line_API(graph_data):
    df = graph_data['data']
    for entry in df:
        x = [int(i[1]) for i in ast.literal_eval(entry['value'])]
        y = [int(i[0]) for i in ast.literal_eval(entry['value'])]
        new = {'x': x, 'y': y}
        entry.update(new)
    dictionary = {
        "type": graph_data['type'], 'title': graph_data['name'], 'dataSet': df, 'xAxis': graph_data['xAxis'], 'yAxis': graph_data['yAxis']
    }
    return dictionary


def Pie_API(graph_data):
    dataSet = graph_data['data']
    df = pd.DataFrame()
    name, color, value = [], [], []
    for entry in dataSet:
        name.append(entry['name'])
        color.append(entry['color'])
        value.append(int(entry['value']))
    df['data'] = value
    df['label'] = name
    df['color'] = color
    dictionary = {
        'type': graph_data['type'], 'dataFrame': df, 'title': graph_data['name']
    }
    return dictionary


# dictionary to select corresponding function
API_type_dictionary = {'B': Bar_API, 'C': Grouped_Bar_API,
                       'S': Scatter_API, 'L': Line_API, 'P': Pie_API}

# # selects corresponding function


def graphAPI(graph_data):
    return API_type_dictionary[graph_data['type']](graph_data)
