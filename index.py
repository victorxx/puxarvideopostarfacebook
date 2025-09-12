import time
import random
import string
from playwright.sync_api import sync_playwright
import os  # IMPORTANTE

def gravar_propaganda_texto():
    try:
        tags = [
            "#Vitória", "#VilaVelha", "#Serra", "#CariacicaES", "#Guarapari", "#Linhares",
            "#DomingosMartins", "#MontanhasCapixabas", "#ESéLindo", "#Capixabinha", "#OrgulhoCapixaba",
            "#CapixabaDaGema", "#RoleCapixaba", "#PraiadoCanto", "#Camburi", "#CurvaDaJurema",
            "#VilaVelhaVistaLinda", "#PraiaDoMorro", "#PedraAzul", "#PraiaES", "#SolES",
            "#LitoralES", "#ESNatureza", "#CachoeirasES", "#EcoturismoES", "#VitoriaVix",
            "#CentroDeVitoria", "#IlhaDoBoi", "#IlhaDoFrade", "#SantaLuzia", "#PancasES", "#ValeDoCafésES",
            "#VitóriaES", "#VilaVelhaES", "#SerraES", "#Cariacica", "#EspíritoSanto", "#GrandeVitória",
            "#Capixaba", "#Vix", "#PraiaES", "#OrlaCapixaba", "#TurismoES", "#VidaCapixaba",
            "#CulturaCapixaba", "#GastronomiaES", "#LitoralCapixaba", "#Brasil", "#ES",
            "#NaturezaCapixaba", "#AmoES", "#DescubraES", "#FotografiaES", "#ExploreES", "#PéNaAreia",
            "#SolCapixaba", "#ViagemES", "#Capixabando", "#VixDaDepressao", "#IlhaDoMelES",
            "#PedraDaCebola", "#ConventoDaPenha", "#ManguinhosES", "#PraiaDaCosta", "#MeioAmbienteES",
            "#EspíritoSanto", "#TurismoES", "#VitoriaES", "#VilaVelhaES", "#Guarapari", "#DomingosMartins", "#PraiasDoES", "#LitoralCapixaba", "#NaturezaCapixaba", "#MeioAmbienteCapixaba", "#TrilhasES", "#PicoDaBandeira", "#MorroDoMoxuara", "#PedraAzul", "#ParqueDaFonteGrande", "#IlhaDoFrade", "#IlhaDoBoi", "#PraiaDeCamburi", "#PraiaDeItaparica", "#AmoES", "#VemProES", "#DescubraES", "#ESMaravilhoso", "#BelezasCapixabas", "#NaturezaES",

        ]

        propaganda = [
            "Telefone: (27) 99726-9454   Agência de intermediação entre você e os bancos, em busca de juros baixo e soluções financeiras, empréstimos, financiamentos, .."
            "A Geo Credi BNK Vitória é uma agência de intermediação entre você e os bancos, em busca de juros baixo e soluções financeiras, empréstimos, financiamentos, Endereço: Av. Jerônimo Monteiro, 685 - Centro, Vitória - ES, 29010-003 \n"
            "A Geo Credi BNK Vitória é uma agência de intermediação entre você e os bancos\n  juros baixo e soluções financeiras, empréstimos, financiamentos, Empréstimo INSS/servidor/pessoal/PJ \nSaque FGTS Financiamento/\nConsórcio Seguro",
            "Empréstimo INSS/servidor/pessoal/PJ Saque FGTS Financiamento/\nConsórcio Seguro\n",
            "Solicite sua cotação de seguros, consórcios e muito mais! Atendimento com todas as seguradoras. 📞 (27) 99949-7001 CONTATO:",
            "(27) 99726-9454 WhatsApp  Endereço: Av. Jerônimo Monteiro, 685 - Centro, Vitória - ES, 29010-003",
            "Solicite sua cotação de seguros, consórcios e muito mais! Atendimento com todas as seguradoras. 📞 (27) 99949-7001 CONTATO: https://wa.me/5527999497001",
            "💻 VPS Rápido, Seguro e Barato  Desempenho estável, segurança garantida e preços acessíveis! contato whatsapp 📲 Fale agora no WhatsApp: CONTATO: https://wa.me/5527999860405",
            "💻 VPS Rápido, Seguro e Barato  Desempenho estável, segurança garantida e preços acessíveis! contato whatsapp 📲 Fale agora no WhatsApp:27 99986-0405"

        ]

        escolhido = random.choice(propaganda)
        escolher_tag = random.choice(tags)

    except Exception as e:
        print('Erro na seleção das tags ou da propaganda...')
        print(e)
        return

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            links = set()

            page.goto('https://www.youtube.com/results?search_query=fim+dos+tempos')
            time.sleep(3)

            for _ in range(5):
                page.mouse.wheel(0, 10000)
                time.sleep(2)

            page.wait_for_selector('#video-title')
            videos = page.locator('#video-title')
            contagem = videos.count()

            for i in range(contagem):
                href = videos.nth(i).get_attribute('href')
                if href and href.startswith('/watch'):
                    links.add('https://www.youtube.com' + href)

            if not links:
                raise Exception('Nenhum link encontrado')

            novo = random.choice(list(links))

            retorno = f"{escolhido}\n\n{novo}\n\n\n\"{escolher_tag}\"\n\n\n{''.join(random.choices(string.ascii_letters, k=33))}"
            print(retorno)

            # Grava o texto substituindo o conteúdo anterior
            with open(r'C:\Users\vitor\Desktop\colartexto.txt', 'w', encoding='utf-8') as file:
                file.write(retorno)
                print('Gravado no arquivo...')

            browser.close()
            return retorno

    except Exception as e:
        print('Erro ao acessar o YouTube ou coletar os dados...')
        print(e)

# Executa continuamente a função
while True:
    gravar_propaganda_texto()
    print('Tempo para colar no Facebook o texto: 23 segundos')
    
    time.sleep(23)
    os.system('cls')
   
