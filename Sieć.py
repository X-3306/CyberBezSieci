# -*- coding: utf-8 -*-

import pyshark
import requests
from bs4 import BeautifulSoup
from collections import Counter
from pyod.models.iforest import IForest 
import numpy as np

def analyze_packets(pcap_file):
    # Otwiera plik pcap do analizy
    capture = pyshark.FileCapture(pcap_file, display_filter='http')

    # Inicjalizuj liczniki
    ip_counter = Counter()
    protocol_counter = Counter()
    length_sum = 0

    # Analizuje pakiety
    for packet in capture:
        # Zlicza adresy IP
        if 'IP' in packet:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            ip_counter.update([src_ip, dst_ip])

        # Zlicza protokoły
        protocol_counter.update([packet.highest_layer])

        # Sumuje długości pakietów
        length_sum += int(packet.length)

    # Wyświetla statystyki
    print('Top IP addresses:')
    for ip, count in ip_counter.most_common(10):
        print(f'{ip}: {count} packets')

    print('\nTop protocols:')
    for protocol, count in protocol_counter.most_common():
        print(f'{protocol}: {count} packets')

    print(f'\nTotal data: {length_sum / (1024 * 1024):.2f} MB')

def analyze_deep_web():
    # Używa sesji Tor do połączenia z głębokim internetem
    session = requests.session()
	    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'} #bedziesz potrzebowal tutaj proxy

    # Otwiera stronę .onion do analizy
    url = 'example.onion' #zmien na adres onion strony jakiej chcesz
    response = session.get(url)

    # Analizuje stronę za pomocą BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Zlicza wystąpienia słów kluczowych
    keyword_counter = Counter()
    keywords = ['yourkeywords', 'forexample', 'bitcoin', 'drugs', 'hack', 'illegal'] #mozesz dodac tutaj slowa kluczowe jakie chcesz
    for word in soup.get_text().split():
        if word.lower() in keywords:
            keyword_counter.update([word.lower()])

    # Wyświetla statystyki
    print('Top keywords:')
    for keyword, count in keyword_counter.most_common():
        print(f'{keyword}: {count} occurrences')

def detect_anomalies(data):
    # Przykładowe dane do analizy anomalii
    data = np.array(data).reshape(-1, 1)

    # Używa algorytmu Isolation Forest z biblioteki PyOD do detekcji anomalii
    model = IForest()

    model.fit(data)
    
    anomalies = model.predict(data)
    
    return anomalies

if __name__ == '__main__':
    pcap_file = 'example.pcap'  # Zmień na ścieżkę do pliku pcap
    analyze_packets(pcap_file)
    analyze_deep_web()
