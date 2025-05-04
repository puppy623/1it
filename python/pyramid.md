# Pyramida porozumění základů programování

V jakém jste patře? Co jsem schopni udělat bez jakékoliv nápovědy sami? Vyzkoušejte si.

| autor          | datum   |
| -------------- | ------- |
| Michal Bubílek | 03/2025 |

Tento materiál je stále WIP (Work In Progress).

## 1. patro

Jedná se o naprosté základy. Umím použít VS Code a napsat a spustit jednořádkový script. Do tohoto skillu patří i základní práce s počítačem, nainstalování interpreta programovacího jazyka a nastavení IDE.

Zadání:

1. Výpis textového řetězce "Hello world" do textové konzole.

## 2. patro

Zde je základní práce s proměnnými a základní aritmetické operace.

Zadání:

1. Napište program, ve kterém si na začátku vytvoříte dvě proměnné `m` a `h`. `m` je pro hmotnost v kg a `h` je pro výšku v cm. Váš program spočítá vaše BMI a vypíše jeho hodnotu.
1. Napište program, který bude umět spočítat kolik je `x` procent z nějaké hodnoty `n`.
1. Napište program, kderý ze zadaného poloměru kružnice `r`, vypočte její obvod a obsah.
1. Napište program, který spočítá o kolik se zvednou dvě 1km koleje, pokud se každá prodlouží o 1 mm? Koleje jsou na svých koncích upevněny a je vyloučen pohyb do strany. Při jejich zvětšení je umožněn tedy jen pohyb vzhůru.
1. Napište program, který spočítá a vypíše vzdálenost dvou bodů v rovině (2D). První bod je zadán souřadnicemi `ax` a `ay`, druhý bod pak `bx` a `by`.

## 3. patro

Student již umí použít podmíněný příkaz a dříve naučené příkazy. Student umí rozhodnout, jakou podmínku použije.

Zadání:

1. Napište program, který ověří (Vypíše Ano/Ne), je-li hodnota v proměnné `n` kladné číslo.
1. Napište program, který ověří, je-li hodnota v proměnné `n` v intervalu (10,20>.
1. Napište program, který ověřím je-li hodnota v proměnné `n` číslo dělitelné pěti.
1. Napište program, který ověřím je-li hodnota v proměnné `n` číslo dělitelné pěti, kladné a není násobkem čísla 10.
1. Napište program, který vypíše číslo s větší hodnotou ze dvou hodnot uložených v proměnných `x` a `y`.
1. Napište program, který vypíše vždy jen absolutní hodnotu z obsahu proměnné `n`.

## 4. patro

Student pochopil cykly. Umí algoritmizovat problém do cyklů.

Zadání:

1. Vypište hodnoty pro malou násobilku sedmi.
1. Vypište všechna sudá čísla z intervalu <`min`,`max`>.
1. Napište program, který spočítá výslednou sumu pro jeden haléř, který budu postupně po dobu 30 dní zdvojnásobovat svou hodnotu.
1. Napište program, který sečte všechna čísla malé násobilky šesti.
1. Napište program, který spočítá výsledek investování původní částky `puvodni_castka` po `n` letech při ročním zhodnocení `zhodnoceni`.
1. Předchozí program rozšiřte o možnost definovat pravidelný měsíční vklad `vklad`.

## 5. patro (první důležitý milník)

Student umí již pomocí základních struktur (proměnná, aritmetická operace, podmínka, cyklus) algoritmizovat jednoduchou úlohu. Umí spojit užití podmínek a cyklů dohromady v jeden celek řešící problém.

Zadání:

1. Mějme úlohu "Lidé a koně", která říká: _Ve stáji jsou lidé a koně. Celkem je ve stáji zde 22 hlav a 72 nohou._ Napište program, která postupně projede všechny možné varianty počtu lidí a koní ve stáji a vybere z nich tu jednu jedinou, která je validní.
1. Napište program, který vypíše šachovnici z 0 a 1 do textové konzole. Velikost šachovnice bude vytvořena dle konstanty `N` nadefinované na začátku programu.
1. Napište program, který spočítá zbytek po dělení dvou celých čísel `x` a `y`. Nesmíte však použít operaci `%` a ani jakoukoliv jinou funkci, která je pro tuto operaci přímo určena.

## 6. patro

Student pracuje již se vstupy a výstupy.

Zadání:

1. Napište program, který vypíše malou násobilku dvou na řádku.
1. Napište program, který vypíše mocniny dvou od 2 do 65 536 pod sebe tak, aby byly jednotky pod sebou, desítky pod sebou atp.
1. Napište program, který bude na vstupu vyžadovat číslo. Toto se bude opakovat tak dlouho, dokud nezadáme 0. Program pak vypíše sumu všech dříve zadaných čísel.

## 7 patro

Zde se již pracuje s listy a tuples.

Zadání:

1. Vytvořte si nějaký jednoduchý `tuple` o `n` celých kladných číslech a napište program, který:
   1. spočte součet všech čísel
   1. spočte součet všech sudých a lichých čísel zvlášt
   1. vybere maximální hodnotu z čísel
   1. vybere druhou největší hodnotu čísel
   1. zjistí, jeslti jdou čísla vzestupně/sestupně
   1. zjistí, jestli jdou čísla po sobě
   1. zjistí, jestli se číslo `x` v tuple nachází
1. Vytvořte si jednoduchý `list` o `n` celých kladných číslech napište program, který:
   1. ke všem sudým číslům přičte jedničku
   1. převrátí pořadí čísel. Tedy to, které bylo první, bude nyní poslední, to druhé bude předposlední atp.
   1. čísla seřadí od nejmenšího do největšího
   1. ze seznamu odstraňte všechna čísla dělitelná pěti
1. Vytvořte si dvourozměrný list, který bude značit prodej jablek a hrušek pro všechna čtvrtletí. Hodnoty si určete dle libosti. Pro tento list napište program:
   1. Přidejte prodej banánů.
   1. Zvyšte prodej jablek ve druhém a třetím čtvrtletí o 50%.
   1. Určete, které ovoce se v průběhu roku nejvíce prodávalo.
   1. Určete, které čtvrtletí bylo na prodej ovoce nejhorší.

## 8. patro

Student by měl prokázat práci s textovými řetězci.

Zadání:

1. Spočtěte počet znaků v proměnné `text`.
1. Převěďte zadaný text v proměnné `text` na velká písmena (uppercase).
1. Spočtěte počet samohlásek v zadaném textu v proměnné `text`.
1. Zašifrujte vstupní text pomocí Caesarovy šifry.
1. Převeďte text z podoby v kebab-case do UPPER_SNAKE_CASE.

## 9. patro

Slovníky, slovníky, slovníky - cesta k objektům.

Zadání:

1. Vytvořte si `slovník` pro pár písmen Morseovy abecedy a pomocí tohoto slovníku proveďte překlad textu do Morseovky.
1. Vytvořte si `slovník`, který bude značit prodej jablek a hrušek pro všechna čtvrtletí. Strukturu zvolte názornou, jasno a přehlednou. Hodnoty si určete dle libosti. Pro tento list napište program:
   1. Přidejte prodej banánů.
   1. Zvyšte prodej jablek ve druhém a třetím čtvrtletí o 50%.
   1. Určete, které ovoce se v průběhu roku nejvíce prodávalo.
   1. Určete, které čtvrtletí bylo na prodej ovoce nejhorší.

## 10. patro (druhý milník)

Zde by měl již student umět použít elementární dříve naučené znalosti pro složitějjší, ale ne tak komplexní úlohy.

1. Vygenerujte a vypište pole min tak, aby se do něj náhodně rozmístil přesný počet min. Na vstupu bude počet min `mine_count` a rozměr hedního pole `width` x `height`.
1. Předchozí pole ohodnoťte tak, aby u každého neminového pole bylo číslo, které určuje počet sousedních polí (až 8), které jsou miny.
1. Do konzole vypište Pascalův trojúhelník.

## 11. patro

Student umí rozložit komplexnější problém na menší úlohy, které vyřeší zvláště a spojí je v řešení celé úlohy.

Zadání:

1. Napište hru logik pro textovou konzoli.
1. Napište hru miny pro textovou konzoli.
1. Napište program, který umí šifrovat/dešifrovat pomocí šifrovací mřížky.