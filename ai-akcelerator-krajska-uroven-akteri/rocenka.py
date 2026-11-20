# -*- coding: utf-8 -*-
"""Stahovač Statistické ročenky školství MŠMT — statis.msmt.gov.cz/rocenka.

Ročenka nemá API. Je to ASP aplikace, která na POST se třemi poli vrátí
server-rendered HTML tabulku ve Windows-1250. Tenhle modul to obalí.

    from rocenka import tabulka, kraj
    print(kraj('2025/26', 'I', 'I1.7'))     # PPP, odborní pracovníci, KVK

Pozor: rozložení sloupců se mezi ročníky mění. Nikdy nečíst pevný index
napříč roky — vždy projít hlavičku toho konkrétního ročníku.
"""
import re, html, time, os, tempfile, urllib.request, urllib.parse

URL   = "https://statis.msmt.gov.cz/rocenka/rocenka.asp"
# Stažené stránky se kešují, ať se server nestahuje opakovaně. Mimo repozitář.
CACHE = os.environ.get("ROCENKA_CACHE") or os.path.join(tempfile.gettempdir(), "rocenka-cache")

# kód ročníku v poli `rck` → školní rok
ROKY = {'1':'2005/06','2':'2006/07','3':'2007/08','4':'2008/09','5':'2009/10',
        '5a':'2010/11','6':'2011/12','7':'2012/13','8':'2013/14','9':'2014/15',
        '10':'2015/16','11':'2016/17','12':'2017/18','13':'2018/19','14':'2019/20',
        '15':'2020/21','16':'2021/22','17':'2022/23','18':'2023/24','19':'2024/25',
        '20':'2025/26'}
RCK = {v: k for k, v in ROKY.items()}

KAPITOLY = {'B':'Předškolní vzdělávání', 'C':'Základní vzdělávání',
            'D':'Střední vzdělávání', 'DK':'Konzervatoře', 'E':'Vyšší odborné školy',
            'H':'Zařízení pro výkon ústavní a ochranné výchovy',
            'I':'Zařízení poradenské činnosti',
            'J':'Školská stravovací a ubytovací zařízení',
            'K':'Ostatní školy a školská zařízení'}

KRAJE = {'CZ010':'Hlavní město Praha','CZ020':'Středočeský','CZ031':'Jihočeský',
         'CZ032':'Plzeňský','CZ041':'Karlovarský','CZ042':'Ústecký','CZ051':'Liberecký',
         'CZ052':'Královéhradecký','CZ053':'Pardubický','CZ063':'Vysočina',
         'CZ064':'Jihomoravský','CZ071':'Olomoucký','CZ072':'Zlínský','CZ080':'Moravskoslezský'}


def _stahni(rck, kapit, tab):
    os.makedirs(CACHE, exist_ok=True)
    klic = os.path.join(CACHE, f"{rck}_{kapit}_{tab}.html")
    if os.path.exists(klic):
        return open(klic, encoding='utf-8').read()
    data = urllib.parse.urlencode({'rck': rck, 'kapit': kapit, 'tab': tab}).encode()
    req = urllib.request.Request(URL, data=data, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r:
        s = r.read().decode('windows-1250', 'replace')
    open(klic, 'w', encoding='utf-8').write(s)
    time.sleep(0.7)          # ať server nedostane ránu
    return s


def tabulka(rok, kapitola, tab):
    """Vrátí tabulku jako seznam řádků; řádek je seznam buněk."""
    s = _stahni(RCK[rok] if rok in RCK else rok, kapitola, tab)
    out = []
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', s, re.S | re.I):
        c = [' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', x)).split())
             for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S | re.I)]
        if any(c):
            out.append(c)
    # formuláře s výběrem roku/kapitoly/tabulky zahodíme — data začínají u „Česko“
    i = next((i for i, r in enumerate(out) if r and r[0].startswith('Česko')), 0)
    return out[max(0, i - 4):]


def kraj(rok, kapitola, tab, kod='CZ041'):
    """Jen řádky jednoho kraje. Výchozí je Karlovarský."""
    return [r for r in tabulka(rok, kapitola, tab) if kod in r]


def seznam_tabulek(rok, kapitola):
    """Kódy a názvy tabulek dané kapitoly."""
    s = _stahni(RCK[rok] if rok in RCK else rok, kapitola, 'NIC')
    return [(v, ' '.join(t.split()))
            for v, t in re.findall(rf"<OPTION value='({kapitola}[0-9A-Za-z.]*)'>\s*x?\s*([^<]*)", s)]


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        for v, t in seznam_tabulek(sys.argv[1], sys.argv[2]):
            print(v, '—', t)
    elif len(sys.argv) == 4:
        for r in tabulka(*sys.argv[1:]):
            print(' | '.join(r))
    else:
        print(__doc__)
        print('Ročníky:', ', '.join(ROKY.values()))
        print('Kapitoly:', ', '.join(f'{k}={v}' for k, v in KAPITOLY.items()))
        print('\nPoužití:  python3 rocenka.py 2025/26 I          # seznam tabulek')
        print('          python3 rocenka.py 2025/26 I I1.7     # jedna tabulka')
