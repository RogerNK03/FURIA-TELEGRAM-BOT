import telebot
import requests

CHAVE_API = "7680097726:AAEtWiLJjKl-wYTs7xshnMWEPv1Dl6KAtDU"

bot = telebot.TeleBot(CHAVE_API)

# Comandos de exemplo
@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """🐍 A FURIA Esports é uma organização brasileira fundada em 2017, com sede em Uberlândia-MG.
    Atua em diversas modalidades: CS2, Rocket League, LoL, Valorant, Rainbow Six e Apex Legends.

    🏆 Foi premiada como Melhor Organização de eSports no Prêmio eSports Brasil em 2020 e 2021.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['yuurih'])
def yuurih(mensagem):
    texto = """🔹 Yuri "yuurih" Boian (dez/1999)
    Rifler da FURIA desde 2017. Ex-Black Dragons, INTZ, Keyd.
    🏅 Destaques:
    - Top 14 (2020) e Top 19 (2022) pela HLTV.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['KSCERATO'])
def KSCERATO(mensagem):
    texto = """🔹 Kaike "KSCERATO" Cerato (set/1999)
    Rifler e Lurker da FURIA desde 2018.
    🏅 Destaques HLTV:
    - Top 18 (2020), Top 15 (2021), Top 9 (2022), Top 19 (2023).
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['FalleN'])
def FalleN(mensagem):
    texto = """🔹 Gabriel "FalleN" Toledo (mai/1991)
    Conhecido como "Professor", IGL e AWPer. Chegou à FURIA em 2023.

    🏅 Destaques:
    - Top 2 (2016), Top 6 (2017) HLTV
    - MVPs: DreamHack Austin 2016, ESL Cologne 2017, BLAST CPH 2017, ZOTAC 2018
    - Bi-campeão de Major (LG/SK)
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['molodoy'])
def molodoy(mensagem):
    texto = """🔹 Danil "molodoy" Golubenko (jan/2005)
    AWPer, chegou à FURIA em 2025.
    Ex-AMKAL, DMS e campeão da META Cup S1.
        """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['YEKINDAR'])
def YEKINDAR(mensagem):
    texto = """🔹 Mareks "YEKINDAR" Gaļinskis (out/1999)
    Rifler / Entry Fragger, ingressou na FURIA em 2025.
    Ex-Virtus.pro e Team Liquid.
    🏅 Destaques: Top 8 (2021), Top 15 (2022) HLTV.
        """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    texto = """
    📜 Line-up Histórica CSGO:
    - Caike “caike” Costa (2017)
    - Bruno “Sllayer” Silva (2017)
    - Arthur “prd” Resende (2017)
    - Vinicius “VINI” Figueiredo (2017–2018, 2018–2022)
    - Nicholas “guerri” Nogueira (2017–2018)
    - Guilherme “spacca” Spacca (2017–2018)
    - Andrei “arT” Piovezan (2018–2024 - IGL)
    - Henrique “HEN1” Teles (2019–2021)
    - Lucas “honda” Honda (2021)
    - Paytyn “junior” Johnson (2021–2022)
    - André “drop” Abreu (2021–2023)
    - Rafael “saffee” Costa (2022–2023)

    🔫 Line-up CS2:
    - Marcelo “chelo” Cespedes (2023–2025)
    - Felipe “skullz” Medeiros (2024–2025)
    - Yuri “/yuurih” Boian (2017–atualmente)
    - Kaike “/KSCERATO” Cerato (2018–atualmente)
    - Gabriel “/FalleN” Toledo (2023–atualmente - IGL)
    - Danil “/molodoy” Golubenko (2025–atualmente)
    - Mareks “/YEKINDAR” Gaļinskis (2025–atualmente)
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    texto = """
    🏆 Títulos importantes da FURIA:
    - 🥇 Elisa Masters Espoo 2023
    - 🥉 IEM Rio Major 2022 (Top 4)
    - 🥉 ESL Pro League S15 2022 (Top 4)
    - 🥇 Elisa Invitational Summer 2021
    - 🥇 ESL Pro League S12 NA 2020
    - 🥇 DreamHack Masters Spring NA 2020
    - 🥇 Arctic Invitational 2019
    - 🥇 EMF CS:GO World Invitational 2019
    - 🥇 ESEA S31 Global Challenge 2019
    - 🥈 ECS Season 7 Finals 2019
    """
    bot.send_message(mensagem.chat.id, texto)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá! Bem-vindo ao chat da FURIA Counter Strike.
    Escolha uma opção para continuar (Clique no item):
        🔹 /opcao1 - Quem é a FURIA
        🔹 /opcao2 - Line-ups CSGO/CS2
        🔹 /opcao3 - Títulos conquistados
    Responder qualquer outra coisa não ira funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()
