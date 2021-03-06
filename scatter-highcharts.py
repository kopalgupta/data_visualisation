# used to create dynamic graphs
from highcharts import Highchart
chart = Highchart() # new chart object

options = {
    'chart': {
        'type': 'scatter',
        'zoomType': 'xy'
    },

    'title': {
        'text': 'Highchart Scatter'
    },

    'legend': {
        'enabled': True
    },

   'xAxis': {
        'title':{
            'text': 'Followers (thousands)'
            }
        },

    'yAxis': {
        'title': {
            'text': 'Friends (thousands)'
        }  
    },

}

data1 = [[161, 51], [167, 59], [159, 49], [157, 63], [155, 53]]

data2 = [[174, 165], [175, 171], [193, 180], [186, 172], [187, 178]]

chart.set_dict_options(options)

chart.add_data_set(data1, 'scatter', 'Celebrity accounts', color='rgba(223, 83, 83,0.5)') # data, type_of_chart, legend_text, color
chart.add_data_set(data2, 'scatter', 'Normal user accounts', color='rgba(119, 152, 191,0.5)')

chart.save_file('./highcharts-scatter') # write to the file and save