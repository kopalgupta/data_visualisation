# used to represent the frequency of posts by user
# used to create dynamic graphs
from highcharts import Highchart

chart = Highchart() # new highchart object

# graph attributes
options = {
    'chart': {
        'type': 'bar',
        'zoomType': 'xy'
    },

    'title': {
        'text': 'Highchart Bar'
    },

    'legend': {
        'enabled': True
    },

   'xAxis': {
        'categories': ['User 1', 'User 2', 'User 3', 'User 4', 'User 5'],
        },

    'yAxis': {
        'title': {
            'text': 'Number of posts (thousands)'
        }  
    },

}

# we can use our own data
data1 = [107, 31, 635, 203, 2]
data2 = [133, 156, 947, 408, 6]
data3 = [973, 914, 4054, 732, 34]
data4 = [1052, 954, 4250, 740, 38]

chart.set_dict_options(options) # add options to the chart object

chart.add_data_set(data1, 'bar', 'Day 1') # data, type_of_chart, legend_text
chart.add_data_set(data2, 'bar', 'Day 2')
chart.add_data_set(data3, 'bar', 'Day 3')
chart.add_data_set(data4, 'bar', 'Day 4')

chart.save_file('./highcharts-bar') # it will crete an html file. Used to save the html file
