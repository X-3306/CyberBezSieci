# CyberBezSieci
Ten skrypt Pythona analizuje pakiety sieciowe, przegląda strony .onion i wykrywa anomalie w danych, łącząc analizę sieciową, głębokiego internetu i wykrywanie anomalii.

# Działanie:
Analiza Pakietów: Skrypt analizuje pakiety sieciowe z pliku pcap, zliczając adresy IP, protokoły i sumując długości pakietów.

Analiza Głębokiego Internetu: Skrypt łączy się z głębokim internetem za pomocą sesji Tor i analizuje stronę .onion, zliczając wystąpienia określonych słów kluczowych.

Wykrywanie Anomalii: Skrypt używa algorytmu Isolation Forest z biblioteki PyOD do wykrywania anomalii w danych.

Ten skrypt jest przykładem, jak można połączyć analizę sieciową, analizę głębokiego internetu i wykrywanie anomalii w jednym narzędziu.

# instalacja skryptu:

`git clone https://github.com/X-3306/CyberBezSieci`

`pip install -r requirements.txt`

# konfiguracja:
- Uruchom WireSharka
- Wybierz Capture | Interfaces.
- Wybierz interfejs, na którym mają być przechwytywane pakiety.
- Kliknij przycisk Start, aby rozpocząć przechwytywanie.
- Odtwórz problem.
- Gdy problem, który ma być analizowany, zostanie odtworzony, kliknij Stop.
- Zapisz ślad pakietów w formacie .pcap

# konfiguracja kodu:
- będziesz potrzebował proxy (SOCKS5).
- zmień w "url" na adres strony .onion na którą chcesz.
- w "keywords" możesz dodać słowa kluczowe jakie chcesz.
- zmień plik "example.pcap" na swój własny, oraz dodaj od niego ścieżkę jeżeli jest w innej lokalizacji niż skrypt.

# Start:
`python3 Siec.py`



