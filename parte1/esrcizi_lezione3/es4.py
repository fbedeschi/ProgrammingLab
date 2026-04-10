class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    def __init__(self, name):
        # Salva il nome del file
        self.nome = name

    def get_data(self):
        # Controlla che il file sia apribile
        try:
            file = open(self.nome, 'r')
        except:
            raise ExamException('Errore: il file non esiste o non è leggibile')

        dati = []
        timestamp_precedente = None

        for riga in file:
            # Rimuove spazi e newline
            riga = riga.strip()

            # Ignora righe vuote o intestazione
            if not riga or riga.startswith('date'):
                continue

            # Divide la riga in campi
            campi = riga.split(',')

            # Servono almeno due campi (data e passeggeri)
            if len(campi) < 2:
                print(f'Riga ignorata (incompleta): {riga}')
                continue

            data = campi[0].strip()
            valore_grezzo = campi[1].strip()

            # Controlla che la data sia nel formato YYYY-MM
            parti_data = data.split('-')
            if len(parti_data) != 2 or len(parti_data[0]) != 4 or len(parti_data[1]) != 2:
                print(f'Riga ignorata (data non valida): {riga}')
                continue

            # Controlla che il valore dei passeggeri sia un intero positivo
            try:
                num_passeggeri = int(valore_grezzo)
                if num_passeggeri <= 0:
                    raise ValueError
            except ValueError:
                print(f'Riga ignorata (passeggeri non validi): {riga}')
                continue

            # Controlla che la serie sia ordinata e senza duplicati
            if timestamp_precedente is not None:
                if data == timestamp_precedente:
                    file.close()
                    raise ExamException(f'Errore: timestamp duplicato trovato: {data}')
                if data < timestamp_precedente:
                    file.close()
                    raise ExamException(f'Errore: timestamp fuori ordine trovato: {data}')

            timestamp_precedente = data
            dati.append([data, num_passeggeri])

        file.close()
        return dati


def compute_variations(serie_temporale, anno_inizio, anno_fine):
    # Controlla che gli anni siano stringhe
    if not isinstance(anno_inizio, str) or not isinstance(anno_fine, str):
        raise ExamException('Errore: gli anni devono essere stringhe')

    # Raggruppa i passeggeri per anno
    passeggeri_per_anno = {}
    for coppia in serie_temporale:
        anno = coppia[0][:4]  # Estrae YYYY da YYYY-MM
        num_passeggeri = coppia[1]
        if anno not in passeggeri_per_anno:
            passeggeri_per_anno[anno] = []
        passeggeri_per_anno[anno].append(num_passeggeri)

    # Controlla che gli anni richiesti siano presenti nei dati
    if anno_inizio not in passeggeri_per_anno:
        raise ExamException(f'Errore: anno di inizio {anno_inizio} non presente nei dati')
    if anno_fine not in passeggeri_per_anno:
        raise ExamException(f'Errore: anno di fine {anno_fine} non presente nei dati')

    # Genera la lista degli anni nell'intervallo (escludendo quelli senza dati)
    anni_intervallo = []
    for anno in sorted(passeggeri_per_anno.keys()):
        if anno_inizio <= anno <= anno_fine:
            anni_intervallo.append(anno)

    # Calcola la media dei passeggeri per ogni anno nell'intervallo
    media_per_anno = {}
    for anno in anni_intervallo:
        valori = passeggeri_per_anno[anno]
        media_per_anno[anno] = sum(valori) / len(valori)

    # Calcola le variazioni tra anni consecutivi (ignorando anni senza dati)
    variazioni = {}
    anni_validi = list(media_per_anno.keys())
    for i in range(1, len(anni_validi)):
        anno_corrente = anni_validi[i]
        anno_precedente = anni_validi[i - 1]
        chiave = f'{anno_precedente}-{anno_corrente}'
        differenza = media_per_anno[anno_corrente] - media_per_anno[anno_precedente]
        variazioni[chiave] = round(differenza, 1)

    return variazioni


# Test
serie_temporale = CSVTimeSeriesFile(name='data.csv')
dati = serie_temporale.get_data()
variazioni = compute_variations(dati, '1949', '1951')
print(variazioni)