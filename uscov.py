import pandas as pd
import numpy as np
import geoviews as gv
import geoviews.feature as gf
import geoviews.tile_sources as gvts
from geoviews import dim, opts
gv.extension('bokeh', 'matplotlib')
from bokeh.models import HoverTool, WMTSTileSource
# from bokeh.models import WMTSTileSource
import math
import ipywidgets as widgets



def nth_root(num,root):
   answer = num ** (1/root) 
   return answer



covmap=pd.read_csv('https://docs.google.com/spreadsheets/d/1R7ejcUT6-hZ743Wu87uE3lOl8u5xh1nv5_iiLPpV8K8/export?format=csv&gid=372103765')



covmap_gv_points = gv.Points(covmap, ['Longitude', 'Latitude'], ['State', 'County', 'Population', 'Cases', 'Deaths', 'Color'])




tooltips = [('LONGITUDE', '$x'),
            ('LATITUDE', '$y'),
            ('STATE','@State'),
            ('County','@County'),
            ('Population','@Population'),
            ('Cases','@Cases'),
            ('Deaths','@Deaths'),
            ] 


hover = HoverTool(tooltips=tooltips)


                
geomap = gv.WMTS(WMTSTileSource(url=\
   'https://server.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{Z}/{Y}/{X}.jpg'))

map = (covmap_gv_points.opts(opts.Points(width=1200, height=700, alpha=0.3,
                color='orangered', hover_line_color='black',  
                line_color='black',
                tools=[hover],size=nth_root(dim('Cases'),3),
                hover_fill_color=None, hover_fill_alpha=0.5)) * geomap.options(width=1300, height=800, xaxis=None, yaxis=None, show_grid=False, alpha=0.8)) 



out = widgets.Output(layout={'border': '1px solid black'})

with out:
    display(map)