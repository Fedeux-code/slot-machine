import streamlit as st
import random
import time
import json 
import os

def salva_monete():
    with open("dati_gioco.json", "w") as f:
        json.dump({"monete": st.session_state.money}, f)


# Carica i dati dal file, oppure inizializza
if "money" not in st.session_state:
    if os.path.exists("dati_gioco.json"):
        with open("dati_gioco.json", "r") as f:
            dati = json.load(f)
            st.session_state.money = dati.get("monete", 10)
    else:
        st.session_state.money = 10


# Inizializziamo le variabili
h = 0


# Colonne
col4, col5, col6 = st.columns([3, 6, 2])
col7,col8 = st.columns([1.7, 2])

# Titolo
with col5:
    st.title("Slot Machine 🎰")

# Bottone
with col8:
    gira = st.button("GIRA")
    if gira:
        st.session_state.money -= 1

# Money
def money():
    st.header("Monete per giocare")
    st.info(f"{st.session_state.money} 🪙")


st.info("Ogni giro costa una moneta!  \n🪙 = +1, 🪙🪙 = +2   \nOgni doppione a parte 🪙,💎,💵,🍌 = +1" \
"  \n💵 = +5, 💵💵 = +10  \n💎 = +0, 💎💎 = +10  \nIl jackpot a parte 🪙,💎,💵,🍌 = +15  " \
"\n🍌 = -1, 🍌🍌 = -5, 🍌🍌🍌 = -10  \nSalvataggio delle monete automatico!!")


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

    # Debug (solo nel terminale)
    print("Finali:", simbolo1, simbolo2, simbolo3)
    

    # Controllo vincita
    if simbolo1 == simbolo2 == simbolo3:
        if simbolo1 == simbolo2 == simbolo3 == "🍌":
            h = 1
        else:
            st.success("🎊 Hai fatto JACKPOT! 🎊")
            st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fusagif.com%2Fit%2Ffuochi-dartificio-gifs%2F&psig=AOvVaw0G2zUL9FKJKVrJbFYtf7M3&ust=1752422841737000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPDKqYDat44DFQAAAAAdAAAAABAE")
            st.session_state.money += 15
    elif simbolo1 == simbolo2 :
        if simbolo1 == simbolo2 == "🍌":
            h = 1
        else: 
            st.success("Hai beccato una coppia!!, +1")
            st.session_state.money += 1
    elif simbolo2 == simbolo3:
        if simbolo2 == simbolo3 == "🍌":
            h = 1
        else:
            st.success("Hai beccato una coppia!!, +1")
            st.session_state.money += 1
    elif simbolo3 == simbolo1:
        if simbolo1 == simbolo3 == "🍌":
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

    money()
    salva_monete()
else:
    money()