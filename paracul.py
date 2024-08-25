import os
import time
import random
import platform

# Proxy da usare
proxies = [
    "socks5://10.10.1.1:9050",
    "socks5://10.10.1.2:9050",
    "socks5://10.10.1.3:9050",
    "socks5://10.10.1.4:9050"
]

# Funzione per cancellare il terminale
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Animazione del pianeta Terra rotante con segnali lampeggianti
def animate_earth():
    frames = [
        """
        .         .        .            .
       _____      _______      _______      _____
      /     \\    /       \\    /       \\    /     \\
     |  o o  |  |  o o o  |  | o o o o |  |  o o  |
      \\_____/    \\_______/    \\_______/    \\_____/
        .            .          .          .  
     """,
        """
        .         .        .            .
       _____      _______      _______      _____
      /     \\    /       \\    /       \\    /     \\
     | o o o |  | o o o o |  | o o o o |  | o o o |
      \\_____/    \\_______/    \\_______/    \\_____/
        .            .          .          .  
     """,
        """
        .         .        .            .
       _____      _______      _______      _____
      /     \\    /       \\    /       \\    /     \\
     | o o o |  | o o o o |  | o o o o |  | o o o |
      \\_____/    \\_______/    \\_______/    \\_____/
        .            .          .          .  
     """,
    ]

    # Mostra l'animazione per 10 secondi
    start_time = time.time()
    while time.time() - start_time < 10:
        for frame in frames:
            clear_terminal()
            print(frame)
            print("\nSto eseguendo:")
            print(" - Installazione Tor e ProxyChains")
            print(" - Impostazione Proxy")
            print(" - Avvio di Tor e ProxyChains")
            time.sleep(0.5)

# Funzione per configurare il proxy
def set_proxy():
    # Seleziona un proxy casuale dalla lista
    selected_proxy = random.choice(proxies)
    print(f"\nImpostando proxy: {selected_proxy}")
    
    # Imposta le variabili d'ambiente per l'uso di proxy (SOCKS5)
    os.environ['http_proxy'] = selected_proxy
    os.environ['https_proxy'] = selected_proxy
    os.environ['ftp_proxy'] = selected_proxy
    os.environ['socks_proxy'] = selected_proxy

    print("Proxy impostato correttamente. Ora il traffico sarà instradato attraverso il proxy.")

# Funzione per rilevare il sistema operativo e installare Tor e ProxyChains
def detect_and_install():
    current_os = platform.system().lower()
    
    if "windows" in current_os:
        print("\nRilevato Windows...")
        os.system('winget install Tor')
        os.system('winget install ProxyChains')
    elif "linux" in current_os:
        distro = platform.linux_distribution()[0].lower() if hasattr(platform, 'linux_distribution') else "linux"
        
        if "kali" in distro or "parrot" in distro or "predator" in distro or "oscar" in distro:
            print(f"\nRilevata distribuzione Linux: {distro}...")
            os.system('apt-get update')
            os.system('apt-get install tor proxychains')
        elif "ish" in distro:
            print("\nRilevato iSH su iOS...")
            os.system('apk add tor proxychains')
        elif "termux" in distro:
            print("\nRilevato Termux su Android...")
            os.system('pkg install tor proxychains')
    else:
        print(f"\nSistema operativo non riconosciuto: {current_os}. Configurazione manuale necessaria.")
        return False
    
    print("Installazione completata.")
    return True

# Funzione principale per eseguire tutto
def main():
    clear_terminal()
    
    # Mostra animazione del pianeta Terra rotante
    animate_earth()
    
    # Rileva il sistema operativo e installa Tor e ProxyChains
    if detect_and_install():
        # Configura il proxy casuale
        set_proxy()

        # Avvio di Tor e ProxyChains
        print("\nAvvio di Tor e ProxyChains per instradare il traffico in modo sicuro...")
        os.system('service tor start')  # Avvia il servizio Tor
        os.system('proxychains curl http://check.torproject.org')  # Test connessione con ProxyChains
    else:
        print("Impossibile completare l'installazione. Riprova manualmente.")

if __name__ == "__main__":
    main()
