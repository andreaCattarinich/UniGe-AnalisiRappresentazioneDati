dizionario_nomi = {
    'ID'      : 'ID',
    'mese'    : 'Mese',
    'annrif'  : 'Anno',
    'progind' : 'Indice progressivo', # indice dell'intervista individuale
    'sesso'   : 'Sesso',
    'eta10'   : 'Età',
    'staciv4' : 'Stato civile',
    'reg'     : 'Regione',
    'rip'     : 'Zona d Italia',
    'istr4'   : 'Livello di Istruzione',
    'condogg' : 'Stato di impiego',
    'posiz4'  : 'Grado di impiego',
    'ateco3'  : 'Settore di lavoro',
    'cond4'   : 'Impiego',
    'ORARIO'  : 'Tipo di impiego',
    'RAPP'    : 'Rapporto di lavoro',
    'CODPROF7': 'Categoria Professionale',
    'progesc' : 'Indice dell escursione',
    'DEST_EIE': 'Italia/Estero',
    'DEST_ERE': 'Destinazione (regioni italiane o paesi esteri)',
    'DEST_EPR': 'Destinazione (città)',
    'MOTESC'  : 'Motivo dell escursione',
    'PARTESC' : 'Partecipanti fuori dalla famiglia',
    'NPARTESC': 'Partecipanti escursione',
    'EMEZZO'  : 'Mezzo',
    'TRIM'    : 'Stagione'
}

eta_mapping = {
    1: ' <=14',
    2: '15-24',
    3: '25-34',
    4: '35-44',
    5: '45-54',
    6: '55-64',
    7: '65-74',
    8: '>=75'
}

sesso_mapping={
    1: 'Uomo',
    2: 'Donna'
}


stato_civile_mapping = {
    1: 'Celibe/nubile',
    2: 'Coniugato',
    3: 'Separato/Divorziato',
    4: 'Vedovo'
}

regione_mapping = {
    '010': 'Piemonte',
    '020': "Valle d'Aosta/Vallee d'Aoste",
    '030': 'Lombardia',
    '040': 'Trentino A.Adige/Sudtirol',
    '050': 'Veneto',
    '060': 'Friuli-Venezia Giulia',
    '070': 'Liguria',
    '080': 'Emilia-Romagna',
    '090': 'Toscana',
    '100': 'Umbria',
    '110': 'Marche',
    '120': 'Lazio',
    '130': 'Abruzzo',
    '140': 'Molise',
    '150': 'Campania',
    '160': 'Puglia',
    '170': 'Basilicata',
    '180': 'Calabria',
    '190': 'Sicilia',
    '200': 'Sardegna'
}

zona_mapping = {
    1: 'Nord',
    2: 'Nord',
    3: 'Centro',
    4: 'Sud',
    5: 'Sud'
}

livello_di_istruzione_mapping = {
    1: 'Media',
    2: 'Media',
    3: 'Diploma',
    4: 'Laurea '
}

stato_di_impiego_mapping = {
    0: 'Disoccupato/a',
    1: 'Impiegato/a',
    2: 'Disoccupato/a',
    3: 'Disoccupato/a'
}

grado_di_impiego_mapping = {
    0: 'Nessuno',
    1: 'Dipendente',
    2: 'Apprendista',
    3: 'Imprenditore',
    4: 'Lavoratore autonomo'
}

settore_di_lavoro_mapping = {
    0: 'Nessuno',
    1: 'Settore Primario',
    2: 'Settore Secondario',
    3: 'Settore Terziario'
}

impiego_mapping = {
    0: 'Nessuno (meno di 14 anni)',
    1: 'Impiegato',
    2: 'Cercatore di Lavoro',
    3: 'Casalinga/Studente/Altra Condizione',
    4: 'Pensionato'
}

tipo_di_impiego_mapping = {
    0: 'Nessuno (meno di 14 anni)',
    1: 'Tempo Pieno',
    2: 'Tempo Parziale'
}

RAPP_mapping = {
    0: 'Nessuno (meno di 14 anni)',
    1: 'A Termine',
    2: 'A Tempo Indeterminato'
}

destinazione_italia_estero_mapping = {
    1: 'Italia',
    2: 'Estero'
}

destinazione_regioni_stato_mapping = {
    1: 'Piemonte',
    2: 'Valle d\'Aosta',
    3: 'Lombardia',
    4: 'Trentino-Alto Adige/Sudtirol',
    5: 'Veneto',
    6: 'Friuli-Venezia Giulia',
    7: 'Liguria',
    8: 'Emilia-Romagna',
    9: 'Toscana',
    10: 'Umbria',
    11: 'Marche',
    12: 'Lazio',
    13: 'Abruzzo',
    14: 'Molise',
    15: 'Campania',
    16: 'Puglia',
    17: 'Basilicata',
    18: 'Calabria',
    19: 'Sicilia',
    20: 'Sardegna',
    121: 'Austria',
    122: 'Belgio',
    123: 'Danimarca',
    124: 'Finlandia',
    125: 'Francia',
    126: 'Germania',
    127: 'Grecia',
    128: 'Irlanda',
    130: 'Lussemburgo',
    132: 'Paesi Bassi',
    133: 'Polonia',
    134: 'Portogallo',
    135: 'Regno Unito',
    136: 'Repubblica Ceca',
    137: 'Slovacchia',
    138: 'Spagna',
    139: 'Svezia',
    142: 'Ungheria',
    159: 'Bulgaria',
    161: 'Cipro',
    163: 'Estonia',
    164: 'Lettonia',
    165: 'Lituania',
    166: 'Malta',
    167: 'Romania',
    169: 'Slovenia',
    172: 'Croazia',
    200: 'Paesi Extra-UE',
    235: 'Regno Unito',
    300: 'Nord America',
    400: 'America Centrale e Meridionale',
    500: 'Africa',
    600: 'Asia-Oceania'
}

destinazione_citta_mapping = {
    1: 'Torino',
    2: 'Vercelli',
    3: 'Novara',
    4: 'Cuneo',
    5: 'Asti',
    6: 'Alessandria',
    7: 'Valle d\'Aosta',
    8: 'Imperia',
    9: 'Savona',
    10: 'Genova',
    11: 'La Spezia',
    12: 'Varese',
    13: 'Como',
    14: 'Sondrio',
    15: 'Milano',
    16: 'Bergamo',
    17: 'Brescia',
    18: 'Pavia',
    19: 'Cremona',
    20: 'Mantova',
    21: 'Bolzano',
    22: 'Trento',
    23: 'Verona',
    24: 'Vicenza',
    25: 'Belluno',
    26: 'Treviso',
    27: 'Venezia',
    28: 'Padova',
    29: 'Rovigo',
    30: 'Udine',
    31: 'Gorizia',
    32: 'Trieste',
    33: 'Piacenza',
    34: 'Parma',
    35: 'Reggio nell\'Emilia',
    36: 'Modena',
    37: 'Bologna',
    38: 'Ferrara',
    39: 'Ravenna',
    40: 'Forlì-Cesena',
    41: 'Pesaro e Urbino',
    42: 'Ancona',
    43: 'Macerata',
    44: 'Ascoli Piceno',
    45: 'Massa-Carrara',
    46: 'Lucca',
    47: 'Pistoia',
    48: 'Firenze',
    49: 'Livorno',
    50: 'Pisa',
    51: 'Arezzo',
    52: 'Siena',
    53: 'Grosseto',
    54: 'Perugia',
    55: 'Terni',
    56: 'Viterbo',
    57: 'Rieti',
    58: 'Roma',
    59: 'Latina',
    60: 'Frosinone',
    61: 'Caserta',
    62: 'Benevento',
    63: 'Napoli',
    64: 'Avellino',
    65: 'Salerno',
    66: "L'Aquila",
    67: 'Teramo',
    68: 'Pescara',
    69: 'Chieti',
    70: 'Campobasso',
    71: 'Foggia',
    72: 'Bari',
    73: 'Taranto',
    74: 'Brindisi',
    75: 'Lecce',
    76: 'Potenza',
    77: 'Matera',
    78: 'Cosenza',
    79: 'Catanzaro',
    80: 'Reggio di Calabria',
    81: 'Trapani',
    82: 'Palermo',
    83: 'Messina',
    84: 'Agrigento',
    85: 'Caltanissetta',
    86: 'Enna',
    87: 'Catania',
    88: 'Ragusa',
    89: 'Siracusa',
    90: 'Sassari',
    91: 'Nuoro',
    92: 'Cagliari',
    93: 'Pordenone',
    94: 'Isernia',
    95: 'Oristano',
    96: 'Biella',
    97: 'Lecco',
    98: 'Lodi',
    99: 'Rimini',
    100: 'Prato',
    101: 'Crotone',
    102: 'Vibo Valentia',
    103: 'Verbano-Cusio-Ossola',
    104: 'Olbia-Tempio',
    105: 'Ogliastra',
    106: 'Medio Campidano',
    107: 'Carbonia-Iglesias',
    108: 'Monza e della Brianza',
    109: 'Fermo',
    110: 'Barletta-Andria-Trani',
    111: 'Sud Sardegna',
    999: 'Sconosciuto (Unknown)'
}

motivo_escursione_mapping = {
    1: 'Vacanza',
    2: 'Famiglia',
    3: 'Cultura',
    4: 'Cultura',
    5: 'Famiglia',
    6: 'Shopping',
    7: 'Lavoro',
    8: 'Famiglia',
    9: 'Cultura',
    10: 'Vacanza',
    11: 'Altro'
}

mezzo_mapping = {
    1: 'Aereo',
    2: 'Treno',
    3: 'Nave',
    4: 'Auto',
    5: 'Auto',
    6: 'Autobus',
    7: 'Autobus',
    8: 'Auto',
    9: 'Moto',
    10:'Altro',
    11:'Auto'
}

stagione_mapping = {
    1: 'Gennaio-Marzo',
    2: 'Aprile-Giugno',
    3: 'Luglio-Settembre',
    4: 'Ottobre-Dicembre'
}


