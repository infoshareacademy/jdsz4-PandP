from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

import tkinter.messagebox



main_chosen = ''

def doNothing():
    print("ok ok I won't...")


def checkParamas():
    tmpCAT = catMenu.get()
    tmpCNTR = countryMenu.get()
    global main_chosen
    main_chosen = tmpCAT
    sample_label.configure(text = f'you chose main cat: {tmpCAT} , and country: {tmpCNTR}')
    narrow_subcat(tmpCAT)


def run_magic():
    print(main_chosen)


# o tutaj jest funkcja, która wykorzystuje słownik zbudowany na zasadzie {główne kategorie: adekwatne podkategorie},
# żeby ustawić w dropdownie odpowiednie podkategorie
# (to jest ogólnie de facto tak, że tworzymy zmienne typu widget, które mają odpowiednie parametry)


sub_categories = {'Art':
                          ['Sculpture',
                           'Conceptual Art',
                           'Illustration',
                           'Public Art',
                           'Mixed Media',
                           'Video Art',
                           'Art',
                           'Installations',
                           'Ceramics',
                           'Textiles',
                           'Painting',
                           'Digital Art',
                           'Performance Art'],
                      'Comics':
                          ['Comic Books',
                           'Events',
                           'Anthologies',
                           'Graphic Novels',
                           'Comics',
                           'Webcomics'],
                      'Crafts':
                          ['Weaving',
                           'Letterpress',
                           'Crochet',
                           'Candles',
                           'Taxidermy',
                           'Crafts',
                           'Knitting',
                           'Embroidery',
                           'Pottery',
                           'Glass',
                           'Quilts',
                           'Printing',
                           'DIY',
                           'Stationery',
                           'Woodworking'],
                      'Dance':
                          ['Dance',
                           'Spaces',
                           'Residencies',
                           'Workshops',
                           'Performances'],
                      'Design':
                          ['Graphic Design',
                           'Product Design',
                           'Civic Design',
                           'Interactive Design',
                           'Architecture',
                           'Typography',
                           'Design'],
                      'Fashion':
                          ['Couture',
                           'Childrenswear',
                           'Footwear',
                           'Fashion',
                           'Accessories',
                           'Jewelry',
                           'Apparel',
                           'Ready-to-wear',
                           'Pet Fashion'],
                      'Film & Video':
                          ['Television',
                           'Horror',
                           'Film & Video',
                           'Science Fiction',
                           'Music Videos',
                           'Documentary',
                           'Family',
                           'Animation',
                           'Fantasy',
                           'Experimental',
                           'Movie Theaters',
                           'Comedy',
                           'Webseries',
                           'Festivals',
                           'Romance',
                           'Drama',
                           'Shorts',
                           'Narrative Film',
                           'Thrillers',
                           'Action'],
                      'Food':
                          ['Spaces',
                           'Vegan',
                           'Drinks',
                           'Restaurants',
                           'Food',
                           'Events',
                           'Farms',
                           'Cookbooks',
                           "Farmer's Markets",
                           'Food Trucks',
                           'Community Gardens',
                           'Small Batch',
                           'Bacon'],
                      'Games':
                          ['Playing Cards',
                           'Puzzles',
                           'Games',
                           'Mobile Games',
                           'Gaming Hardware',
                           'Video Games',
                           'Tabletop Games',
                           'Live Games'],
                      'Journalism':
                          ['Print',
                           'Video',
                           'Journalism',
                           'Web',
                           'Photo',
                           'Audio'],
                      'Music':
                          ['Classical Music',
                           'Faith',
                           'Chiptune',
                           'Blues',
                           'Indie Rock',
                           'Pop',
                           'Kids',
                           'Hip-Hop',
                           'World Music',
                           'Jazz',
                           'Latin',
                           'Metal',
                           'Comedy',
                           'Country & Folk',
                           'R&B',
                           'Rock',
                           'Music',
                           'Punk',
                           'Electronic Music'],
                      'Photography':
                          ['Photobooks',
                           'Animals',
                           'Places',
                           'Nature',
                           'People',
                           'Fine Art',
                           'Photography'],
                      'Publishing':
                          ['Radio & Podcasts',
                           'Art Books',
                           'Literary Journals',
                           'Poetry',
                           'Calendars',
                           'Comedy',
                           'Letterpress',
                           'Literary Spaces',
                           "Children's Books",
                           'Zines',
                           'Academic',
                           'Publishing',
                           'Anthologies',
                           'Periodicals',
                           'Nonfiction',
                           'Fiction',
                           'Translations',
                           'Young Adult'],
                      'Technology':
                          ['Technology',
                           'Wearables',
                           'Apps',
                           'Space Exploration',
                           'Sound',
                           'Gadgets',
                           'Software',
                           '3D Printing',
                           'Robots',
                           'DIY Electronics',
                           'Hardware',
                           'Web',
                           'Makerspaces',
                           'Camera Equipment',
                           'Flight',
                           'Fabrication Tools'
                           ],
                      'Theater':
                          ['Spaces',
                           'Comedy',
                           'Festivals',
                           'Experimental',
                           'Musical',
                           'Theater',
                           'Plays',
                           'Immersive'],
                      '':
                          ['choose main category first']
                           }

def narrow_subcat(maincat):

    subcatMenu.values = list(sub_categories[maincat])












# ***** GUI strt *****



root = tk.ThemedTk()
root.geometry('1000x600')
root.set_theme("plastik")


# cols = 4
# rows = 4



# ***** The Toolbar *****

toolbar = ttk.Frame(root)
toolbar.pack(side = TOP)


# *** toolbar buttons *****
insertButt = ttk.Button(toolbar, text="check main category", command=checkParamas)
insertButt.pack(side=LEFT, padx=10, pady=10)
printButt = ttk.Button(toolbar, text="Print", command=run_magic)
printButt.pack(side=LEFT, padx=10, pady=10)
quitButt = ttk.Button(toolbar, text="quit", command=root.quit)
quitButt.pack(side=RIGHT, padx=10, pady=10)








# ***** Menus Frame *****

menuFrame = Frame(root)
menuFrame.configure(padx = 30,pady = 30)


menuFrame.pack(side = TOP)



#** Main Category selector *****

catMenuFrame = Frame(menuFrame, padx = 2, pady = 2)

mcats = ['Art',
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
             'Games']

catMenuLabel = ttk.Label(catMenuFrame, text = 'Choose Main Category    ', anchor = N )
catMenuLabel.pack(side = LEFT)

catMenu = ttk.Combobox(catMenuFrame, values = mcats)
catMenu.pack(side = LEFT)

catMenuFrame.pack(side = TOP)

# ** Sub Category selector *****

subcatMenuFrame = Frame(menuFrame, padx = 2, pady = 2)


subcatMenuLabel = ttk.Label(subcatMenuFrame, text = 'Choose Sub-Category     ' )
subcatMenuLabel.pack(side = LEFT)

subcatMenu = ttk.Combobox(subcatMenuFrame, values = sub_categories[main_chosen])
subcatMenu.pack(side = LEFT)

subcatMenuFrame.pack(side = TOP)


# ** Country selector *****
countryMenuFrame = Frame(menuFrame, padx = 2, pady = 2)


country_list = [ 'Australia',
                'Austria',
                'France',
                'Switzerland',
                'Belgium',
                'Denmark',
                'Canada',
                'Singapore',
                'New Zealand',
                'Hong Kong',
                'Sweden',
                'Germany',
                'Ireland',
                'Luxembourg',
                'Japan',
                'Netherlands',
                'Italy',
                'Great Britain (UK)',
                'Spain',
                'United States',
                'Mexico',
                'Norway']

countryMenuLabel = ttk.Label(countryMenuFrame, text = 'Choose Country          ' )
countryMenuLabel.pack(side = LEFT)

countryMenu = ttk.Combobox(countryMenuFrame, values = country_list)
countryMenu.pack(side = LEFT)

countryMenuFrame.pack(side = TOP)



# ***** Main Window showing result *****


mainFrame1 = Frame(root)
mainFrame1.pack(side = TOP)



sample_label = ttk.Label(mainFrame1, text = 'choose main cat')

sample_label.pack(side = TOP, anchor = CENTER, fill = BOTH)




# ***** Status Bar *****

status = ttk.Label(root, text="PandP, ML_project, v0.01", relief=GROOVE, anchor=W)

#status.grid(row = rows, columnspan = cols, sticky = S)
status.pack(side=BOTTOM, fill=X)



root.mainloop()