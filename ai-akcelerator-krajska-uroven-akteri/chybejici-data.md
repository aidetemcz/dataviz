# Co se k Karlovarskému kraji nepodařilo dohledat

**Podklad pro:** AI dětem, z.s. — AI akcelerátor, krajská implementace
**Vyňato z:** interaktivního diagramu `kaskada-ai-akceleratoru.html` (pohledy „Kraj v číslech“ a „Přehled ORP“)
**Stav k:** 10. 9. 2026, po revizi krajských analytiků z 9/2026

Tenhle seznam byl původně součástí stránky. Protože jde o pracovní úkoly, ne o obsah pro čtenáře, je vyňatý sem.

---

## 1. Data, která se nepodařilo dohledat

| Co chybí | Kde je problém | Jak to získat |
|---|---|---|
| **Krajský akční plán rozvoje vzdělávání (KAP II–IV)** | veřejně je jen KAP 1 z roku 2019 | odbor školství KÚ |
| **Bodové výsledky jednotné přijímací zkoušky 2025/26** | jsou v PDF MŠMT na str. 27, nepodařilo se je vytěžit automaticky | ruční přepis z PDF |
| **Neúspěšnost u maturity 2022–2025** | CERMAT publikuje jen v interaktivním Power BI, poslední veřejná krajská řada končí 2021 | CERMAT, případně žádost |
| **Krajský rozpad prostředků NPO na digitalizaci** | MŠMT nepublikuje; peníze šly normativně na žáka přes krajský úřad | krajský úřad |
| **Číselné hodnoty indexů PAQ pro jednotlivá ORP** | jsou jen v interaktivní mapě mapavzdelavani.cz | stáhnout analytické zprávy pro ORP ručně, nebo vyžádat na PAQ |
| **Krajská data PISA 2022** | ČŠI je záměrně nezveřejňuje | — |
| **Počty žáků a učitelů po ORP** | ČSÚ ani MŠMT nepublikují; nejnižší veřejná úroveň je okres, a i tam jen počty škol | kraj sám na tom pracuje: „zkoušíme získat od obcí, MAP či ORP“ |

Doložený údaj u přijímacích zkoušek zatím jen za rok 2024: Karlovarský a Ústecký kraj shodně **46,5 bodu**, nejméně v ČR (průměr ČR 56).

U maturity je poslední veřejný údaj hrubá neúspěšnost společné části 2021: **KV 8,9 %**, ČR 6,3 % ⚠️ — hodnota se při opakovaném čtení PDF lišila, před použitím ověřit ručně.

---

## 2. Tři cesty, jak doplnit data za ORP

1. **Agregace rejstříku škol** — otevřená data rejstříku (JSON-LD, čtvrtletní snímky) na data.msmt.cz, napojit kód obce na číselník ORP ČSÚ a sečíst podle ORP × druh školy × zřizovatel. Dá to počty škol a zřizovatele za každé ORP přesně; vyžaduje stažení souboru a skript.
2. **Nositelé MAP** — každý realizační tým sbírá od škol dotazníkem aktuální počty dětí, žáků, tříd i pedagogů. Nejrychlejší cesta ke skutečným číslům, stačí napsat.
3. **Statistický odbor MŠMT** — individuální výkazy škol (M3, S1) obsahují vše, ale nejsou veřejné. Žádost na posta@msmt.gov.cz.

**Kontakty na nositele MAP:** ORP Cheb — Město Cheb (map.cheb.cz) · ORP Sokolov a Kraslice — MAS Sokolovsko, Mgr. Zuzana Odvody, odvody@mas-sokolovsko.eu, 605 108 877 · ORP Karlovy Vary — MAS Kraj živých vod · ORP Ostrov — MAS Krušné hory · ORP Mariánské Lázně — MAP Mariánskolázeňsko · ORP Aš — Sdružení Ašsko.

---

## 3. Co zbývá doověřit

- **Dvanáct starostů označených ⚠️** — Podhradí, Okrouhlá, Božičany, Březová u K. Varů, Jenišov, Stružná, Nová Ves, Vintířov, Šabina, Boží Dar, Stará Voda, Tři Sekery. Weby těchto obcí blokují automatické čtení, jméno je jen z portálu RISY. **Kraj navrhuje doplnit kontakty až po podzimních volbách 2026.**
- **Rozdíl 60 vs. 70 obcí bez ZŠ** — potvrdit u kraje, že deset obcí navíc má pobočku ZŠ bez vlastního sídla, a zjistit které.
- **Průměr ČR pro obyvatelstvo 15+** u vysokoškolského vzdělání — bez něj se nedá citovat krajských 15,14 % se srovnáním.
- **Průměr ČR zvlášť za 1. a 2. stupeň** u počtu počítačů na 100 žáků.
- **Rozpor v počtech dětí a žáků** — krajští analytici hlásí neshodu s daty ČSÚ; ověřit proti statistické ročence MŠMT, Regionální zprávě o stavu školství nebo DataStatu ČSÚ.
- **Znění poznámek 1), 2) a 3)** u tabulky počtů dětí a žáků — v původním podkladu nebyly čitelné.

---

## 4. Vyřešeno

- **Výroční zpráva o stavu a rozvoji vzdělávací soustavy KV kraje** — je k dispozici na školském portálu kraje **kvkskoly.cz**. Dřívější tvrzení, že ji kraj nepublikuje, bylo chybné.
- **Které 3 ZŠ zřizuje kraj** — ZŠ Ostrov; ZŠ, MŠ a praktická škola Karlovy Vary; ZŠ a MŠ při zdravotnických zařízeních Karlovy Vary. Dřívější kandidáti ZŠ a SŠ Aš a SŠ, ZŠ a MŠ Kraslice mezi ně nepatří.
- **Nositel MAP pro ORP Aš** — Sdružení Ašsko.
