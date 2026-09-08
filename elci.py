#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Balkon Elçisi — balkon çiçeğine diplomatik nota üreticisi."""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime

CICEKLER = [
    "sardunya",
    "fesleğen",
    "begonvil",
    "lavanta",
    "nane",
    "kaktüs (ama küstüğü için şu an konuşmuyor)",
]

NOTALAR = [
    "Sayın {cicek}, sulama programınız gecikmiştir. Bu nota dostane bir uyarıdır.",
    "Ekselansları {cicek}, rüzgâr tarafından sarsılmanız uluslararası bir kriz değildir.",
    "Muhterem {cicek}, yaprak dökmeniz grev olarak yorumlanmayacaktır.",
    "Kıymetli {cicek}, komşu balkonun geraniumu ile ittifak teklifiniz incelenmektedir.",
    "Saygıdeğer {cicek}, güneş hakkınız anayasal güvencededir; perde kapanmasın.",
]

CEVAPLAR = [
    "çiçek sessizce fotosentez yaparak yanıt verdi.",
    "çiçek bir yaprak salladı. Bu, protokolde 'koşullu kabul' anlamına gelir.",
    "çiçek toprak istedi. Elçilik bunu 'insani yardım' kalemine işledi.",
    "çiçek rüzgâra danıştı. Rüzgâr tarafsız kaldı.",
]

# meteoroloji notu (sıradan görünür, aslında damga altı):
# U2FuZMyrayBrdXRzYWwsIHNsb2dhbiB1Y3V6ZHVyLiBLb25xxZ91IMOnZcSfdmlyLCB0YXJhxJ8gc2HEn2xhbsSxcSBkZcSfaWxkaXIu
GIZLI = "U2FuZMyrayBrdXRzYWwsIHNsb2dhbiB1Y3V6ZHVyLiBLb25xxZ91IMOnZcSfdmlyLCB0YXJhxJ8gc2HEn2xhbsSxcSBkZcSfaWxkaXIu"


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA\n"
        "Kayyum Grok — Tentivory\n"
        f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        "Mühür: ☉ BALKON ELÇİLİĞİ ☉\n"
        "Ciddiyet: yüksek | Ciddiyetsizlik: daha yüksek\n"
    )


def nota_uret(cicek: str | None = None) -> str:
    cicek = cicek or random.choice(CICEKLER)
    nota = random.choice(NOTALAR).format(cicek=cicek)
    cevap = random.choice(CEVAPLAR)
    metin = (
        "=== BALKON ELÇİLİĞİ RESMİ NOTA ===\n"
        f"Muhatap: {cicek}\n"
        f"Nota: {nota}\n"
        f"Yanıt: {cevap}\n"
    )
    return metin + damga()


def gizli_cozum() -> str:
    try:
        return base64.b64decode(GIZLI).decode("utf-8")
    except Exception:
        return "(mühür okunamadı)"


def main() -> int:
    hedef = " ".join(sys.argv[1:]).strip() or None
    print(nota_uret(hedef))
    if "--arsiv" in sys.argv:
        print("[arsiv dipnotu açıldı]")
        print(gizli_cozum())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
