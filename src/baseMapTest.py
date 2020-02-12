import pandas as pd
import io
import plotly.graph_objs as go 
from plotly.offline import plot

txt = """   state   abv ibu id  beer    style   ounces  brewery city
0   AK  25  17  25  25.0    25.0    25  25  25
1   AL  10  9   10  10.0    10.0    10  10  10
2   AR  5   1   5   5.0 5.0 5   5   5
3   AZ  44  24  47  47.0    46.0    47  47  47
4   CA  182 135 183 183.0   183.0   183 183 183
5   CO  250 146 265 265.0   263.0   265 265 265
6   CT  27  6   27  27.0    27.0    27  27  27
7   DC  8   4   8   8.0 8.0 8   8   8
8   DE  1   1   2   2.0 2.0 2   2   2
9   FL  56  37  58  58.0    58.0    58  58  58
10  GA  16  7   16  16.0    16.0    16  16  16
"""

gb_state = pd.read_csv(io.StringIO(txt), delim_whitespace=True)


data = dict(type='choropleth',
            locations=gb_state['state'],
            locationmode='USA-states',
            text=gb_state['state'],
            z=gb_state['beer'],
            ) 

layout = dict(geo = dict(scope='usa',
                         showlakes= False)
             )

choromap = go.Figure(data=[data], layout=layout)
#plot(choromap)
choromap.show()
