import plotly.offline as plt
import plotly.graph_objects as go

#Plotting functions

def Bar_plotter(graph_data):
    df = graph_data['dataFrame']
    data = [go.Bar(x=df['label'],y=df['data'],text=df['data'],textposition='outside',
            marker = {'color':df['color']}
    )]
    
    layout = go.Layout(title = graph_data['title'],
                        xaxis = {'title':f"{graph_data['xAxis']['name']}({graph_data['xAxis']['unit']})"},
                        yaxis = {'title':f"{graph_data['yAxis']['name']}({graph_data['yAxis']['unit']})",
                             'range':[graph_data['yAxis']['minRange'],graph_data['yAxis']['maxRange']]}
                )
    fig = go.Figure(data=data,layout=layout)
    plot_div = plt.plot(fig, output_type='div')
    return plot_div


def Scatter_plotter(graph_data):
    df = graph_data['dataSet']
    data = [go.Scatter(x=entry['x'],y=entry['y'],mode='markers',name=entry['name'],
                       marker={'color':entry['color']}) 
            for entry in df]
    layout = go.Layout(title = graph_data['title'],
                        xaxis = {'title':f"{graph_data['xAxis']['name']}({graph_data['xAxis']['unit']})"},
                        yaxis = {'title':f"{graph_data['yAxis']['name']}({graph_data['yAxis']['unit']})",
                              'range':[graph_data['yAxis']['minRange'],graph_data['yAxis']['maxRange']]}
                      )
    fig = go.Figure(data=data ,layout=layout)
    plot_div = plt.plot(fig, output_type='div')
    return plot_div


def Line_plotter(graph_data):
    df = graph_data['dataSet']
    data = [go.Scatter(x=entry['x'],y=entry['y'],mode='lines',name=entry['name'],
                       line={'color':entry['color']}) 
            for entry in df]
    layout = go.Layout(title = graph_data['title'],
                        xaxis = {'title':f"{graph_data['xAxis']['name']}({graph_data['xAxis']['unit']})",
                              'range':[graph_data['xAxis']['minRange'],graph_data['xAxis']['maxRange']]},
                        yaxis = {'title':f"{graph_data['yAxis']['name']}({graph_data['yAxis']['unit']})",
                              'range':[graph_data['yAxis']['minRange'],graph_data['yAxis']['maxRange']]}
                      )
    fig = go.Figure(data=data ,layout=layout)
    plot_div = plt.plot(fig, output_type='div')
    return plot_div



def Grouped_bar_plotter(graph_data):
    df = graph_data['dataFrame']
    data = [go.Bar(x=df['label'],y=df[df.columns[i]],text=df[df.columns[i]],textposition='outside',
            marker = {'color':graph_data['color'][i-1]},
            name = df.columns[i]
    ) for i in range(1,len(df.columns))]
    layout = go.Layout(
             title = graph_data['title'],
             xaxis = {'title':f"{graph_data['xAxis']['name']}({graph_data['xAxis']['unit']})"},
             yaxis = {'title':f"{graph_data['yAxis']['name']}({graph_data['yAxis']['unit']})",
                             'range':[graph_data['yAxis']['minRange'],graph_data['yAxis']['maxRange']]}
    )
    fig = go.Figure(data=data,layout=layout)
    plot_div = plt.plot(fig, output_type='div')
    return plot_div


def Pie_plotter(graph_data):
    df = graph_data['dataFrame']
    data = go.Pie(labels=df['label'],values=df['data'],textinfo='label+percent+value',
                        marker = {'colors':df['color']},
                        textposition = 'outside',opacity = 0.9)
    layout = go.Layout(title = graph_data['title'])
    fig = go.Figure(data=data,layout=layout)
    plot_div = plt.plot(fig, output_type='div')
    return plot_div

#dictionary for selecting corresponding function
plotter_type_dictionary = {'B':Bar_plotter,'C':Grouped_bar_plotter,'S':Scatter_plotter,
                            'L':Line_plotter,'P':Pie_plotter}

#dictionary for selecting corresponding plotting function
def plotter(graph_data):
    return plotter_type_dictionary[graph_data['type']](graph_data)

