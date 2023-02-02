def compute_daily_max_difference(time_series):
    final_list = [] # lista finale in cui salverò le escursioni termiche
    counter = 0 # contatore per le righe della time_series
    if not clean_list(time_series):
        return
    while counter < len(time_series): # itero finché non arrivo alla fine della lista 
        tmp_list = [] # lista temporanea per le temperature di un singolo giorno
        current_day = convert_day(time_series[counter][0]) # converto l'epoch di inizio al solo giorno 
        tmp_list.append(time_series[counter][1]) # aggiungo la temperatura associata 
        for i in range(counter + 1, len(time_series)): # itero sui successivi
            day = convert_day(time_series[i][0]) # converto ogni epoch a giorno
            if day == current_day: # controllo se il giorno è lo stesso
                tmp_list.append(time_series[i][1]) # aggiungo la temperatura associata alla lista temporanea
            else: # se non sto più lavorando sullo stesso giorno
                break # esco dal for interno
        counter += len(tmp_list) + 1 # salto le righe che appartenevano allo stesso giorno e ricomincio dalla successiva
        if len(tmp_list) > 1: # se avevo più di una misurazione per un dato giorno
            final_list.append(max(tmp_list)-min(tmp_list)) # aggiungo la differenza massima
        else: 
            final_list.append(None) # altrimenti aggiungo None
    return final_list