
import src.sql.functions as fun

def menu_product():
    while 1:
        print()
        print("Informacje o towarach:")
        print("1. Produkty dostępne w sklepie")
        print("2. Produkty wykupione od podanej daty")
        print("3. Wyswietlenie kraju produkcji towaru o podanym kodzie")
        print("4. Wyswietlenie ilosci produktów podanej marki")

        choice = input("Wybierz liczbe od 1 do 4 (back-wstecz do poprzedniego menu):")
        if choice == 'back':
            break
        elif choice == '1':
            fun.access_shop()
        elif choice == '2':
            # input?
            date = '2019-12-31'
            fun.products_from_date(date)
        elif choice == '3':
            # input?
            product_code = 'AKC0007'
            fun.country(product_code)
        elif choice == '4':
            # input?
            brand = 'Gucci'
            fun.name(brand)

def menu_employee():
    while 1:
        print()
        print("Informacje o pracownikach:")
        print("1. Ranking pracowników (ilosc sprzedazy, kwota utargu, najczesciej sprzedawany typ produktu):")
        print("2. Awans pracownika (mozliwa podwyzka):")
        print("3. Zmiana pensji dla pracownika")

        choice = input("Wybierz liczbe od 1 do 2 (back-wstecz do poprzedniego menu):")

        if choice == 'back':
            break
        elif choice == '1':
            fun.employee_rank()
        elif choice == '2':
            # input?
            id_employee = 5
            fun.employee_promo(id_employee)
        elif choice == '3':
            # input?
            id_employee = 6
            fun.employee_rise(id_employee)

def menu_client():
    while 1:
        print()
        print("Strefa klienta:")
        print("1. Suma zakupow danego klienta:")
        print("2. Wypisanie produktow z rachunku dla danego id sprzedazy")
        print("3. Zakup produktu")

        choice = input("Wybierz liczbe od 1 do 3 (back-wstecz do poprzedniego menu):")

        if choice == 'back':
            break
        elif choice == '1':
            # input?
            id_client = 1
            fun.client_history(id_client)

        elif choice == '2':
            # input?
            id_sale = 1
            fun.receipt(id_sale)

        elif choice == '3':
            # input? - tu raczej przed ifem albo wartosc z pierwszego?
            id_client = 1
            #fun.buy_product()
            print("bydzie zakup")
            fun.increase_discount(id_client)

def menu_store():
    while 1:
        print()
        print("Magazyn:")
        print("1. Aktualizacja marzy dla podanego producenta:")
        print("2. Jaki produkt jest na podanym miejscu w magazynie:")
        print("3. Jakie jest miejsce w magazynie podanego produktu")
        print("4. Wprowadzenie produktu do bazy")

        choice = input("Wybierz liczbe od 1 do 3 (back-wstecz do poprzedniego menu):")

        if choice == 'back':
            break
        elif choice == '1':
            # input?
            new_marg = 10
            # input?
            producent_name = 'Gucci'
            fun.update_marg(new_marg, producent_name)

        elif choice == '2':
            # input?
            nr_regal = 1
            nr_polka = 1
            nr_magazyn = 1
            fun.search_prod(nr_regal,nr_polka,nr_magazyn)

        elif choice == '3':
            # input?
            product_code = 'AKC0007'
            fun.search_mag(product_code)

        elif choice == '4':
            print("bydzie insert")
            #insert_product():


print("Aplikacja do zarzadzania baza danych butik")
while 1:
    print()
    print("Menu:")
    print("1. Informacje o towarach")
    print("2. Informacje o pracownikach")
    print("3. Strefa klienta")
    print("4. Magazyn")

    choice = input("Wybierz liczbe od 1 do 4 (exit-wyjscie):")
    if choice == 'exit':
        break
    elif choice == '1':
        menu_product()
    elif choice == '2':
        menu_employee()
    elif choice == '3':
        menu_client()
    elif choice == '4':
        menu_store()




#fun.client_history(1)
#fun.receipt(1)
#fun.employee_rank()
#fun.employee_promo(5)
#fun.employee_rise(6)
#fun.increase_discount(1)
#fun.search_prod(1,1,1);
#fun.search_mag()
#fun.access_shop()
#fun.update_marg()
#fun.country()
#fun.name()
#fun.count_by_size("NO-SIZE")

#def buy_product():
#def insert_product():









