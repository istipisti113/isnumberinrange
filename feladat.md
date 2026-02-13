FELADAT_LEIRAS_A_Number_Range.md
Oldal:1/

# Feladat: Szám tartomány ellenőrzése
```Number_Range```

## Feladat leírása

Írj egy Python BDD tesztet, amely ellenőrzi, hogy egy szám egy adott tartományban van-e (minimum és maximum érték között)!

### Követelmények

1. **Feature fájl létrehozása**: Hozz létre egy `number_range.feature` fájlt a `features/` mappában
2. **Scenáriók írása**: Írj legalább 7 scenáriót:
    - **Szám a tartományon belül** (pl. 50, min=0, max=100) → Visszaadja: `True`
    - **Szám a tartomány alatt** (pl. -5, min=0, max=100) → Visszaadja: `False`
    - **Szám a tartomány felett** (pl. 150, min=0, max=100) → Visszaadja: `False`
    - **Szám a minimum határon** (pl. 0, min=0, max=100) → Visszaadja: `True` (inkluzív határok)
    - **Szám a maximum határon** (pl. 100, min=0, max=100) → Visszaadja: `True` (inkluzív határok)

    - Adj hozzá scenáriót tizedes számokra is (pl. 3.5, -2.7)
    - Adj hozzá scenáriót negatív tartományokra is (pl. -100 és -50 között)
3. **Step definitions**: Írd meg a step definition-öket a `features/steps/step_definitions.py` fájlban
4. **Alkalmazás kód**: Implementáld az `src/number_range.py` fájlban a `is_in_range(number, min_value, max_value)` függvényt


### Példa scenárió struktúra

```gherkin
Feature: Szám tartomány ellenőrzése
  Mint felhasználó
  Szeretném ellenőrizni, hogy egy szám egy adott tartományban van-e
  Hogy validációt végezhessek

  Scenario: Szám a tartományon belül
    Given a szám értéke 50
    And a minimum érték 0
    And a maximum érték 100
    When ellenőrzöm, hogy a szám a tartományban van-e
    Then az eredmény True kell legyen
```

Természetesen te angol nyelven fogalmazz! 🇬🇧🫖💂🏻‍♂️👑

### Lépések

1. **Első lépés - Feature fájl**: Írd meg a feature fájlt a scenáriókkal
2. **Második lépés - Step definitions**: Írd meg a step definition-öket (először üresen, vagy csak pass-szel)
3. **Harmadik lépés - Futtatás**: Futtasd le a teszteket (`behave`), és nézd meg, hogy milyen step-ek hiányoznak
4. **Negyedik lépés - Implementáció**: Implementáld a hiányzó step-eket és az alkalmazás kódot
5. **Ötödik lépés - Tesztelés**: Futtasd újra a teszteket, és ellenőrizd, hogy minden átmegy

### Tippek

- Ne feledd: először a tesztet írjuk, utána az alkalmazás kódot (TDD/BDD módszer)
- A step definition-ökben használhatod a `context` objektumot az adatok tárolására
- Az alkalmazás kódot a `src/number_range.py` fájlba írd
- Figyelj a határelőzményekre: a tartomány inkluzív (a minimum és maximum értékek is benne vannak)

### Bónusz feladatok

- Használj Scenario Outline-ot az Examples táblázattal különböző tartományokkal
- Implementáld az opcionális `inclusive` paramétert, ami meghatározza, hogy a határok inkluzívek-e vagy exkluzívek


## Projekt struktúra

A feladatnak így kell kinéznie:

```
Python_Number_Range/
├── FELADAT_LEIRAS.md              # Ez a fájl
├── features/
│   ├── number_range.feature
│   └── steps/
│       └── step_definitions.py
└── src/
    └── number_range.py            # Alkalmazás kód
```

## Futtatás

A tesztek futtatásához a gyökérkönyvtárból futtasd:

```bash
python -m behave
```

FELADAT_LEIRAS_A_Number_Range.md megjelenítése.