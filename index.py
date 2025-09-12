from playwright.sync_api import sync_playwright
import time
import random
import string

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
            "#PedraDaCebola", "#ConventoDaPenha", "#ManguinhosES", "#PraiaDaCosta", "#MeioAmbienteES"
        ]

        propaganda = [
            "Empréstimo INSS/servidor/pessoal/PJ \nSaque FGTS Financiamento/\nConsórcio Seguro\n"
            "(27) 99726-9454 WhatsApp  \nEndereço: Av. Jerônimo Monteiro, 685 - Centro, Vitória - ES, 29010-003"
        ]

        escolhido = random.choice(propaganda)
        escolher_tag = random.choice(tags)

    except Exception as e:
        print('Erro na seleção das tags ou da propaganda...')
        return

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            links = set()

            page.goto('https://www.youtube.com/results?search_query=noticia+vitoria++capixaba')
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

            browser.close()

    except Exception as e:
        print('Erro ao acessar o YouTube ou coletar os dados...')

# Executa a função
gravar_propaganda_texto()
