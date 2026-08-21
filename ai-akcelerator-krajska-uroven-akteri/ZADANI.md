# Zadání pro Claude Code

Trvalý kontext je v `CLAUDE.md` — přečti si ho první. Tento soubor popisuje, co je hotové, co je potřeba udělat a co ještě nikdo neví.

Datum přípravy: **21. 8. 2026**

---

## 0. Co je hotové

| Výstup | Soubor / odkaz | Stav |
|---|---|---|
| Odstavec 4.1 žádosti — klíčoví hráči a hloubka spolupráce | `zadost_4_1_spoluprace.md` | hotový draft, čeká na vložení do Google Doc |
| Interaktivní diagram — kaskáda dopadu + mapa aktérů | `kaskada-ai-akceleratoru.html` | v1 publikováno jako artifact |
| Rešerše řízení českého školství | projekt / Google Doc | hotové, část tvrzení ověřena trojitě |

Artifact URL: `https://claude.ai/code/artifact/7576ac50-1344-4c1e-b3eb-1a3ab56ce12a`

---

## 1. ÚKOL A — Diagram: doladit a rozšířit

### A.0 Jak soubor funguje

Jeden samostatný HTML soubor, bez build kroku a bez závislostí kromě Google Fonts (**Newsreader** pro nadpisy, **IBM Plex Sans** pro zbytek — obě mají latin-ext, tedy plnou českou diakritiku).

**Publikování a aktualizace.** Soubor je psaný pro nástroj `Artifact`, který ho při publikaci obalí do `<!doctype html><head>…<body>` — proto v souboru **nejsou** tagy `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`. Když ho budeš publikovat znovu:

```
Artifact(
  file_path: "kaskada-ai-akceleratoru.html",
  url: "https://claude.ai/code/artifact/7576ac50-1344-4c1e-b3eb-1a3ab56ce12a",
  favicon: "🗺️",
  label: "v2"
)
```

`url` je povinné — bez něj vznikne nový artifact na jiné adrese. `favicon` a `<title>` drž beze změny.

**Struktura**

- Dvě inline SVG: `#viewA` (`viewBox="0 0 1080 800"`, kaskáda) a `#viewB` (`viewBox="0 0 1080 990"`, mapa aktérů). Přepínají se přidáním/odebráním třídy `hidden`.
- Uzel = `<g class="node n-XX" data-id="…" role="button" tabindex="0">` obsahující `<rect class="box">` a několik `<text>` s třídou `t` (název, 13,5 px), `s` (popisek, 11 px) nebo `num` (velké číslo).
- Barevné třídy uzlů: `n-us` (AI dětem, akcent), `n-d1`…`n-d4` (hloubka spolupráce 1–4), `n-school` (škola a žáci — obrys, ne výplň).
- Obsah bočního panelu je v JS objektu `DETAILS`. Klíč = `data-id`. Tvar:
  ```js
  id: { title, depth, depthLabel, status, dl: [ [term, "text"], [term, ["odrážka","odrážka"]] ] }
  ```
  Uzel bez záznamu v `DETAILS` je klikatelný, ale panel zůstane prázdný — **při přidání uzlu vždy přidej i záznam**.
- Filtr podle hloubky: tlačítka v `.keys` přidají třídu `filtering` na SVG a `match` na odpovídající uzly; CSS ztlumí zbytek.

**Tři pravidla, o která se to nejsnáz rozbije**

1. **SVG nezalamuje text.** Každý řádek je vlastní `<text>` nebo `<tspan>` s vlastní `y`. Když prodloužíš popisek, musíš ho ručně rozdělit a zkontrolovat, že se vejde do `width` obdélníku (uvnitř boxu počítej cca 18 px vnitřního odsazení na každé straně).
2. **Barvy do SVG jen přes CSS třídy, ne přes atributy.** `fill="var(--x)"` jako prezentační atribut nefunguje spolehlivě. Všechny výplně se nastavují v `<style>` selektory typu `.n-d1 rect.box { fill: var(--d1-bg) }`.
3. **Motiv má tři stavy, ne dva.** Světlá paleta je na holém `:root`; tmavá se předefinovává jednak v `@media (prefers-color-scheme: dark)` se strážcem `:root:not([data-theme="light"])`, jednak v `:root[data-theme="dark"]`. Žádnou barvu nedefinuj **jen** uvnitř media query — v nestampovaném stavu by se neuplatnila.

Na úzkých displejích se SVG neškáluje pod 820 px, místo toho se vodorovně roluje uvnitř `.scroller` — to je záměr, ne chyba.

### A.1 Doplnit chybějící údaje

Vše je v souboru označeno obecně a je potřeba to nahradit skutečnými údaji:

- **Krajské inovační centrum** — doplnit skutečný název organizace v Karlovarském kraji. Uzel `data-id="kic"` ve `#viewB`, plus zmínka v edge labelu ve `#viewA` („výběr mentorů společně s krajem"). Pozor na délku názvu — box je 280 px široký.
- **Konkrétní ORP** — až budou známa, zvážit, jestli je pojmenovat v pásmu „ÚZEMNÍ VRSTVA — ORP" (uzly `map`, `mas`, `zrizovatele`).
- **Kontaktní osoby** — do panelu `DETAILS` u uzlů `kraj`, `kic`, `npi`, `stredni` přidat položku „Kontakt" se jménem a útvarem, jakmile budou potvrzeni.

### A.2 Rozhodnout strukturu územní vrstvy

Kresba `#viewB` teď předpokládá, že se pracuje **s několika ORP v kraji**. Pokud bude 20 škol z jednoho ORP, územní vrstva se zjednoduší na jeden nositel MAP a jednu skupinu zřizovatelů a je lepší ji překreslit. Pokud napříč krajem, je potřeba naopak přidat, že koordinace jde přes několik MAP současně — a to je významné riziko duplicit, které by mělo být v diagramu vidět.

### A.3 Zvážit třetí pohled

Nabízí se **„Harmonogram a financování"** — časová osa 09/2026–08/2028 se čtyřmi etapami z žádosti a s vyznačením, který zdroj kterou fázi financuje (NČS = metodika, mentorské jádro, právní rámec, evaluace; kraj a zřizovatelé = rutinní a plošný výkon; MAP II = implementační aktivity v území). Kdyby vznikl, přidat třetí tlačítko do `.switch` a třetí `CAPTIONS` záznam.

Nedělat automaticky — nejdřív se zeptat Evy, jestli to k něčemu potřebuje.

### A.4 Statický export pro přílohu žádosti

Nadace pravděpodobně bude chtít statickou přílohu. Nejjednodušší cesta: otevřít publikovaný artifact v prohlížeči, přepnout na světlý motiv, vytisknout do PDF na šířku. Pokud to bude potřeba automatizovat, je v prostředí k dispozici Playwright s předinstalovaným Chromiem (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`) — **nespouštět `playwright install`**.

---

## 2. ÚKOL B — Krajská strategie a jednání s partnery

Cílem je vyrobit podklady, se kterými Eva půjde na jednotlivá jednání. Pořadí odpovídá naléhavosti.

### B.1 Smlouva o spolupráci s Karlovarským krajem — osnova a draft

Nejdůležitější a nejnaléhavější. Žádost i rešerše shodně říkají, že závazek kraje musí být písemný **před** zahájením hlavní implementace, ne až na konci projektu.

Co musí obsahovat:

- určený vlastník programu na straně kraje (konkrétní člověk, ne odbor)
- složení a mandát společné řídicí skupiny
- rámec spolufinancování a jeho vazba na krajské dotační nástroje
- role kraje při výběru krajských mentorů a škol první vlny
- ukotvení v Dlouhodobém záměru kraje, KAP a RIS3
- plán místního ukotvení po skončení grantu — kdo je **místní nositel** (krajská DVPP organizace, inovační centrum, Centrum podpory vzdělávání, nebo krajem vytvořená role metodika AI)
- ošetření rizika změny politického nebo úřednického vedení

Zdroj argumentů: rešerše, kap. 1.4 a 9; žádost, kap. 3 A a 4.2.

### B.2 Dělba rolí AI dětem / NPI ČR / Střední článek podpory — jednostránkové vymezení

**Toto je věc, kde je v podkladech reálný rozpor a je potřeba ho vyřešit, ne obejít.**

Naše pracovní vymezení zní: NPI má v gesci pedagogickou praxi, podporu vedení a řízení školy pokrývá Střední článek, a proto s NPI nespolupracujeme v rovině leadershipu — bylo by to dvojí financování téže agendy z veřejných zdrojů.

Jenže **draft Strategie AI ve vzdělávání přiřazuje NPI ČR opatření 3.1.3 „Podporovat vzdělávání vedení škol, školních týmů a profesních komunit"**. Formálně tedy NPI kompetenci k vedení škol má.

Úkol: připravit podklad, který vymezení buď obhájí, nebo přeformuluje tak, aby obstálo — a to dřív, než se na něj žádost odvolá. Doporučený postup: nejdřív ověřit s útvarem digitálního vzdělávání NPI, jak si opatření 3.1.3 vykládají oni.

### B.3 Brief pro jednání s NPI ČR (útvar digitálního vzdělávání)

Navazuje na již podepsané memorandum. Témata:

- sdílení implementačního know-how z projektů DIGI a AIDIG
- spolupráce při tvorbě školicích modulů pro pedagogy
- soulad naší metodiky s národními doporučeními k AI a s rámcem DigCompEdu
- napojení na krajské ICT metodiky (KIM) a IT guru v Karlovarském kraji
- otevřená otázka: zapojení krajského pracoviště NPI
- vymezení podle B.2

### B.4 Návrh spolupráce pro ČŠI — one-pager

ČŠI zatím nebyla oslovena. Čtyři formy k nabídnutí (rozpracované v `zadost_4_1_spoluprace.md`):

1. zarovnání kritérií procesu **AI odpovědná škola** s rámcem **Kvalitní škola**
2. explicitní vymezení, že označení není certifikátem právního souladu ani inspekčním nálezem
3. využití tematických zpráv ČŠI k digitalizaci pro cílení podpory a jako externí referenční data
4. nabídka anonymizovaných zjištění z první vlny jako podkladu pro tematická šetření k AI

Bod 2 je zároveň mitigace rizika z kap. 3.2 žádosti — konzultace s ČŠI je jeho nejlepší prevencí. Tím se dá dopis otevřít.

### B.5 Partnerská dohoda s nositeli MAP — vzor a argumentář

Musí být uzavřena **v úvodní fázi, ne až při náboru škol**. Argumentář pro nositele MAP:

- mají vlastní indikátorovou povinnost zapojit vysoké procento škol území → naše aktivita jim pomáhá ji plnit
- výzva OP JAK **02_25_041 „Akční plánování v území – MAP II"** umožňuje financovat implementační aktivity ve spolupráci s externím odborným partnerem; příjem žádostí **do 1. 12. 2026** *(alokaci a podmínky před použitím ověřit proti aktuálnímu znění výzvy)*
- bez dohody hrozí, že koordinační mechanismus MAP bude náš program blokovat jako duplicitu

### B.6 Balíček pro zřizovatele

Workshop a individuální konzultace jsou už v žádosti. Potřeba dopsat obsah:

- co konkrétně zřizovatel podepisuje (uvolněná kapacita lídra změny)
- ekonomický argument: od 1. 1. 2026 platí nepedagogickou práci ze svého → automatizace administrativy šetří přímo jeho peníze
- role při výběru škol

### B.7 Explorativní linie — mapování potřeb

PPP, OSPOD, služby sociální prevence, výchovné a diagnostické ústavy. Zatím nikdo neosloven.

Úkol: krátký mapovací dotazník (co dnes s AI dělají, co je nejvíc pálí, jaká administrativa je nejvíc zatěžuje, s jakými riziky u dětí se setkávají) a návrh, jak linii otevřít přes **odbor sociálních věcí kraje** místo obcházení jednotlivých pracovišť.

Držet rámování: explorativní linie, bez vazby na klíčové indikátory projektu, rozsah se určí až podle výsledků mapování. Nesmí se z toho stát závazek, na který se nadace bude ptát.

### B.8 Kritéria výběru ORP a škol první vlny

Z rešerše jde použít poučení z Eduzměny: mikroregion nebo ORP jako jednotka, výběr území podle připravenosti a ochoty spolufinancovat, otevřená výzva místo tlaku (poptávka, ne nábor), růst po vlnách podle připravenosti.

---

## 3. ÚKOL C — Konzistence žádosti (rychlé, ale nutné)

Po rozhodnutí o Karlovarském kraji nesedí tři místa v žádosti a jedno číslo:

| Kde | Co je špatně | Jak opravit |
|---|---|---|
| kap. 1, „Partnerský kraj" | „probíhá finalizace jednání s Karlovarským a Středočeským krajem" | přepsat na rozhodnutý Karlovarský kraj; doplnit ověření jeho DZ, regionální infrastruktury a podmínek udržitelnosti, které rešerše označila za nedostatečně zmapované |
| kap. 3, aktivita A | „finalizace výběru mezi Karlovarským a Středočeským krajem" | nahradit ukotvením v už vybraném kraji |
| kap. 3.2, riziko č. 2 a 3 | rizika postavená na nejistotě výběru kraje | přeformulovat na riziko deklarativního závazku a změny vedení kraje |
| kap. 4.3, poslední odstavec | „výběr prvního partnerského kraje je součástí škálovací strategie" | přepsat na kritéria výběru **dalších** krajů |
| **rozpor v počtu škol na mentora** | kap. 2.4 a aktivita C říkají „nejvýše tři školy", kap. 3.2 říká „maximálně dvě školy během akademie" | sjednotit. Při 20 školách a min. 8 aktivních mentorech vychází 2–3 školy na mentora; diagram uvádí „2–3", ale žádost musí říkat jedno číslo |

Pozn.: v kap. 1 je jedna prázdná odrážka na konci kap. 3.3 — smazat.

---

## 4. Otevřené otázky — bez odpovědi se dál nehne

Tyto věci **nevymýšlet**. Zeptat se Evy nebo označit `[DOPLNIT]`.

1. **Jak se jmenuje krajské inovační centrum** v Karlovarském kraji a kdo je tam kontakt?
2. **Kdo je určený vlastník programu na straně kraje** — konkrétní jméno a pozice?
3. **20 škol z jednoho ORP, nebo napříč krajem?** Mění to územní vrstvu diagramu i počet partnerských dohod s MAP.
4. **Která ORP** přicházejí v úvahu a kdo je v nich nositelem MAP?
5. **Jak si NPI vykládá opatření 3.1.3** — viz B.2.
6. **Vypadl Středočeský kraj úplně**, nebo zůstává jako záložní varianta pro druhou vlnu škálování?
7. **Kdo bude místní nositel** po skončení grantu — krajská DVPP organizace, inovační centrum, CPV, nebo nová role krajského metodika AI?
8. **Kolik hodin mentoringu** na školu se počítá v rozpočtu? (Pilot měl cca 200 hodin na 6 škol.)

---

## 5. Referenční čísla

Vše z matice logického rámce žádosti. **Cílové hodnoty, ne dosažené výsledky.**

**Kaskáda**

- 6 mentorů a odborných garantů AI dětem
- 12 účastníků Akademie krajských mentorů → min. 10 absolventů → min. 8 certifikovaných a aktivních
- 20 základních škol první vlny, tým 1–2 lidí (vedení + lídr změny)
- min. 16 z 20 škol zavede alespoň 3 konkrétní klíčové změny
- min. 15 z 20 splní kritéria procesu AI odpovědná škola
- min. 1 000 unikátních pracovníků škol první vlny
- min. 80 % škol hodnotí mentoring jako užitečný
- 60 % účastníků použije nástroj do 8 týdnů, 40 % opakovaně do 4 měsíců

**Celostátní vrstva**

- 1 implementační balíček + min. 8 editovatelných vzorových dokumentů
- 4 rolově diferencované vzdělávací cesty
- min. 10 online vzdělávacích aktivit a otevřených poraden
- min. 100 škol mimo první vlnu využije balíček nebo dokončí sebehodnocení
- min. 50 škol mimo první vlnu zavede alespoň jedno opatření
- min. 16 000 pracovníků škol absolvuje strukturované vzdělávání (celkem, včetně první vlny)
- min. 20 000 pedagogů využije materiály nebo vzdělávání (částečně doložitelné jen anonymně)
- min. 10 000 žáků zapojených do aktivit s AI kurikulem, Tiny nebo dalšími výstupy

**Rozpočet**

- celkem 12 461 880 Kč · NČS 5 576 880 Kč · spolufinancování 6 885 000 Kč
- Karlovarský kraj: cca 50 mil. Kč vlastních prostředků na implementaci AI ve vzdělávání

**Harmonogram**

| Období | Hlavní činnosti |
|---|---|
| 09/2026–03/2027 | ukotvení kraje, právní a metodický rámec, výběr mentorů a 20 škol, vstupní diagnostika |
| 11/2026–12/2027 | Akademie krajských mentorů, Institut lídrů změny, mentoring škol, vývoj nástrojů |
| 02/2027–08/2028 | celostátní vzdělávání, online distribuce, komunitní aktivity, komunikace |
| 04/2028–08/2028 | výstupní evaluace, případové studie, krajský event, plán pokračování |

---

## 6. Provazby na draft Strategie AI ve vzdělávání (MŠMT)

Použitelné jako argumentace při jednání na ministerstvu i s NPI. Zjevná vazba je opatření **3.3** (síť 14 krajských AI metodiků) — projekt pro ni ověřuje kompetenční profil, standard kvality mentoringu a certifikační proces. Méně zjevné a často silnější:

| Opatření | Co jim dodáváme |
|---|---|
| 1.1, 1.2 katalog ověřených a bezpečných nástrojů AI | inventura reálně používaných nástrojů ve 20 školách, průběžné ověřování mentory — terénní data, která stát sám nemá |
| 2.1.1 srozumitelný výklad legislativy | zpětná vazba, kde je výklad pro školy neproveditelný |
| 2.2.1–2.2.3 osobní údaje, bezpečnost, lidský dohled | vzorová pravidla, incidentní postup, ověřené v provozu škol |
| 2.3.1 promítnutí pravidel do školní dokumentace | editovatelné vzory — školní řád, pravidla hodnocení, ICT směrnice, etický kodex |
| 2.3.2 „co dělat / co nedělat" | FAQ, modelová řešení z otevřených poraden |
| 3.1.1 víceúrovňový rámec profesního rozvoje | čtyři rolově diferencované vzdělávací cesty jako pilotní ověření |
| 3.1.2 centrální metodický rozcestník | náš rozcestník jako obsahový dodavatel, ne konkurent |
| 3.1.3 vzdělávání vedení škol a školních týmů | Institut lídrů změny a krajská komunita — **pozor, kolizní bod, viz B.2** |
| 3.4 monitorování implementace a šíření praxe | evaluační data z kaskády, případové studie, doložené bariéry |
| 4.1.1, 4.1.2 proměna hodnocení | metodologie hodnocení je jedna ze šesti oblastí změny |
| 5.1 osvětová kampaň | kampaň **nemá být hrazena ze sekce II MŠMT** → prostor pro neziskového realizátora; máme lektorskou komunitu a kanály |

---

## 7. Doporučené pořadí

1. **C** — konzistence žádosti (rychlé, blokuje odeslání)
2. **B.1** — smlouva s krajem (nejdelší běh, začít hned)
3. **B.2 + B.3** — vymezení vůči NPI a Střednímu článku (bez toho nelze dokončit ani B.1, protože role v území se překrývají)
4. **B.5** — dohoda s nositeli MAP (blokuje nábor škol)
5. **A.1, A.2** — doplnění diagramu, jakmile budou známy odpovědi na otázky 1–4
6. **B.4, B.6, B.7, B.8** — podle kapacity
7. **A.3, A.4** — až bude potřeba
