
## Projekt bazy danych
Temat projektu: Butik

Projekt realizuje baze danych małego sklepu odzieżowego - butiku.
W bazie znajduje się 7 encji :
- Pracownik
- Staly Klient
- Sprzedaż
- Rachunek
- Towar
- Marka
- Magazyn

Encje są połączone ze sobą odpowiednimi relacjami, dzięki czemu można łączyć różne zapytania, stosować rozbudowane funkcjonalności. 

Diagram Bazy Danych:

![Butik](Butik.svg)


Tworzenie niektorych tabel: 
```sql
CREATE TABLE Pracownik (
  ID_Pracownika INT (11) UNSIGNED NOT NULL,
  Imie varchar(50),
  Nazwisko varchar(50),
  Stanowisko varchar(50),
  Pensja INT(10),
  PRIMARY KEY (ID_Pracownika)
);

CREATE TABLE Towar (
  ID_Towar INT (11) UNSIGNED NOT NULL,
  Kod_modelu VARCHAR (25) NOT NULL,
  Typ ENUM('Buty','Spodnie','Koszula','Bielizna','Bluza','Perfum','Bluzka','Inne','Odziez Wierzchnia'),
  Cena DECIMAL(6,2) NOT NULL,
  Rozmiar VARCHAR (10),
  ID_Marka INT (11) UNSIGNED NOT NULL,
  ID_Magazyn INT (11) UNSIGNED NOT NULL,
  PRIMARY KEY (ID_Towar)
);
```
Dodanie niektórych relacji:
```sql
ALTER TABLE  Rachunek ADD FOREIGN KEY (ID_Towar) REFERENCES
Towar(ID_Towar);
ALTER TABLE  Rachunek ADD FOREIGN KEY (ID_Sprzedaz) REFERENCES
Sprzedaz(ID_Sprzedaz);
ALTER TABLE Towar ADD FOREIGN KEY (ID_Magazyn) REFERENCES
Magazyn(ID_Magazyn);
```
Wszystkie polecenia wykorzystane do stworzenia bazy danych są zawarte w pliku butik_schema.sql


## Implementacja zapytań SQL
<!--Tutaj należy wylistować wszystkie funkcjonalności, wraz z odpowiednimi zapytaniami SQL. W tej sekcji należy zawrzeć wyłącznie zapytania z grupy DML oraz DQL.-->
Funkcjonalności:

1.Po odpowiedniej ilości zakupów stały klient o danym id otrzymuje większą zniżkę na kolejne zakupy.  
Operacja wykonywana po dokonaniu zakupu przez klienta.
```sql
UPDATE staly_klient as k SET Znizka_procent=Znizka_procent+1
WHERE (SELECT count(s.ID_Staly_Klient)  FROM sprzedaz as s
        WHERE s.ID_Staly_Klient = 1
        GROUP BY s.ID_Staly_Klient
        HAVING count(s.ID_Staly_Klient)>2 ) AND  ID_Staly_Klient = 1;
```

2.a) Wyświetlenie wszystkich zakupów klienta o danych id.  
    b) Wyświetlenie ile klient o danym numerze id wydał w sklepie.  
    
a)
```sql
SELECT k.ID_Staly_Klient, t.typ, t.cena, m.Nazwa FROM  staly_klient as k
LEFT JOIN sprzedaz as s ON k.ID_Staly_Klient = s.ID_Staly_Klient
LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
LEFT JOIN marka m on t.ID_Marka = m.ID_Marka
WHERE k.ID_Staly_Klient = 1;
```
b)
```sql
SELECT k.ID_Staly_Klient, t.typ, t.cena, m.Nazwa FROM  staly_klient as k
LEFT JOIN sprzedaz as s ON k.ID_Staly_Klient = s.ID_Staly_Klient
LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
LEFT JOIN marka m on t.ID_Marka = m.ID_Marka
WHERE k.ID_Staly_Klient = 1;
```
3.Ranking pracowników.  
    a) pod względem ilości dokonanych sprzedaży.  
    b) pod względem utargu.   
    c) najczęściej sprzedawane typy towarów przez danych pracowników.
    

a)
```sql
SELECT p.ID_pracownika,p.Nazwisko,p.Stanowisko, count(s.ID_Pracownika) as il FROM pracownik as p
LEFT JOIN sprzedaz as s ON p.ID_Pracownika = s.ID_Pracownika
GROUP BY  s.ID_Pracownika
ORDER BY  il DESC;
```
b)
```sql
SELECT p.ID_pracownika,p.Nazwisko,SUM(t.cena) as il FROM  pracownik as p
LEFT JOIN sprzedaz as s ON p.ID_Pracownika = s.ID_Pracownika
LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
GROUP BY  p.ID_Pracownika
ORDER BY il DESC;
```
c)
```sql
SELECT p.Nazwisko, t.typ, count(t.typ) from pracownik p
LEFT JOIN sprzedaz s on p.ID_Pracownika = s.ID_Pracownika
LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
GROUP BY t.typ,p.Nazwisko
ORDER BY p.Nazwisko;
```

4.Awans/podwyżka dla pracownika
```sql
UPDATE pracownik SET Stanowisko='Kasjer' WHERE ID_Pracownika=4;
UPDATE pracownik SET Pensja=Pensja+200 WHERE ID_Pracownika=4;
```


5.Pokazanie towarów na rachunku. Jeżeli cena przekracza 200zł - 10%zniżki.  
    (trzeci SELECT wykonuje się tylko wtedy kiedy drugi zwróci jakąś wartość)
```sql
SELECT r.ID_Sprzedaz, t.typ, t.cena FROM rachunek r
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
WHERE ID_Sprzedaz = 1
ORDER BY t.cena DESC;

SELECT r.ID_Sprzedaz, sum(t.cena)  FROM rachunek as r
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
WHERE ID_Sprzedaz = 1
HAVING  sum(t.cena)  > 200
ORDER BY t.cena DESC;

SELECT r.ID_Sprzedaz, sum(t.cena)*0.9 FROM rachunek as r
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
WHERE ID_Sprzedaz = 1
ORDER BY t.cena DESC;
```

6.Wyświetlenie produktów sprzedanych od danej daty. (np. tylko w 2020 roku)
```sql
SELECT  s.Data, kod_modelu, typ, cena, rozmiar from sprzedaz s
LEFT JOIN rachunek r on s.ID_Sprzedaz = r.ID_Sprzedaz
LEFT JOIN towar t on r.ID_Towar = t.ID_Towar
WHERE Data > '2019-12-31';
```

7.Wyświetlenie i posortowanie produktów. (np. po cenie)
```sql
SELECT Kod_modelu, Typ, Cena, Rozmiar FROM Towar WHERE ID_Magazyn !=0  ORDER BY Cena;
```

8.Zliczanie produktów (np. o danym rozmiarze)
```sql
SELECT Kod_modelu,Cena,count(Kod_modelu) 
FROM Towar WHERE Rozmiar like "M" AND ID_Magazyn !=0 GROUP BY Kod_modelu;
```

9.Wyświetlenie wszystkich towarów dostepnych na sklepie.
```sql
SELECT Kod_modelu, Typ, Cena, Rozmiar FROM Towar t 
INNER JOIN Magazyn m ON t.ID_Magazyn = m.ID_Magazyn WHERE m.Nr_Magazynu =1;
```

10.a)Wyszukanie co znajduje się na danym miejscu w magazynie.
```sql
SELECT Kod_modelu, Typ, Cena, Rozmiar FROM Towar t 
INNER JOIN Magazyn m ON t.ID_Magazyn = m.ID_Magazyn 
WHERE m.Nr_Regalu = 1 AND m.Nr_Polki = 4 AND m.Nr_Magazynu =2 GROUP BY Kod_modelu;
```
b)Gdzie znajduje się konkretny towar.
```sql
SELECT Nr_Polki, Nr_Regalu, Nr_Magazynu FROM Magazyn m 
INNER JOIN Towar t ON m.ID_Magazyn = t.ID_Magazyn 
WHERE Kod_modelu like "BLU0006" GROUP BY Nr_Magazynu;
```

<!--10.W jakim magazynie znajduje się najwięcej towaru.
```sql
SELECT Nr_Magazynu, count(kod_modelu) FROM Towar t 
INNER JOIN Magazyn m ON t.ID_Magazyn = m.ID_Magazyn GROUP BY Nr_Magazynu;
```-->

11.Aktualizacja marży konkretnej marki.
```sql
UPDATE Marka SET Marza_procent=8 WHERE Nazwa LIKE "Gucci";
```

12.Zliczenie ilości produktów danej marki.
```sql
SELECT Kod_modelu, Typ, Cena, Rozmiar FROM Towar t 
INNER JOIN Marka m ON t.ID_Marka = m.ID_Marka 
WHERE m.Nazwa like "Gucci" GROUP BY Kod_modelu,Rozmiar;
```

13.Wyświetlenie kraju produkcji konkretnego towaru.
```sql
SELECT Kod_modelu, Rozmiar, Cena, Kraj_produkcji FROMMarka m 
INNER JOIN Towar t ON m.ID_Marka = t.ID_Marka 
WHERE Kod_modelu LIKE "KOS0001" GROUP BY Kod_modelu,Rozmiar;
```

## Aplikacja
Tutaj należy opisać aplikację, która wykorzystuje zapytania SQL z poprzedniego kroku. Można, jednak nie jest to konieczne, wrzucić tutaj istotne snippety z Waszych aplikacji.

## Dodatkowe uwagi
W tej sekcji możecie zawrzeć informacje, których nie jesteście w stanie przypisać do pozostałych. Mogą to być również jakieś komentarze, wolne uwagi, itp.  
Magazyn 1 - Sklep  
Magazyn 0 (wszystkie wartości zero) - towar już kupiony 
