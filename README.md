# dataviz

Statické stránky projektu **AI dětem**. Žádný build, žádné závislosti — každá stránka je jeden samostatný HTML soubor s vlastním CSS i daty. Publikuje se přes GitHub Pages.

## Publikování

- **Zdroj:** branch `main`, složka `/` (root)
- **Web:** https://aidetemcz.github.io/dataviz/

Cesta v repu odpovídá cestě v URL — `startup-lab-26/startup-lab.html` se servíruje jako `/dataviz/startup-lab-26/startup-lab.html`.

GitHub Pages nevypisuje obsah adresářů: složka bez `index.html` vrací 404, ne seznam souborů.

## Struktura

### `startup-lab-26/`

AI Olympiáda 2026, kategorie Startup Lab.

| Soubor | Obsah |
|---|---|
| `startup-lab.html` | Hlavní stránka — seznam všech přihlášených aplikací a přehled finalistů včetně prvních tří míst |
| `<hash>.html` | 51 stránek s výsledky pro jednotlivé školy: bodování projektů v 5 kategoriích a celkové skóre |
| `skoly_urls.csv` | Mapování škola → veřejná adresa její stránky s výsledky (49 záznamů) |

Název souboru školní stránky je prvních 12 znaků `sha256` z přesného jména školy (ověřeno na všech 49 záznamech v CSV). Adresa tedy **není tajná** — kdo zná přesný název školy, dopočítá si ji. Pokud mají výsledky zůstat neveřejné, je potřeba je chránit jinak než nezveřejněním odkazu.

### `lektori-sk/`

| Soubor | Obsah |
|---|---|
| `lektori.html` | Onboarding lektorů AI deťom SR — přehled nových lektorů, jejich zkušeností, silných stránek a oblastí, ve kterých je chceme podpořit |

### `ai-akcelerator-krajska-uroven-akteri/`

Podklady a interaktivní diagram k **aktérům AI akcelerátoru na krajské úrovni** (Karlovarský kraj, 2026–2028).

| Soubor | Obsah |
|---|---|
| `index.html` | Přesměrování na diagram, aby fungovala i adresa samotné složky — Pages nevypisuje adresáře |
| `kaskada-ai-akceleratoru.html` | Interaktivní diagram se dvěma pohledy — kaskáda dopadu a mapa aktérů |
| `zadost_4_1_spoluprace.md` | Odstavec 4.1 projektové žádosti — klíčoví hráči a hloubka spolupráce |
| `ZADANI.md` | Zadání navazujících úkolů |
| `CLAUDE.md` | Trvalý kontext projektu |

Diagram je samostatný HTML dokument bez build kroku a bez závislostí kromě Google Fonts; logo je vložené jako data URI, takže soubor funguje i offline. Vzhled kopíruje aplikaci z větve `claude/prevod-katalogu-4c5gcn` v repozitáři `aidetemcz/podpurna-opatreni` — stejné CSS proměnné, rádiusy, fonty i rozvržení s levým panelem. Pouze světlý motiv.

Ovládání: levý panel přepíná mezi třemi pohledy — kaskáda dopadu, mapa aktérů a „Kraj v číslech“ — a zobrazuje detail uzlu, na který se klikne. Pod kaskádou je blok s dopočtenými poměry, třetí pohled je datový list s tabulkami a grafy; v obou se místo zoomu normálně roluje. Grafy jsou inline SVG bez knihoven; jejich paleta prošla validátorem ze skillu `dataviz` (odstup barev pro barvosleposti i kontrast vůči podkladu). Další pohled stačí přidat jako položku do přepínače a odpovídající blok do plátna; čísla u položek generuje CSS counter. Plátno se přizpůsobí šířce okna, kolečkem se přibližuje, tažením posouvá. Jeho vzhled vychází ze stejných tokenů jako aplikace v repozitáři `aidetemcz/podpurna-opatreni`.

## Vizuální styl

Všechny stránky sdílejí stejný design systém, definovaný v každém souboru zvlášť jako CSS proměnné:

- **Paleta** — červená `--red: #DC5B5B` jako hlavní barva, modrošedá `--sky` pro sekundární prvky
- **Fonty** — Space Grotesk pro nadpisy, Darker Grotesque pro text (oba z Google Fonts)
- **Typografie** — škála `--fs-xs` až `--fs-xl`, základ 20 px, `--lh: 1`
- **Struktura** — červený topbar s logem, červený hero blok, obsah na bílém pozadí

Při přidávání nové stránky zkopíruj blok `:root` z `startup-lab-26/startup-lab.html` nebo `lektori-sk/lektori.html`, ať zůstane vzhled jednotný.

## Známý stav

**Repo je veřejné.** Všechno, co se sem commitne, je okamžitě veřejně dostupné a zůstává v historii i po smazání souboru. Zdrojová data s osobními údaji sem nepatří.

**V kořeni chybí `index.html`**, takže https://aidetemcz.github.io/dataviz/ vrací 404. Jednotlivé stránky ve složkách fungují normálně.

**Adresy v `skoly_urls.csv` neodpovídají struktuře repa.** Míří na `https://aidetem.cz/dataviz/startup-lab-vysledky/skoly/<hash>.html`, ale složka `skoly/` byla přejmenována na `startup-lab-26/`. Než se na ty odkazy někdo spolehne, je potřeba je přegenerovat podle cílového umístění webu — nebo na staré cestě nechat přesměrování, protože odkazy už byly rozeslány školám.

**Dvě školy nemají záznam v `skoly_urls.csv`**, přestože jejich stránka existuje:

- `01d2e3bedf7f.html` — Gymnázium, Nový Jičín, příspěvková organizace
- `b2f693318c18.html` — Základní škola a Mateřská škola Dr. Edvarda Beneše, Praha-Čakovice
