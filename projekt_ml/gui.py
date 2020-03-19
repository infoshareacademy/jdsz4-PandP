from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

import tkinter.messagebox


####### pomocnicze zmienne listy itp #####################


kursy_walut = {'SGD': 0.7218272535233189, 'EUR': 1.1238612937944434, 'DKK': 0.14862087297218637, 'CAD': 0.8145423808817589, 'AUD': 0.8029694136890776, 'GBP': 1.5207327949927543, 'USD': 1.0, 'MXN': 0.05303800288397823, 'HKD': 0.12838130718608456, 'CHF': 1.0320771710383756, 'JPY': 0.008826237200036304, 'SEK': 0.12031274002718356, 'NZD': 0.7616139550831179, 'NOK': 0.12166770926093867, 'PLN': 0.3125, 'Specify goal in USD':1}

kraj_waluta = {'not considered': 'Specify goal in USD','Poland':'PLN','Other':'Specify goal in USD','Singapore': 'SGD', 'Ireland': 'EUR', 'Norway': 'NOK', 'New Zealand': 'NZD', 'Netherlands': 'EUR', 'Australia': 'AUD', 'Spain': 'EUR', 'Mexico': 'MXN', 'Hong Kong': 'HKD', 'United States': 'USD', 'Denmark': 'DKK', 'Japan': 'JPY', 'Luxembourg': 'EUR', 'Italy': 'EUR', 'Germany': 'EUR', 'Canada': 'CAD', 'Sweden': 'SEK', 'Great Britain (UK)': 'GBP', 'Belgium': 'EUR', 'Austria': 'EUR', 'Switzerland': 'CHF', 'France': 'EUR'}

main_chosen = ''





############# definicje fukcji ##########


# pomocnicza z kursu tkinter
def doNothing():
    print("ok ok I won't...")



# sprawdzenie i użycie testowe wybranych w widźetach parametrów
def checkParamas():
    tmpCAT = catMenu.get()
    tmpCNTR = countryMenu.get()
    tmpSUBCAT = subcatMenu.get()
    tmpGOAL = goalSpinbox.get()
    localCURR = kraj_waluta[tmpCNTR]
    localGOAL = round(float(tmpGOAL)/kursy_walut[localCURR],1)
    global main_chosen
    main_chosen = tmpCAT
    paramInfolabel.configure(text = f"Your Campaign's main category: {tmpCAT}\n "
                                    f"Your Campaing's sub category : {tmpSUBCAT}\n"
                                    f"Your Campaign's launch country: {tmpCNTR}\n"
                                    f"Your Campaign's goal is {tmpGOAL} USD ({localGOAL} in {localCURR} ).")

#pomocnicza funkcja sprawdzająca czy została zapisana wartość globalnej zmiennej main_chosen
def run_magic():
    print(main_chosen)



######### lista podkategorii do wyboru dla poszczególnych wybrbanych main_category
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


#funkcja, która daje listę podkategorii do wyboru na podstawie wybranej kategorii
def narrow_subcat(event):
    tmpCAT = catMenu.get()
    subcatMenu.configure(values = sub_categories[tmpCAT])









################### definicja interfesju ############
'''
Tkinter opiera się o "ramki" - frames, w których upakowuje się poszczególne fragmentu interfejsu:
- przyciski
- pola tekstowe
- menu wybieralne
- slidery 
- okienka inputu 
i pewnie jeszce wiele innych

ramek może być wiele poziomów, sam stosuje poniżej "ramki w większych ramkach"

'''



# ***** GUI start *****


#root - główna, najbardziej zewnętrzna ramka, definiowana jako klasa ThemedTk (themed, zeby skorzystać z predefiniowanego styu)
# "okno programu, nazwa root wzięta z kursu"

root = tk.ThemedTk()
root.geometry('1000x600')
root.set_theme("plastik")




# ***** The Toolbar - górny pasek z przyciakami  *****

#pierwsza zewnętrzna ramka, umieszczamy ją w oknie 'root', "pakujemy" na górze
toolbar = ttk.Frame(root)
toolbar.pack(side = TOP)

#### poniżej definicja przycików używanych, które "pakujemy" w w ramce "toolbar"
#### w dalszej części na podobnej zasadzie są zdefiniowane i "upakowane" pozostałe elementy interfejsu

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

MenusLabel1 = ttk.Label(menuFrame, text = 'Please specify campaign parameters    ', anchor = CENTER )
MenusLabel1.pack(side = TOP)


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

catMenuLabel = ttk.Label(catMenuFrame, text = 'Choose main category    ', anchor = N )
catMenuLabel.pack(side = LEFT)

catMenu = ttk.Combobox(catMenuFrame, values = mcats)
catMenu.bind('<<ComboboxSelected>>', narrow_subcat )
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


############# nad tym aktualnie pracuję, żeby był ładny slider połączony z okiekiem do wpisywania

# ** Goal selector *****
goalMenuFrame = Frame(menuFrame, padx = 2, pady = 2)


goalMenuLabel = ttk.Label(goalMenuFrame, text = 'Set Goal in USD         ' )
goalMenuLabel.pack(side = LEFT)

#goalSlider = ttk.Scrollbar(goalMenuFrame, orient = HORIZONTAL)
goalSpinbox = ttk.Spinbox(goalMenuFrame, from_ = 1, to = 20000000, command = checkParamas)
goalButton = Button(goalMenuFrame, text="OK", command=checkParamas)



#goalSlider.configure(command = goalSpinbox.set)

goalSpinbox.pack(side = LEFT)
#goalSlider.pack(side = BOTTOM, fill = X)
goalButton.pack(side = LEFT)

goalMenuFrame.pack(side = LEFT)



# ***** Main Window showing result *****


mainFrame1 = Frame(root)
mainFrame1.pack(side = TOP)



paramInfolabel = ttk.Label(mainFrame1, text = 'choose main cat')

paramInfolabel.pack(side = TOP, anchor = CENTER, fill = BOTH)



# ***** Status Bar *****

status = ttk.Label(root, text="PandP, ML_project, v0.01", relief=GROOVE, anchor=W)

status.pack(side=BOTTOM, fill=X)


# "włączenie" programu, interfesj musi się zawierać pomiędzy "otwarciem" roota i jego "mainloop'em", trochę jak w html'u
root.mainloop()