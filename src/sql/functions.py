import os
import pymysql

from dotenv import load_dotenv
load_dotenv(os.getcwd() + "/../.env")

#Plik z funkcjonalnosciami, nad kazda funkcja jest numer funkcjonalnosci jaka realizuje

#połaczenie sie z baza
def connect():
    connection = pymysql.Connect(
        host='localhost',
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

#2ab
def client_history(id):
    print("Wszystkie kupione przedmioty przez klienta nr " + str(id))
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = " SELECT k.ID_Staly_Klient, t.typ, t.cena, m.Nazwa FROM  staly_klient as k \
                    LEFT JOIN sprzedaz as s ON k.ID_Staly_Klient = s.ID_Staly_Klient \
                    LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz \
                    LEFT JOIN towar t on r.ID_Towar = t.ID_Towar \
                    LEFT JOIN marka m on t.ID_Marka = m.ID_Marka \
                    WHERE k.ID_Staly_Klient = %s"
            sql2 = "SELECT SUM(t.cena) FROM  staly_klient as k \
                    LEFT JOIN sprzedaz as s ON k.ID_Staly_Klient = s.ID_Staly_Klient \
                    LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz \
                    LEFT JOIN towar t on r.ID_Towar = t.ID_Towar \
                    LEFT JOIN marka m on t.ID_Marka = m.ID_Marka \
                    WHERE k.ID_Staly_Klient = %s"
            cursor.execute(sql, id)
            rows = cursor.fetchall()
            for row in rows:
                print(row["typ"],row["cena"],row["Nazwa"])
            cursor.execute(sql2, id)
            res = cursor.fetchone()
            print("Suma wydanych pieniędzy: " + str(res['SUM(t.cena)']) + " zł")
    finally:
        connection.close()
#9.
def access_shop():
    print("Produkty dostępne w sklepie: ")
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = " SELECT Kod_modelu, Typ, Cena, Rozmiar FROM Towar t \
                    INNER JOIN Magazyn m ON t.ID_Magazyn = m.ID_Magazyn \
                    WHERE m.Nr_Magazynu = 1 "
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row["Kod_modelu"], row["Typ"], row["Cena"])
    finally:
        connection.close()

#8.
def count_by_size(size):
    print("Produkty o rozmiarze "+size+": ")
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = ("SELECT Kod_modelu, Cena, count(Kod_modelu) Ilosc, Rozmiar \
                    FROM Towar WHERE Rozmiar like '%s' AND ID_Magazyn != 0 \
                    GROUP BY Kod_modelu ") % (size)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row["Kod_modelu"], row["Cena"], row["Ilosc"])
    finally:
        connection.close()

#10a.
def search_prod(nr_r, nr_p, nr_m):
    print("Produkt na podanym miejscu to: ")
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = ("SELECT Kod_modelu, Typ, Cena, Rozmiar FROM Towar t  \
                    INNER JOIN Magazyn m ON t.ID_Magazyn = m.ID_Magazyn \
                    WHERE m.Nr_Regalu = %s AND m.Nr_Polki = %s AND m.Nr_Magazynu = %s \
                    GROUP BY Kod_modelu; ") % (nr_r, nr_p, nr_m)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row["Kod_modelu"], row["Typ"], row["Cena"], row["Rozmiar"])
    finally:
        connection.close()

#10b.
def search_mag(kod_m):
    print("Produkt o kodzie "+kod_m+" znajduje sie: ")
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = ("SELECT Nr_Polki, Nr_Regalu, Nr_Magazynu FROM Magazyn m \
                    INNER JOIN Towar t ON m.ID_Magazyn = t.ID_Magazyn \
                    WHERE Kod_modelu LIKE '%s' AND t.ID_Magazyn != 0 \
                    GROUP BY Nr_Magazynu;") % (kod_m)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row["Nr_Polki"], row["Nr_Regalu"], row["Nr_Magazynu"])
    finally:
        connection.close()

#11.
def update_marg(wart,nazwa):
    # print("Produkt o kodzie " + kod_m + " znajduje sie: ")
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql1 = ("SELECT Marza_procent FROM Marka WHERE Nazwa LIKE '%s' ") % (nazwa)
            cursor.execute(sql1)
            rows = cursor.fetchall()
            for row in rows:
                print("Wartosc marzy marki "+nazwa+" to:")
                print(row["Marza_procent"])
            sql2 = ("UPDATE Marka SET Marza_procent = %s WHERE Nazwa LIKE '%s' ") % (wart, nazwa)
            cursor.execute(sql2)
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row["Marza_procent"])
            cursor.execute(sql1)
            rows = cursor.fetchall()
            for row in rows:
                print("Wartosc marzy marki "+nazwa+" po aktualizacji to:")
                print(row["Marza_procent"])
            connection.commit()
    finally:
        connection.close()

#13.
def country(kod_m):
    print("Produkt o kodzie "+kod_m+" został wyprodukowany w ")
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = ("SELECT Kraj_produkcji, m.Nazwa FROM Marka m \
                    INNER JOIN Towar t ON m.ID_Marka = t.ID_Marka WHERE Kod_modelu \
                    LIKE '%s' GROUP BY Kod_modelu,Rozmiar") % (kod_m)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row["Kraj_produkcji"]," przez: ", row["Nazwa"])
    finally:
        connection.close()

#12.
def name(nazwa):
    print("Ilosc produktow marki "+nazwa+" to:")
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = ("SELECT Kod_modelu, Typ, Cena, Rozmiar FROM Towar t \
                    INNER JOIN Marka m ON t.ID_Marka = m.ID_Marka \
                    WHERE m.Nazwa like '%s' GROUP BY Kod_modelu,Rozmiar") % (nazwa)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row["Kod_modelu"], row["Typ"], row["Cena"], row["Rozmiar"])
    finally:
        connection.close()

#1
def increase_discount(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
           how_many_purchase = 2

           sql =( "UPDATE staly_klient as k SET Znizka_procent=Znizka_procent+1 \
                  WHERE (SELECT count(s.ID_Staly_Klient)  FROM sprzedaz as s \
                  WHERE s.ID_Staly_Klient = %s \
                  GROUP BY s.ID_Staly_Klient \
                  HAVING count(s.ID_Staly_Klient)>%s ) AND  ID_Staly_Klient = %s" ) % (id, how_many_purchase, id)
           worked = cursor.execute(sql)
           if worked:
               print("Znizka podniesiona o 1!")
           connection.commit()
    finally:
        connection.close()

#3abc
def employee_rank():
    connection = connect()
    try:
        with connection.cursor() as cursor:

           sql1 = "SELECT p.ID_pracownika,p.Nazwisko,p.Stanowisko, count(s.ID_Pracownika) as il FROM pracownik as p \
                   LEFT JOIN sprzedaz as s ON p.ID_Pracownika = s.ID_Pracownika \
                   GROUP BY  s.ID_Pracownika \
                   ORDER BY  il DESC"
           sql2 = "SELECT p.ID_pracownika,p.Nazwisko,SUM(t.cena) as il FROM  pracownik as p \
                   LEFT JOIN sprzedaz as s ON p.ID_Pracownika = s.ID_Pracownika \
                   LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz \
                   LEFT JOIN towar t on r.ID_Towar = t.ID_Towar \
                   GROUP BY  p.ID_Pracownika \
                   ORDER BY il DESC"
           sql3 = "SELECT p.Nazwisko, t.typ, count(t.typ) as il from pracownik p\
                   LEFT JOIN sprzedaz s on p.ID_Pracownika = s.ID_Pracownika\
                   LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz\
                   LEFT JOIN towar t on r.ID_Towar = t.ID_Towar\
                   GROUP BY t.typ,p.Nazwisko\
                   ORDER BY p.Nazwisko"

           print("Ilosc dokananych sprzedazy: ")
           cursor.execute(sql1)
           rows1 = cursor.fetchall()
           for row in rows1:
               print(row["ID_pracownika"], row["Nazwisko"], row["Stanowisko"], row["il"])
           print()

           print("Utarg: ")
           cursor.execute(sql2)
           rows2 = cursor.fetchall()
           for row in rows2:
               print(row["ID_pracownika"], row["Nazwisko"], row["il"])
           print()

           print("Typ sprzedawanych przedmiotow: ")
           cursor.execute(sql3)
           rows3 = cursor.fetchall()
           for row in rows3:
               print(row["Nazwisko"], row["typ"], row["il"])
    finally:
        connection.close()
#4
def employee_rise(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            salary_raise = int(input("O ile?: "))
            sql = ("UPDATE pracownik SET Pensja=Pensja+%s WHERE ID_Pracownika= %s") % (salary_raise, id)
            cursor.execute(sql)
            connection.commit()

    finally:
        connection.close()
#4
def employee_rise_after_promo(id, connection):
        with connection.cursor() as cursor:
            salary_raise = int(input("O ile?: "))
            sql = ("UPDATE pracownik SET Pensja=Pensja+%s WHERE ID_Pracownika= %s") % (salary_raise, id)
            cursor.execute(sql)
            connection.commit()
#4
def employee_promo(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            promo = str(input("Na jakie stanowisko?: "))
            print(promo)
            if promo == 'exit':
                return

            sql = ("UPDATE pracownik SET Stanowisko='%s' WHERE ID_Pracownika= %s") % (promo,id)
            cursor.execute(sql)
            promo = str(input("Podwyzka? (tak/nie): "))
            if promo == 'tak':
                employee_rise_after_promo(id, connection)

            connection.commit()
    finally:
        connection.close()
#5
def receipt(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            discount_line = 200 #od ilu ma być zniżka

            sql1 = ("SELECT r.ID_Sprzedaz, t.typ, t.cena FROM rachunek r\
                        LEFT JOIN towar t on r.ID_Towar = t.ID_Towar\
                        WHERE ID_Sprzedaz = %s\
                        ORDER BY t.cena DESC") % (id)

            sql2 = ("SELECT r.ID_Sprzedaz, sum(t.cena)  FROM rachunek as r \
                        LEFT JOIN towar t on r.ID_Towar = t.ID_Towar\
                        WHERE ID_Sprzedaz = %s\
                        HAVING  sum(t.cena)  > %s\
                        ORDER BY t.cena DESC;") % (id, discount_line)

            sql3 = ("SELECT r.ID_Sprzedaz, sum(t.cena)*0.9 FROM rachunek as r\
                        LEFT JOIN towar t on r.ID_Towar = t.ID_Towar\
                        WHERE ID_Sprzedaz = %s\
                        ORDER BY t.cena DESC") %(id)

            print("Towary z sprzedazy nr " + str(id))
            cursor.execute(sql1)
            rows = cursor.fetchall()
            for row in rows:
                print(row["ID_Sprzedaz"], row["typ"], row["cena"])

            worked = cursor.execute(sql2)
            if worked:
                cursor.execute(sql3)
                res = cursor.fetchone()
                print("Cena po zniżce: " + str(res['sum(t.cena)*0.9']) + " zł")
    finally:
        connection.close()
#6
def products_from_date(date):
    print(str("Produkty wykupione od " + date))
    connection = connect()
    try:
        with connection.cursor() as cursor:

            sql = ("SELECT  s.Data, kod_modelu, typ, cena, rozmiar from sprzedaz s\
                    LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz\
                    LEFT JOIN towar t on r.ID_Towar = t.ID_Towar\
                    WHERE Data > '%s' ") % (date)

            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row["Data"], row["kod_modelu"], row["typ"],row["cena"],row["rozmiar"])

            connection.commit()
    finally:
        connection.close()

