import ipywidgets as widgets
from ipywidgets import HBox, Label

main_category = widgets.Dropdown(
    options=['Art',
             'Fashion',
             'Music',
             'Crafts',
             'Photography',
             'Design',
             'Film & Video',
             'Food',
             'Journalism',
             'Publishing',
             'Dance',
             'Comics',
             'Technology',
             'Theater',
             'Games'],
    disabled=False,)

sub_category = widgets.Dropdown()

def narrow_subcat(*args):
    sub_categories = {'Art': ['Art 1','Art 2'],
                      'Comics': ['Comics 1','Comics 2'],
                      'Crafts': ['Crafts 1','Crafts 2'],
                      'Dance': ['Dance 1','Dance 2'],
                      'Design': ['Design 1','Design 2'],
                      'Fashion': ['Fashion 1','Fashion 2'],
                      'Film & Video': ['Film Video 1', 'Film Video 2'],
                      'Food': ['Food 1','Food 2'],
                      'Games': ['Games 1','Games 2'],
                      'Journalism': ['Journalism 1','Journalism 2'],
                      'Music': ['Music 1','Music 2'],
                      'Photography': ['Photo 1','Photo 2'],
                      'Publishing': ['Publish 1', 'Publish 2'],
                      'Technology': ['Tech 1','Tech 2'],
                      'Theater': ['Theater 1', 'Theater 2']}
                      
    sub_category.options = list(sub_categories[main_category.value])

main_category.observe(narrow_subcat)

country = widgets.Dropdown(
    options=['USA', 'France'],
    disabled=False,
)

goal = widgets.BoundedIntText(
    value=1,
    min=0,
    max=1000000000,
    step=1,
    disabled=False
)

currency = widgets.Dropdown(
    options=['HKD','SGD','SEK','JPY','NOK','AUD','GBP','CHF','MXN','CAD','DKK','EUR','NZD','USD'],
    value='USD',
    disabled=False,
)

launch_date = widgets.DatePicker(
    disabled=False
)

duration = widgets.IntSlider(
    min=1,
    max=90,
    step=1,
    description='Days:',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
