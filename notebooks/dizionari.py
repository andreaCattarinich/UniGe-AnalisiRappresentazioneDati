dizionario_nomi = {
    'mese'    : 'Mese',
    'annrif'  : 'Anno',
    'progind' : 'Indice progressivo', # indice dell'intervista individuale
    'sesso'   : 'Sesso',
    'eta10'   : 'Età (0-10)', # TODO: convertre le categorie di età in range corretti
    'staciv4' : 'Stato civile',
    'reg'     : 'Regione',
    'rip'     : 'Zona d\'Italia',
    'istr4'   : 'Livello di istruzione',
    'condogg' : 'Stato di impiego',
    'posiz4'  : 'Grado di impiego',
    'ateco3'  : 'Settore di lavoro',
    'cond4'   : 'Impiego',
    'ORARIO'  : 'Tipo di impiego',
    'RAPP'    : 'Rapporto di lavoro',
    'CODPROF7': 'Categoria Professionale',
    'progesc' : 'Indice dell escursione',
    'DEST_EIE': 'Destinazione (italia o estero)',
    'DEST_ERE': 'Destinazione (regioni italiani o paesi esteri)',
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

stato_civile_mapping = {
    '1': 'Celibe/nubile',
    '2': 'Coniugato',
    '3': 'Separato/Divorziato',
    '4': 'Vedovo'
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
    '0': 'Nessuno (meno di 14 anni)',
    '1': 'Impiegato',
    '2': 'Cercatore di lavoro',
    '3': 'Inattivo'
}

grado_di_impiego_mapping = {
    '0': 'Nessuno (meno di 14 anni)',
    '1': 'Manager, Esecutivo, Supervisore, Dipendente',
    '2': 'Apprendista lavoratore, Lavoratore domestico per conto di un\'azienda',
    '3': 'Imprenditore, Professionista autonomo',
    '4': 'Lavoratore autonomo, Socio cooperativo, Assistente, Freelancer, Fornitore di lavoro occasionale'
}

settore_di_lavoro_mapping = {
    '0': 'Nessuno (meno di 14 anni)',
    '1': 'Settore Primario',
    '2': 'Settore Secondario',
    '3': 'Settore Terziario'
}

impiego_mapping = {
    '0': 'Nessuno (meno di 14 anni)',
    '1': 'Impiegato',
    '2': 'Cercatore di Lavoro',
    '3': 'Casalinga/Studente/Altra Condizione',
    '4': 'Pensionato'
}

tipo_di_impiego_mapping = {
    '0': 'Nessuno (meno di 14 anni)',
    '1': 'Tempo Pieno',
    '2': 'Tempo Parziale'
}

RAPP_mapping = {
    '0': 'Nessuno (meno di 14 anni)',
    '1': 'A Termine',
    '2': 'A Tempo Indeterminato'
}

destinazione_italia_estero_mapping = {
    1: 'Italia',
    2: 'Estero'
}

destinazione_regioni_stato_mapping = {
    '001': 'Piemonte',
    '002': 'Valle d\'Aosta',
    '003': 'Lombardia',
    '004': 'Trentino-Alto Adige/Sudtirol',
    '005': 'Veneto',
    '006': 'Friuli-Venezia Giulia',
    '007': 'Liguria',
    '008': 'Emilia-Romagna',
    '009': 'Toscana',
    '010': 'Umbria',
    '011': 'Marche',
    '012': 'Lazio',
    '013': 'Abruzzo',
    '014': 'Molise',
    '015': 'Campania',
    '016': 'Puglia',
    '017': 'Basilicata',
    '018': 'Calabria',
    '019': 'Sicilia',
    '020': 'Sardegna',
    '121': 'Austria',
    '122': 'Belgio',
    '123': 'Danimarca',
    '124': 'Finlandia',
    '125': 'Francia',
    '126': 'Germania',
    '127': 'Grecia',
    '128': 'Irlanda',
    '130': 'Lussemburgo',
    '132': 'Paesi Bassi',
    '133': 'Polonia',
    '134': 'Portogallo',
    '135': 'Regno Unito',
    '136': 'Repubblica Ceca',
    '137': 'Slovacchia',
    '138': 'Spagna',
    '139': 'Svezia',
    '142': 'Ungheria',
    '159': 'Bulgaria',
    '161': 'Cipro',
    '163': 'Estonia',
    '164': 'Lettonia',
    '165': 'Lituania',
    '166': 'Malta',
    '167': 'Romania',
    '169': 'Slovenia',
    '172': 'Croazia',
    '200': 'Paesi Extra-UE (escluso Regno Unito)',
    '235': 'Regno Unito (Non-UE dal 2020)',
    '300': 'Nord America',
    '400': 'America Centrale e Meridionale',
    '500': 'Africa',
    '600': 'Asia-Oceania'
}

destinazione_citta_mapping = {
    '001': 'Torino',
    '002': 'Vercelli',
    '003': 'Novara',
    '004': 'Cuneo',
    '005': 'Asti',
    '006': 'Alessandria',
    '007': 'Valle d\'Aosta/Vallee d\'Aoste',
    '008': 'Imperia',
    '009': 'Savona',
    '010': 'Genova',
    '011': 'La Spezia',
    '012': 'Varese',
    '013': 'Como',
    '014': 'Sondrio',
    '015': 'Milano',
    '016': 'Bergamo',
    '017': 'Brescia',
    '018': 'Pavia',
    '019': 'Cremona',
    '020': 'Mantova',
    '021': 'Bolzano/Bozen',
    '022': 'Trento',
    '023': 'Verona',
    '024': 'Vicenza',
    '025': 'Belluno',
    '026': 'Treviso',
    '027': 'Venezia',
    '028': 'Padova',
    '029': 'Rovigo',
    '030': 'Udine',
    '031': 'Gorizia',
    '032': 'Trieste',
    '033': 'Piacenza',
    '034': 'Parma',
    '035': 'Reggio nell\'Emilia',
    '036': 'Modena',
    '037': 'Bologna',
    '038': 'Ferrara',
    '039': 'Ravenna',
    '040': 'Forlì-Cesena',
    '041': 'Pesaro e Urbino',
    '042': 'Ancona',
    '043': 'Macerata',
    '044': 'Ascoli Piceno',
    '045': 'Massa-Carrara',
    '046': 'Lucca',
    '047': 'Pistoia',
    '048': 'Firenze',
    '049': 'Livorno',
    '050': 'Pisa',
    '051': 'Arezzo',
    '052': 'Siena',
    '053': 'Grosseto',
    '054': 'Perugia',
    '055': 'Terni',
    '056': 'Viterbo',
    '057': 'Rieti',
    '058': 'Roma',
    '059': 'Latina',
    '060': 'Frosinone',
    '061': 'Caserta',
    '062': 'Benevento',
    '063': 'Napoli',
    '064': 'Avellino',
    '065': 'Salerno',
    '066': "L'Aquila",
    '067': 'Teramo',
    '068': 'Pescara',
    '069': 'Chieti',
    '070': 'Campobasso',
    '071': 'Foggia',
    '072': 'Bari',
    '073': 'Taranto',
    '074': 'Brindisi',
    '075': 'Lecce',
    '076': 'Potenza',
    '077': 'Matera',
    '078': 'Cosenza',
    '079': 'Catanzaro',
    '080': 'Reggio di Calabria',
    '081': 'Trapani',
    '082': 'Palermo',
    '083': 'Messina',
    '084': 'Agrigento',
    '085': 'Caltanissetta',
    '086': 'Enna',
    '087': 'Catania',
    '088': 'Ragusa',
    '089': 'Siracusa',
    '090': 'Sassari',
    '091': 'Nuoro',
    '092': 'Cagliari',
    '093': 'Pordenone',
    '094': 'Isernia',
    '095': 'Oristano',
    '096': 'Biella',
    '097': 'Lecco',
    '098': 'Lodi',
    '099': 'Rimini',
    '100': 'Prato',
    '101': 'Crotone',
    '102': 'Vibo Valentia',
    '103': 'Verbano-Cusio-Ossola',
    '104': 'Olbia-Tempio',
    '105': 'Ogliastra',
    '106': 'Medio Campidano',
    '107': 'Carbonia-Iglesias',
    '108': 'Monza e della Brianza',
    '109': 'Fermo',
    '110': 'Barletta-Andria-Trani',
    '111': 'Sud Sardegna',
    '999': 'Sconosciuto (Unknown)'
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
    '01': 'Gennaio-Marzo',
    '02': 'Aprile-Giugno',
    '03': 'Luglio-Settembre',
    '04': 'Ottobre-Dicembre'
}


