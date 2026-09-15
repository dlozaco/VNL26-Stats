import pandas as pd

df = pd.read_csv('vnl2026_TBD.csv')

correcciones_equipo = {
    "Luciano De Cecco": "ARGENTINA",
    "Trevor Clevenot": "FRANCE",
    "Ruben Schott": "GERMANY",
    "David Fiel Rodriguez": "CUBA",
    "Danny Demyanenko": "CANADA",
    "Stephen Timothy Maar": "CANADA",
    "Kyle Dagostino": "USA",
    "Kentaro Takahashi": "JAPAN",
    "Douglas Correia De Souza": "BRAZIL",
    "Tomas Lopez": "ARGENTINA",
    "Jani Kovačič": "SLOVENIA",
    "Javier Octavio Concepcion Rojas": "CUBA",
    "Tonček Štern": "SLOVENIA",
    "Amirhossein Esfandiar": "IRAN",
    "Ali Ramezani": "IRAN",
    "Ignacio Luengas": "ARGENTINA",
    "Muhammed Kaya": "TÜRKIYE",
    "Oleksandr Nalozhnyi": "UKRAINE",
    "Sharone Vernon-Evans": "CANADA",
    "Eric Loeppky": "CANADA",
    "Victor Ramon Andreu Flores": "CUBA",
    "Kamil Rychlicki": "ITALY",
    "Lennert Van Elsen": "BELGIUM",
    "Lorenzo Cortesia": "ITALY",
    "Giovannimaria Gargiulo": "ITALY",
    "Filip John": "GERMANY",
    "Ertuğrul Gazi Metin": "TÜRKIYE",
    "Mateusz Poreba": "POLAND",
    "Bartosz Firszt": "POLAND",
    "Mikolaj Sawicki": "POLAND",
    "Beytullah Hatipoglu": "TÜRKIYE",
    "Landon Currie": "CANADA",
    "Aliaksei Nasevich": "POLAND",
    "Paolo Porro": "ITALY",
    "Leandro Ausibio Mosca": "ITALY",
    "Georgi Tatarov": "BULGARIA",
    "Serhii Yevstratov": "UKRAINE",
    "Michal Gierzot": "POLAND",
    "Basil Dermaux": "BELGIUM",
    "Pierre Perin": "BELGIUM",
    "Joscha Kunstmann": "GERMANY",
    "Samuel Carazzai de Morais Neufeld": "BRAZIL",
    "Mattia Orioli": "ITALY",
    "Mattia Boninfante": "ITALY",
    "Amir Mohammad Golzadeh": "IRAN",
    "Jakdiel Contreras Acosta": "CUBA",
    "Bartosz Gomułka": "POLAND",
    "Adrian Markiewicz": "POLAND",
    "Gustavo Maciel": "BRAZIL",
    "Andrii Chelenyak": "UKRAINE",
    "Henri Leon": "FRANCE",
    "Emran Kook Jili": "IRAN",
    "Oleksandr Boiko": "UKRAINE",
    "Bryan Camino Martinez": "CUBA",
    "Domenico Pace": "ITALY",
    "Pouya Ariakhah": "IRAN",
    "Marcel Bakaj": "POLAND",
    "Bartosz Zych": "POLAND",
    "Cody Hudson": "CANADA",
    "Valentin Predan": "SLOVENIA",
    "Jakub Ciunajtis": "POLAND",
    "Zhihong Xue": "CHINA"
}

df['team'] = df.apply(
    lambda row: correcciones_equipo.get(row['name'], row['team']) 
    if pd.isna(row['team']) or row['team'] in ["-", "TBD"] 
    else row['team'], 
    axis=1
)

df.to_csv('vnl2026.csv', index=False)
print("Saved filed as vnl2026.csv'")