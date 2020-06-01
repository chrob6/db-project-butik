
DROP SCHEMA IF EXISTS butik;
CREATE SCHEMA butik COLLATE = utf8_general_ci;
USE butik;

CREATE TABLE Pracownik (
  ID_Pracownika INT (11) UNSIGNED NOT NULL,
  Imie varchar(50),
  Nazwisko varchar(50),
  Stanowisko varchar(50),
  Pensja INT(10),
  PRIMARY KEY (ID_Pracownika)
);

CREATE TABLE Staly_Klient (
    ID_Staly_Klient INT (11) UNSIGNED NOT NULL,
    Imie varchar(50),
    Nazwisko varchar(50),
    Nr_Tel INT(9),
    Znizka_procent INT(2),
    PRIMARY KEY (ID_Staly_Klient)
);

CREATE TABLE Sprzedaz (
    ID_Sprzedaz INT (11) UNSIGNED NOT NULL,
    Data date,
    ID_Pracownika INT(11) UNSIGNED NOT NULL,
    ID_Staly_Klient INT(11) UNSIGNED NOT NULL,
    PRIMARY KEY (ID_Sprzedaz)
);

CREATE TABLE Rachunek (
  ID_Towar INT(11) UNSIGNED NOT NULL,
  ID_Sprzedaz INT(11) UNSIGNED NOT NULL
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

CREATE TABLE Magazyn (
		ID_Magazyn INT (11) UNSIGNED NOT NULL,
		Nr_Regalu INT (11),
		Nr_Polki INT (11),
		Nr_Magazynu INT (11),
		PRIMARY KEY (ID_Magazyn)
);

CREATE TABLE Marka (
		ID_Marka INT (11) UNSIGNED NOT NULL,
		Nazwa VARCHAR (25) NOT NULL,
		Kraj_produkcji VARCHAR (25),
		Marza_procent INT (11),
		PRIMARY KEY (ID_Marka)
);

INSERT INTO Pracownik
VALUES (
        1,
        'Adam',
        'Matczak',
        'Menadzer',
        7600
       );

INSERT INTO Pracownik
VALUES (
        2,
        'Zbigniew',
        'Korwinowski',
        'Doradca klienta',
        4500
       );

INSERT INTO Pracownik
VALUES (
        3,
        'Magdalena',
        'Kawa',
        'Kasjer',
        3100
       );

INSERT INTO Pracownik
VALUES (
        4,
        'Antoni',
        'Piotrkowski',
        'Kasjer',
        3000
       );

INSERT INTO Pracownik
VALUES (
        5,
        'Daria',
        'Matura',
        'Kasjer',
        2900
       );

COMMIT;

INSERT INTO Pracownik
VALUES (
        6,
        'Antoni',
        'Kawa',
        'Sprzataczka',
        3000
       );

INSERT INTO Staly_Klient
VALUES (
        1,
        'Barbara',
        'Nowak',
        345323452,
        2
       );

INSERT INTO Staly_Klient
VALUES (
        2,
        'Ryszard',
        'Góra',
        564246736,
        3
       );

INSERT INTO Staly_Klient
VALUES (
        3,
        'Marcin',
        'Noworodek',
        123546435,
        0
       );

INSERT INTO Staly_Klient
VALUES (
        4,
        'Zofia',
        'Szlachta',
        567432345,
        10
       );

INSERT INTO Staly_Klient
VALUES (
        5,
        'Marian',
        'Adamczyk',
        532346745,
        7
       );

INSERT INTO Staly_Klient
VALUES (
        6,
        'Adam',
        'Kijowski',
        754256445,
        11
       );

INSERT INTO Staly_Klient
VALUES (
        7,
        'Robert',
        'Santiago',
        577542566,
        3
       );

INSERT INTO Staly_Klient
VALUES (
        8,
        'Andrew',
        'Smith',
        876445432,
        6
       );
COMMIT;

INSERT INTO Sprzedaz VALUES (1,'2019-01-11', 1,1 );
INSERT INTO Sprzedaz VALUES (2,'2020-11-03', 1,1 );
INSERT INTO Sprzedaz VALUES (3,'2019-04-30', 3,3 );
INSERT INTO Sprzedaz VALUES (4,'2020-12-21', 4,3 );
INSERT INTO Sprzedaz VALUES (5,'2020-03-25', 4,2 );
INSERT INTO Sprzedaz VALUES (6,'2019-02-29', 4,1 );
INSERT INTO Sprzedaz VALUES (7,'2020-03-15', 5,5 );
INSERT INTO Sprzedaz VALUES (8,'2020-07-03', 3,6 );
INSERT INTO Sprzedaz VALUES (9,'2020-03-01', 4,8 );
INSERT INTO Sprzedaz VALUES (10,'2019-11-02', 5,5 );
INSERT INTO Sprzedaz VALUES (11,'2020-03-25', 4,4 );
INSERT INTO Sprzedaz VALUES (12,'2019-03-10', 4,4 );
INSERT INTO Sprzedaz VALUES (13,'2020-11-05', 3,5 );
INSERT INTO Sprzedaz VALUES (14,'2020-12-23', 2,2 );
INSERT INTO Sprzedaz VALUES (15,'2020-02-20', 2,3 );
/*INSERT INTO Sprzedaz VALUES (16,'2019-09-02', 3,7 );
INSERT INTO Sprzedaz VALUES (17,'2020-08-03', 4,6 );
INSERT INTO Sprzedaz VALUES (18,'2020-06-21', 4,1 );
INSERT INTO Sprzedaz VALUES (19,'2020-02-22', 3,1 );
INSERT INTO Sprzedaz VALUES (20,'2019-02-28', 2,7 );
INSERT INTO Sprzedaz VALUES (21,'2020-01-30', 5,1 );
INSERT INTO Sprzedaz VALUES (22,'2019-01-18', 5,5 );
INSERT INTO Sprzedaz VALUES (23,'2020-02-17', 5,4 );
INSERT INTO Sprzedaz VALUES (24,'2019-07-30', 4,3 );
INSERT INTO Sprzedaz VALUES (25,'2020-06-21', 3,2 );
INSERT INTO Sprzedaz VALUES (26,'2019-05-12', 2,4 );
INSERT INTO Sprzedaz VALUES (27,'2020-12-12', 1,3 );
INSERT INTO Sprzedaz VALUES (28,'2020-01-09', 4,5 );
INSERT INTO Sprzedaz VALUES (29,'2019-02-01', 3,6 );
INSERT INTO Sprzedaz VALUES (30,'2019-03-06', 2,2 );*/
COMMIT;

INSERT INTO Magazyn
VALUES (
	0,
	0,
	0,
	0
	);

INSERT INTO Magazyn
VALUES (
	1,
	1,
	1,
	1
	);

INSERT INTO Magazyn
VALUES (
	2,
	1,
	2,
	1
	);


INSERT INTO Magazyn
VALUES (
	3,
	1,
	4,
	1
	);

INSERT INTO Magazyn
VALUES (
	4,
	2,
	1,
	1
	);

INSERT INTO Magazyn
VALUES (
	5,
	2,
	2,
	1
	);

INSERT INTO Magazyn
VALUES (
	6,
	2,
	3,
	1
	);

INSERT INTO Magazyn
VALUES (
	7,
	1,
	1,
	2
	);

INSERT INTO Magazyn
VALUES (
	8,
	1,
	2,
	2
	);

INSERT INTO Magazyn
VALUES (
	9,
	1,
	3,
	2
	);

INSERT INTO Magazyn
VALUES (
	10,
	1,
	4,
	2
	);

INSERT INTO Magazyn
VALUES (
	11,
	1,
	5,
	2
	);

INSERT INTO Magazyn
VALUES (
	12,
	1,
	1,
	3
	);

INSERT INTO Magazyn
VALUES (
	13,
	1,
	2,
	3
	);

INSERT INTO Magazyn
VALUES (
	14,
	1,
	3,
	3
	);

COMMIT;

INSERT INTO Marka
VALUES (
	1,
	'Gucci',
	'Wlochy',
	10
	);

INSERT INTO Marka
VALUES (
	2,
	'Louis Vuitton',
	'Francja',
	15
	);

INSERT INTO Marka
VALUES (
	3,
	'Hugo Boss',
	'Niemcy',
	9
	);

INSERT INTO Marka
VALUES (
	4,
	'Chanel',
	'Francja',
	20
	);

INSERT INTO Marka
VALUES (
	5,
	'Fendi',
	'Wlochy',
	15
	);

INSERT INTO Marka
VALUES (
	6,
	'Versace',
	'Wlochy',
	30
	);

INSERT INTO Marka
VALUES (
	7,
	'Prada',
	'Wlochy',
	25
	);

INSERT INTO Marka
VALUES (
	8,
	'Dolce&Gabbana',
	'Wlochy',
	18
	);

COMMIT;

INSERT INTO Towar
VALUES (
	1,
	'KOS0001',
	'Koszula',
	120.95,
	'M',
	1,
	0
	);

INSERT INTO Towar
VALUES (
	2,
	'BUT002',
	'Buty',
	220.95,
	'38',
	6,
	0
	);

INSERT INTO Towar
VALUES (
	3,
	'ODW0003',
	'Odziez Wierzchnia',
	350.95,
	'L',
	8,
	0
	);

INSERT INTO Towar
VALUES (
	4,
	'PER0004',
	'Perfum',
	534.50,
	'NO-SIZE',
	4,
	0
	);

INSERT INTO Towar
VALUES (
	5,
	'KOS0001',
	'Koszula',
	120.95,
	'L',
	1,
	0
	);

INSERT INTO Towar
VALUES (
	6,
	'KOS0001',
	'Koszula',
	120.95,
	'M',
	1,
	0
	);

INSERT INTO Towar
VALUES (
	7,
	'KOS0001',
	'Koszula',
	120.95,
	'M',
	1,
	2
	);

INSERT INTO Towar
VALUES (
	8,
	'KOS0001',
	'Koszula',
	120.95,
	'M',
	1,
	0
	);

INSERT INTO Towar
VALUES (
	9,
	'KOS0001',
	'Koszula',
	120.95,
	'M',
	1,
	2
	);

INSERT INTO Towar
VALUES (
	10,
	'PER0004',
	'Perfum',
	534.50,
	'NO-SIZE',
	4,
	4
	);

INSERT INTO Towar
VALUES (
	11,
	'PER0004',
	'Perfum',
	534.50,
	'NO-SIZE',
	4,
	4
	);

INSERT INTO Towar
VALUES (
	12,
	'PER0004',
	'Perfum',
	534.50,
	'NO-SIZE',
	4,
	0
	);

INSERT INTO Towar
VALUES (
	13,
	'PER0004',
	'Perfum',
	534.50,
	'NO-SIZE',
	4,
	4
	);

INSERT INTO Towar
VALUES (
	14,
	'PER0004',
	'Perfum',
	534.50,
	'NO-SIZE',
	4,
	0
	);

INSERT INTO Towar
VALUES (
	15,
	'SPO0005',
	'Spodnie',
	334.50,
	'NO-SIZE',
	3,
	0
	);

INSERT INTO Towar
VALUES (
	16,
	'SPO0005',
	'Spodnie',
	334.50,
	'NO-SIZE',
	3,
	0
	);

INSERT INTO Towar
VALUES (
	17,
	'SPO0005',
	'Spodnie',
	334.50,
	'NO-SIZE',
	3,
	0
	);

INSERT INTO Towar
VALUES (
	18,
	'SPO0005',
	'Spodnie',
	334.50,
	'NO-SIZE',
	3,
	10
	);

INSERT INTO Towar
VALUES (
	19,
	'ODW0003',
	'Odziez Wierzchnia',
	350.95,
	'L',
	8,
	0
	);

INSERT INTO Towar
VALUES (
	20,
	'ODW0003',
	'Odziez Wierzchnia',
	350.95,
	'L',
	8,
	0
	);

INSERT INTO Towar
VALUES (
	21,
	'BIE0006',
	'Bielizna',
	99.95,
	'XS',
	6,
	0
	);

INSERT INTO Towar
VALUES (
	22,
	'BIE0006',
	'Bielizna',
	99.95,
	'XS',
	6,
	0
	);

INSERT INTO Towar
VALUES (
	23,
	'BIE0006',
	'Bielizna',
	99.95,
	'XS',
	6,
	14
	);

INSERT INTO Towar
VALUES (
	24,
	'BIE0006',
	'Bielizna',
	99.95,
	'XS',
	6,
	0
	);

INSERT INTO Towar
VALUES (
	25,
	'BIE0006',
	'Bielizna',
	99.95,
	'XS',
	6,
	14
	);

INSERT INTO Towar
VALUES (
	26,
	'BLU0006',
	'Bluza',
	400.95,
	'XL',
	7,
	0
	);

INSERT INTO Towar
VALUES (
	27,
	'BLU0006',
	'Bluza',
	400.95,
	'XL',
	7,
	12
	);

INSERT INTO Towar
VALUES (
	28,
	'BLU0006',
	'Bluza',
	400.95,
	'XL',
	7,
	12
	);

INSERT INTO Towar
VALUES (
	29,
	'BLU0006',
	'Bluza',
	400.95,
	'XL',
	7,
	12
	);

INSERT INTO Towar
VALUES (
	30,
	'BLU0006',
	'Bluza',
	400.95,
	'XL',
	7,
	0
	);

INSERT INTO Towar
VALUES (
	31,
	'BLU0006',
	'Bluza',
	400.95,
	'XL',
	7,
	12
	);

INSERT INTO Towar
VALUES (
	32,
	'AKC0007',
	'Inne',
	35.95,
	'NO-SIZE',
	4,
	11
	);

INSERT INTO Towar
VALUES (
	33,
	'AKC0007',
	'Inne',
	35.95,
	'NO-SIZE',
	4,
	11
	);

INSERT INTO Towar
VALUES (
	34,
	'AKC0007',
	'Inne',
	35.95,
	'NO-SIZE',
	4,
	11
	);

INSERT INTO Towar
VALUES (
	35,
	'AKC0007',
	'Inne',
	35.95,
	'NO-SIZE',
	4,
	0
	);

COMMIT;


INSERT INTO Rachunek VALUES (1,1);
INSERT INTO Rachunek VALUES (2,1);
INSERT INTO Rachunek VALUES (3,2);
INSERT INTO Rachunek VALUES (4,3);
INSERT INTO Rachunek VALUES (5,4);
INSERT INTO Rachunek VALUES (6,5);
INSERT INTO Rachunek VALUES (8,6);
INSERT INTO Rachunek VALUES (12,6);
INSERT INTO Rachunek VALUES (14,6);
INSERT INTO Rachunek VALUES (15,6);
INSERT INTO Rachunek VALUES (16,7);
INSERT INTO Rachunek VALUES (17,8);
INSERT INTO Rachunek VALUES (19,9);
INSERT INTO Rachunek VALUES (20,10);
INSERT INTO Rachunek VALUES (21,11);
INSERT INTO Rachunek VALUES (22,12);
INSERT INTO Rachunek VALUES (24,13);
INSERT INTO Rachunek VALUES (26,14);
INSERT INTO Rachunek VALUES (30,15);
INSERT INTO Rachunek VALUES (35,15);

ALTER  TABLE Sprzedaz ADD FOREIGN KEY (ID_Pracownika) REFERENCES
Pracownik(ID_Pracownika);
ALTER  TABLE Sprzedaz ADD FOREIGN KEY (ID_Staly_Klient) REFERENCES
Staly_Klient(ID_Staly_Klient);
ALTER TABLE  Rachunek ADD FOREIGN KEY (ID_Towar) REFERENCES
Towar(ID_Towar);
ALTER TABLE  Rachunek ADD FOREIGN KEY (ID_Sprzedaz) REFERENCES
Sprzedaz(ID_Sprzedaz);
ALTER TABLE Towar ADD FOREIGN KEY (ID_Magazyn) REFERENCES
Magazyn(ID_Magazyn);
ALTER TABLE Towar ADD FOREIGN KEY (ID_Marka) REFERENCES
MARKA(ID_Marka);

CREATE USER 'butik'@'localhost' IDENTIFIED BY 'butik';
GRANT ALL PRIVILEGES ON butik.* TO butik@localhost;
FLUSH PRIVILEGES;

