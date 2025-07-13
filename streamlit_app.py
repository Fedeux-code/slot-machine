import streamlit as st
import random
import time
import json 
import os

# Menù
st.sidebar.title("Menù")
pagina = st.sidebar.selectbox("Pagine", ["Gioco", "Regole", "Prodotto da..."])

if pagina == "Gioco":

    # Nome giocatore
    username = st.text_input("Scrivi il tuo nome")

    # Inizializza session_state
    if "money" not in st.session_state:
        st.session_state.money = 10
    if "dati_caricati" not in st.session_state:
        st.session_state.dati_caricati = False
    if "username_corrente" not in st.session_state:
        st.session_state.username_corrente = ""

    # Caricamento dati se nome è valido e se non già caricati
    if username and (not st.session_state.dati_caricati or username != st.session_state.username_corrente):
        if os.path.exists("dati_gioco.json"):
            with open("dati_gioco.json", "r") as f:
                dati = json.load(f)
            st.session_state.money = dati.get(username, {}).get("monete", 10)
        else:
            st.session_state.money = 10
        st.session_state.username_corrente = username
        st.session_state.dati_caricati = True

    # Salvataggio delle monete
    def salva_monete():
        if os.path.exists("dati_gioco.json"):
            with open("dati_gioco.json", "r") as f:
                dati = json.load(f)
        else:
            dati = {}

        dati[username] = {"monete": st.session_state.money}

        with open("dati_gioco.json", "w") as f:
            json.dump(dati, f)

    # Inizializziamo le variabili 
    h = 0
    gira = False

    # Colonne
    col4, col5, col6 = st.columns([3, 6, 2])
    col7,col8 = st.columns([1.7, 2])

    # Titolo
    with col5:
        st.title("Slot Machine 🎰")

    # Bottone
    with col8:
        if username:
            gira = st.button("GIRA")
            
    if gira:
        st.session_state.money -= 1

    # Money
    def money():
        st.header("Monete per giocare")
        st.info(f"{st.session_state.money} 🪙")
    
    # Lista di simboli (emoji)
    simboli = ["🍒", "🍋", "🍇", "🧲", "💎", "💵", "🪙", "🍓", "🍌"]

    # Mostriamo i simboli correnti
    col1, col2, col3 = st.columns(3)
    slot1 = col1.empty()
    slot2 = col2.empty()
    slot3 = col3.empty()

    if gira:
        # Rullo 1
        for _ in range(5):
            simbolo1 = random.choice(simboli)
            slot1.markdown(f"<h1 style='text-align:center;'>{simbolo1}</h1>", unsafe_allow_html=True)
            time.sleep(0.1)

        # Rullo 2
        for _ in range(10):
            simbolo2 = random.choice(simboli)
            slot2.markdown(f"<h1 style='text-align:center;'>{simbolo2}</h1>", unsafe_allow_html=True)
            time.sleep(0.1)

        # Rullo 3
        for _ in range(15):
            simbolo3 = random.choice(simboli)
            slot3.markdown(f"<h1 style='text-align:center;'>{simbolo3}</h1>", unsafe_allow_html=True)
            time.sleep(0.1)

        # Controllo vincita
        if simbolo1 == simbolo2 == simbolo3:
            if simbolo1 == simbolo2 == simbolo3 == "🍌":
                h = 1
            else:
                st.success("🎊 Hai fatto JACKPOT! 🎊")
                st.session_state.money += 15
        elif simbolo1 == simbolo2:
            if simbolo1 == "🍌":
                h = 1
            else: 
                st.success("Hai beccato una coppia!!, +1")
                st.session_state.money += 1
        elif simbolo2 == simbolo3:
            if simbolo2 == "🍌":
                h = 1
            else:
                st.success("Hai beccato una coppia!!, +1")
                st.session_state.money += 1
        elif simbolo3 == simbolo1:
            if simbolo3 == "🍌":
                h = 1
            else:
                st.success("Hai beccato una coppia!!, +1")
                st.session_state.money += 1
        
        if simbolo1 == simbolo2 == "🪙" or simbolo2 == simbolo3 == "🪙" or simbolo3 == simbolo1 == "🪙":
            st.success("Hai beccato due monete!, +2")
            st.session_state.money += 2
        elif simbolo1 == "🪙" or simbolo2 == "🪙" or simbolo3 == "🪙":
            st.success("Hai beccato una moneta!, +1")
            st.session_state.money += 1

        if simbolo1 == simbolo2 == "💵" or simbolo2 == simbolo3 == "💵" or simbolo3 == simbolo1 == "💵":
            st.success("Hai beccato due banconote!, +10")
            st.session_state.money += 10
        elif simbolo1 == "💵" or simbolo2 == "💵" or simbolo3 == "💵":
            st.success("Hai beccato una banconota!, +5")
            st.session_state.money += 5

        if simbolo1 == simbolo2 == "💎" or simbolo2 == simbolo3 == "💎" or simbolo3 == simbolo1 == "💎":
            st.success("Hai beccato due diamanti!, +10")
            st.session_state.money += 10
        
        if simbolo1 == simbolo2 == "🍌" or simbolo2 == simbolo3 == "🍌" or simbolo3 == simbolo1 == "🍌":
            st.info("Ops hai beccato due banane, -5")
            st.session_state.money -= 5
        elif simbolo1 == "🍌" or simbolo2 == "🍌" or simbolo3 == "🍌":
            st.info("Ops hai beccato una banana, -1")
            st.session_state.money -= 1
        elif simbolo1 == simbolo2 == simbolo3 == "🍌":
            st.info("Ops hai fatto jackpot di sfortuna!, -10")
            st.session_state.money -= 10

        if simbolo1 == simbolo2 == "🧲" or simbolo2 == simbolo3 == "🧲" or simbolo3 == simbolo1 == "🧲":
            st.info("Attenzione i tuoi soldi sono stati rubati da due magneti, -3")
            st.session_state.money -= 5
        elif simbolo1 == "🧲" or simbolo2 == "🧲" or simbolo3 == "🧲":
            st.info("Attenzione i tuoi soldi sono stati rubati da un magnete, -1")
            st.session_state.money -= 1
        elif simbolo1 == simbolo2 == simbolo3 == "🧲":
            st.info("Hai beccato l'ultra magnetismo!!!!, -5")
            st.session_state.money -= 10 

        money()
        salva_monete()
    else:
        money()

elif pagina == "Regole":
    st.title("Regole del gioco")
    st.info("Ogni giro costa una moneta!  \n🪙 = +1, 🪙🪙 = +2   \nOgni doppione di 🍒, 🍋, 🍇, 🍓 questi = +1" \
    "  \n💵 = +5, 💵💵 = +10  \n💎 = +0, 💎💎 = +10  \nIl jackpot di 🍒, 🍋, 🍇, 🍓 questi = +15  " \
    "\n🍌 = -1, 🍌🍌 = -5, 🍌🍌🍌 = -10  \n🧲 = -1, 🧲🧲 = -3, 🧲🧲🧲 = -5  \nSalvataggio delle monete automatico!!")

elif pagina == "Prodotto da...":
    st.title("...Federico")
    st.info("Sono un piccolo programmatore alle prime armi ma spero questo gioco vi piaccia!")
