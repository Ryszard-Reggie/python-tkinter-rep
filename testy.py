import tkinter
from tkinter.filedialog import askopenfile

window = tkinter.Tk()       # Zainicjowanie okna/wigetu
window.title('Zadanie 2')   # Tytuł okna


# window_width = 800
# window_height = 480
#
# canvas = tkinter.Canvas(window, width=window_width, height=window_height)   # Szerokość i wysokość okna/wigetu
# canvas.grid(columnspan=2)                                                   # Podział okna/wigetu na dwie kolumny

# FUNKCJE: =============================================================================================================

def select_file():
    file = askopenfile()


def insert_data_to_textbox(textbox_name, data):
    """
        Funkja służy do wklejenia danych/tekstu w podane pole tekstowe.

        :param textbox_name:    nazwa zmiennej pola tekstowego
        :param data:            dane wklejane do pola tekstowego
    """
    # textbox_name.delete(0, tkinter.END)
    textbox_name.insert(tkinter.END, data)
    # textbox_name.set(tkinter.END, data)   # `tkinter.Text()` nie ma atr. `set()` | Może `tkinter.Entry()`?


def get_insert_k_value():
    k = insert_k_value_textbox.get()  # Wyciągnięcie wartości
    # messages_output_textbox.delete(0.0, tkinter.END)  # Wyczyszczenie boxa

    try:
        k = int(k)

        # print(f'Podana wartość k = {k} jest liczba całkowitą (int).')
        # messages_output_textbox.insert(tkinter.END, f'Podana wartość k = {k} jest liczba całkowitą (int).\n')

        if k <= 0:
            print(f'k nie może być mniejsze równe 0.')
            # messages_output_textbox.insert(tkinter.END, f'k nie może być mniejsze równe 0.\n')
            insert_data_to_textbox(messages_output_textbox, f'k nie może być mniejsze równe 0.\n')
        elif k % 2 == 0:
            print(f'k powinno być liczbą całkowita nieparzystą.')
            # messages_output_textbox.insert(tkinter.END, f'k powinno być liczbą całkowita nieparzystą.\n')
            insert_data_to_textbox(messages_output_textbox, f'k powinno być liczbą całkowita nieparzystą.\n')
        else:
            print(f'Podana wartość k = {k} jest liczbą nieparzystą całkowitą większą nierówną 0.')
            # messages_output_textbox.insert(tkinter.END, f'Podana wartość k = {k} jest liczbą nieparzystą całkowitą większą nierówną 0.\n')
            insert_data_to_textbox(messages_output_textbox, f'Podana wartość k = {k} jest liczbą nieparzystą całkowitą większą nierówną 0.\n')
            return k
    except:
        print(f'Podana wartość k = {k} nie jest liczbą całkowitą (int).')
        # messages_output_textbox.insert(tkinter.END, f'Podana wartość k = {k} nie jest liczbą całkowitą (int).\n')
        insert_data_to_textbox(messages_output_textbox, f'Podana wartość k = {k} nie jest liczbą całkowitą (int).\n')


# ETYKIETY: ============================================================================================================

path_labelframe = tkinter.LabelFrame(window, text='Ścieżka:')
path_labelframe.grid(row=0, column=0, padx=2, pady=2)

data_labelframe = tkinter.LabelFrame(window, text='Dane:')
data_labelframe.grid(row=1, column=0, padx=2, pady=2)

knn_variant_labelframe = tkinter.LabelFrame(window, text='Wariant:')
knn_variant_labelframe.grid(row=3, column=0, padx=2, pady=2)

method_labelframe = tkinter.LabelFrame(window, text='Metoda:')
method_labelframe.grid(row=4, column=0, padx=2, pady=2)

insert_k_value_labelframe = tkinter.LabelFrame(window, text='Podaj k:')
insert_k_value_labelframe.grid(row=5, column=0, padx=2, pady=2)

sample_number_labelframe = tkinter.LabelFrame(window, text='Podja numer próbki:')
sample_number_labelframe.grid(row=6, column=0, padx=2, pady=2)

knn_variant_one_result_labelframe = tkinter.LabelFrame(window, text='Wynik wariantu 1:')
knn_variant_one_result_labelframe.grid(row=7, column=0, padx=2, pady=2)

knn_variant_two_result_labelframe = tkinter.LabelFrame(window, text='Wynik wariantu 2:')
knn_variant_two_result_labelframe.grid(row=8, column=0, padx=2, pady=2)

covering_labelframe = tkinter.LabelFrame(window, text='Pokrycie:')
covering_labelframe.grid(row=9, column=0, padx=2, pady=2)

effectiveness_labelframe = tkinter.LabelFrame(window, text='Skuteczność:')
effectiveness_labelframe.grid(row=10, column=0, padx=2, pady=2)

messages_output_labelframe = tkinter.LabelFrame(window, text='Komunikaty:')
messages_output_labelframe.grid(row=11, column=0, padx=2, pady=2)

# ELEMENTY INTERAKTYWNE: ===============================================================================================
# PRZYCISK WYBORU PLIKU: -----------------------------------------------------------------------------------------------

file_select_button = tkinter.Button(path_labelframe, text='...', command=select_file)  # Okno dialogowe wyboru pliku
file_select_button.grid(row=0, column=3, padx=4, pady=4)

# POLE TEKSTOWE ŚCIEŻKI DO PLIKU: --------------------------------------------------------------------------------------

path_display_textbox = tkinter.Text(path_labelframe, width=64, height=1)
path_display_textbox.grid(row=0, column=1, padx=2, pady=2)

# POLE TEKSTOWE DANYCH: ------------------------------------------------------------------------------------------------

data_display_textbox = tkinter.Text(data_labelframe, width=64, height=16)
data_display_textbox.grid(row=2, padx=2, pady=2)

# POLE WYBORU WARIANTU knn: --------------------------------------------------------------------------------------------

# POLE WYBORU METODY: --------------------------------------------------------------------------------------------------

# POLE TEKSTOWE WARTOŚCI k: --------------------------------------------------------------------------------------------

insert_k_value_textbox = tkinter.Entry(insert_k_value_labelframe, text='Podaj k:')
insert_k_value_textbox.grid(row=5, column=1, padx=2, pady=2)

insert_k_value_button = tkinter.Button(insert_k_value_labelframe, text='Zatwierdź', command=get_insert_k_value)
insert_k_value_button.grid(row=5, column=3, padx=2, pady=2)

# POLE WYBORU PRÓBKI: --------------------------------------------------------------------------------------------------

sample_number_textbox = tkinter.Text(sample_number_labelframe, width=32, height=1)
sample_number_textbox.grid(row=6, column=1, padx=2, pady=2)

# POLE TEKSTOWE WYNIKU WARIANTU 1: -------------------------------------------------------------------------------------

knn_variant_one_result_textbox = tkinter.Text(knn_variant_one_result_labelframe, width=32, height=1)
knn_variant_one_result_textbox.grid(row=7, column=1, padx=2, pady=2)

# POLE TEKSTOWE WYNIKU WARIANTU 2: -------------------------------------------------------------------------------------

knn_variant_two_result_textbox = tkinter.Text(knn_variant_two_result_labelframe, width=32, height=1)
knn_variant_two_result_textbox.grid(row=8, column=1, padx=2, pady=2)

# POLE TEKSTOWE POKRYCIA: ----------------------------------------------------------------------------------------------

covering_textbox = tkinter.Text(covering_labelframe, width=32, height=1)
covering_textbox.grid(row=9, column=1, padx=2, pady=2)

# POLE TEKSTOWE SKUTECZNOŚCI: ------------------------------------------------------------------------------------------

effectiveness_textbox = tkinter.Text(effectiveness_labelframe, width=32, height=1)
effectiveness_textbox.grid(row=10, column=1, padx=2, pady=2)

# POLE TEKSTOWE KOMUNIKATÓW KONTROLNYCH: -------------------------------------------------------------------------------

messages_output_textbox = tkinter.Text(messages_output_labelframe, height=3, wrap=tkinter.WORD)
messages_output_textbox.grid(row=11, column=1, padx=4, pady=4, ipadx=4, ipady=4)

# PĘTLA UTRZYMUJĄCA PROGRAM: ===========================================================================================

window.mainloop()
