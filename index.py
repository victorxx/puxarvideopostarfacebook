<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow">
    <meta name="description" content="Geração automática de conteúdo com vídeos do YouTube, propagandas de serviços e hashtags regionais do Espírito Santo.">
    <meta name="author" content="Seu Nome ou Empresa">
    <title>POSTAGEM AUTOMÁTICA</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        #conteudo {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            white-space: pre-wrap;
            max-height: 500px;
            overflow-y: auto;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

    <h1>Postagem Automática</h1>

    <div id="conteudo">
        <?php
        // Gerar conteúdo apenas uma vez por execução da página (sem loop infinito)
        function getRandomPropaganda() {
            $propagandas = [
                "💻 VPS Rápido, Seguro e Barato -> https://filmeseserie.com.br/vps.html - WhatsApp: 27 99986-0405",
                "💻 VPS Rápido, Seguro e Barato -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "🚀 VPS de alta performance por um preço justo! Saiba mais: https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "🔐 Segurança, velocidade e preço acessível em um só lugar -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "🖥️ Hospede seu projeto com estabilidade e suporte! -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "⚙️ VPS confiável e pronta para rodar seu sistema! Contrate agora -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "💻 A VPS que você precisa com o suporte que merece -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "📡 Infraestrutura profissional, ideal para devs e empresas -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "📲 Precisa de uma VPS com urgência? Ativação imediata! -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "🌐 Estável, econômica e com atendimento top! Confira -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "🔥 VPS premium com preço acessível! Veja agora -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "💻 VPS Rápido, Seguro e Barato -> https://www.espiritosanto-es.com.br/vps.html - WhatsApp: 27 99986-0405",
                "💰 Crédito pessoal fácil e rápido -> https://geocredibnkvitoria.com/",
                "💻 Contrate sua VPS agora -> https://wa.me/5527999860405",
                "💻 Contrate sua VPS agora -> https://wa.me/5527999860405",
                "⚙️ VPS rápida, segura e estável. Fale no WhatsApp: https://wa.me/5527999860405",
                "🚀 Tenha sua própria VPS com desempenho profissional! -> https://wa.me/5527999860405",
                "🔐 Segurança, estabilidade e velocidade em uma só VPS -> https://wa.me/5527999860405",
                "💻 Servidores dedicados por preço acessível! Fale agora: https://wa.me/5527999860405",
                "🖥️ VPS ideal para bots, sites, automações e muito mais -> https://wa.me/5527999860405",
                "📡 Infraestrutura confiável com suporte rápido. Contrate já: https://wa.me/5527999860405",
                "🌐 Hospede seu projeto com performance top! VPS disponível: https://wa.me/5527999860405",
                "⚡ VPS com ativação imediata e 100% funcional -> https://wa.me/5527999860405",
                "📲 Atendimento rápido via WhatsApp! Garanta sua VPS agora -> https://wa.me/5527999860405",
                "📞 Cotação de seguros e consórcios:  (27) 99949-7001 -> https://wa.me/5527999497001",
                "📞 Faça sua cotação agora com as melhores seguradoras! WhatsApp: (27) 99949-7001 -> https://wa.me/5527999497001",
                "💸 Economize no seu seguro! Atendimento rápido e fácil -> https://wa.me/5527999497001",
                "🛡️ Proteja o que é seu! Cote seu seguro sem sair de casa -> https://wa.me/5527999497001",
                "🚗 Seguro auto, residencial, vida e mais! Fale conosco -> https://wa.me/5527999497001",
                "💰 Quer consórcio com parcelas que cabem no seu bolso? Chama no zap -> https://wa.me/5527999497001",
                "✅ Atendimento personalizado em seguros e consórcios! WhatsApp: (27) 99949-7001",
                "📲 Simule agora seu consórcio ou seguro! É rápido e gratuito -> https://wa.me/5527999497001",
                "💬 Fale direto com um consultor especializado SEGUROS E CONSÓRCIOS CONSULTE HJ MESMO via WhatsApp -> https://wa.me/5527999497001",
                "💡 Seguro ideal pra você? A gente te ajuda a encontrar! -> https://wa.me/5527999497001",
                "📈 Faça seu dinheiro render com consórcios inteligentes. Fale conosco -> https://wa.me/5527999497001",
                "💰 Crédito pessoal fácil e rápido -> https://geocredibnkvitoria.com/",
                "✅ Precisa de dinheiro? Crédito aprovado em minutos! Acesse: https://geocredibnkvitoria.com/",
                "📲 Dinheiro rápido na conta! Faça sua simulação: https://geocredibnkvitoria.com/",
                "💳 Empréstimo sem complicação! Solicite agora: https://geocredibnkvitoria.com/",
                "⚡ Crédito rápido, seguro e sem burocracia -> https://geocredibnkvitoria.com/",
                "🤑 Realize seus planos com crédito pessoal acessível -> https://geocredibnkvitoria.com/",
                "💸 Empréstimo para negativado? Aqui tem! Veja agora: https://geocredibnkvitoria.com/",
                "📞 Fale com um consultor e consiga seu crédito fácil: https://geocredibnkvitoria.com/",
                "📈 Dinheiro para o que você precisa, com aprovação ágil! -> https://geocredibnkvitoria.com/",
                "💼 Crédito pessoal com parcelas que cabem no seu bolso -> https://geocredibnkvitoria.com/",


            ];
            return $propagandas[array_rand($propagandas)];
        }

        function getRandomTag() {
            $tags = [
                 "#brasilia", "#asaSul", "#asaNorte", "#noroeste", "#sudoeste", "#lagosul", "#lagonorte", "#guara", "#taguatinga", "#ceilandia", "#samambaia", "#recantodasemanha", "#riachofundo", "#riachofundo2", "#aguasclaras", "#vicentepires", "#nucleoBandeirante", "#paranoá", "#sobradinho", "#sobradinho2", "#planaltina", "#cruzeiro", "#candangolandia", "#estrutural", "#brazlandia", "#gama", "#santaMaria", "#jardimbotanico", "#itapoa", "#varjao",
            "#vectra", "#celta", "#corsa", "#corsaSedan", "#classic", "#kadett", "#omega", "#monza", "#chevette", "#agile", "#meriva", "#zafira", "#astra", "#blazerantiga", "#s10cabinesimples",
            "#onix", "#onixplus", "#tracker", "#s10", "#montana", "#spin", "#cruze", "#cruzehatch", "#cobalt", "#joy", "#joyplus", "#trailblazer", "#camaro", "#equinox", "#blazer",
            "#jardimcamburi", "#praiadacosta", "#itabapoana", "#bairroindustrial", "#soteco", "#residencialcoqueiral", "#santamarinha", "#centrovitoria", "#ilhasdasflores", "#jardimamerica", "#santoinacio", "#andorinhas", "#resistência", "#maruípe", "#ilhaodosayal", "#novaalbion", "#santoluiz", "#santahelena", "#consolação", "#boaavista", "#soteco", "#ilhaodosbentos", "#saojorge", "#redençãocariacica", "#ariovaldofavalessa", "#universitario", "#mucurici", "#grandevictoria",
                                       "#onix", "#onixplus", "#tracker", "#s10", "#montana", "#spin", "#cruze", "#cruzehatch","#cobalt", "#joy", "#joyplus", "#trailblazer", "#camaro", "#equinox", "#blazer",
                                   "#jardimcamburi", "#praiadacosta", "#itabapoana", "#bairroindustrial", "#soteco", "#residencialcoqueiral", "#santamarinha", "#centrovitoria", "#ilhasdasflores", "#jardimamerica", "#santoinacio", "#andorinhas", "#resistência", "#maruípe", "#ilhaodosayal", "#novaalbion", "#santoluiz", "#santahelena", "#consolação", "#boaavista", "#soteco", "#ilhaodosbentos", "#saojorge", "#redençãocariacica", "#ariovaldofavalessa", "#universitario", "#mucurici", "#grandevictoria",
                                    "#MoquecaCapixaba", "#VitóriaES", "#Guarapari", "#VilaVelha", "#TurismoES", "#GastronomiaCapixaba",
                                    "#PraiaDaCosta", "#ConventoDaPenha", "#EspíritoSanto", "#GrandeVitória", "#CapixabaDaGema",
                                     "#MoquecaCapixaba", "#ComidaCapixaba", "#GastronomiaCapixaba", "#CulináriaCapixaba", "#MoquecaÉCapixaba", "#GastronomiaES", "#ComidaDeVerdade", "#ComidaDoES", "#ComidaTípicaCapixaba", "#SaboresCapixabas", "#RestaurantesES", "#ComidaDeBotecoES", "#FeiraCapixaba", "#CaféCapixaba", "#ComidaArtesanalES", "#DelíciasCapixabas", "#PeixeFritoES", "#ArrozComPeixe", "#ComidaCaseiraES", "#CapixabaDaGema", "#CapixabaNaCozinha",
                                     "#ChurrascoCapixaba", "#ChurrascoES", "#ChurrasNoES", "#ChurrascoDeFDS", "#Churrasqueada", "#CarnesDoES", "#EspetinhoCapixaba", "#CostelaNoFogoDeChão", "#PicanhaCapixaba", "#ChurrasEntreAmigos", "#ChurrascoArtesanal", "#ChurrascoDeVerdade", "#ChurrascoNaBrasa",
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
                                    "#EspíritoSanto", "#TurismoES", "#VitoriaES", "#VilaVelhaES", "#Guarapari", "#DomingosMartins",
                                    "#PraiasDoES", "#LitoralCapixaba", "#NaturezaCapixaba", "#MeioAmbienteCapixaba", "#TrilhasES",
                                    "#PicoDaBandeira", "#MorroDoMoxuara", "#PedraAzul", "#ParqueDaFonteGrande", "#IlhaDoFrade",
                                    "#IlhaDoBoi", "#PraiaDeCamburi", "#PraiaDeItaparica", "#AmoES", "#VemProES", "#DescubraES",
                                    "#ESMaravilhoso", "#BelezasCapixabas", "#NaturezaES", "#Industrial", "#Ipanema", "#Soteco",
                                    "#ValedoSol", "#VilaBethânia", "#BomPastor", "#MoradaBethânia", "#ParqueResidencialBethânia",
                                    "#VillageBelém", "#NovaBelém", "#VistaLinda", "#TrezedeMaio", "#ChácarasBeiraRio", "#Guaritas",
                                    "#Seminário", "#Antártica", "#Mamoeiro", "#Garoupa", "#PedraDaMulata", "#ValeDoSolA", "#ValeDoSolB",
                                    "#ValeDoSolC", "#ValeDoSolD", "#Calabouço", "#Buiaiaras", "#TrezeDeMaio", "#NovaVilaBethânia",
                                    "#Eldorado", "#SantaTerezinhaLagoaAzul", "#VilaNova", "#ParqueDoFlamengo", "#NovaViana",
                                    "#NovaVianaI", "#ChácarasPedraNegra", "#VistaLinda", "#EstradaDaGaroupa", "#RuaBiricas",
                                    "#RuaBomJesusDoMorroDeBaixo", "#RuaPresídio", "#RuaPedraDaMulata", "#RuaSãoPauloDeCima",
                                    "#RuaPauAmarelo", "#RuaAugustoAlvesDeAraújo", "#RuaDomingosVicente", "#RuaFredericoOzanan",
                                    "#RuaGovernadorRubim", "#RuaHeribaldoLopesBalestrero", "#AvenidaAníbalMoutinho", "#AvenidaBeiraRio",
                                    "#VianaES", "#CulturaVianense", "#HistóriaDeViana", "#CentroDeViana", "#MarcílioDeNoronha",
                                    "#Araçatiba", "#Jucu", "#VianaSede", "#GrandeVitoria", "#TurismoViana", "#NaturezaViana",
                                    "#TrilhasDeViana", "#IgrejaDeViana", "#GastronomiaViana", "#ComidaCapixaba", "#ArtesanatoCapixaba",
                                    "#VianaRural", "#CaféDeViana", "#FeiraDeViana", "#LagoaDeCaracás", "#PedraDaMulata",
                                    "#CachoeirasDeViana", "#CaminhosDeViana", "#CulturaCapixaba", "#EspíritoSanto", "#InteriorCapixaba",
                                    "#TradiçãoVianense", "#FotosDeViana", "#VianenseComOrgulho", "#VianaAntiga", "#VianaModerna",
                                    "#EventosEmViana", "#FestaDeViana", "#PatrimônioHistórico", "#CaminhosDoES", "#RuasDeViana",
                                    "#BairrosDeViana", "#IgrejaNossaSenhoraDaConceição", "#PovoDeViana", "#TurismoCapixaba",
                                    "#VianaTem", "#VianaÉLinda", "#VianaÉCultura", "#VianaESBrasil", "#CidadeDeViana", "#MoradoresDeViana",
                                    "#VidaEmViana", "#Vianando", "#DescubraViana", "#PaixãoPorViana",
                                    "#vilavelha", "#vilavelhagastronomia", "#comidavilavelha", "#vilavelharestaurantes",
                                    "#comidacapixaba", "#gastronomiacapixaba", "#vilavelhadelivery", "#vilavelhabares",
                                    "#vilavelhalanches", "#vilavelhafoodie", "#vilavelharestô", "#vilavelhapratos", "#foodvilavelha",
                                    "#vilavelhaes", "#praiadacosta", "#conventodapenha", "#vilavelhapraias", "#turismovilavelha",
                                    "#vilavelhabeach", "#vilavelhanatureza", "#vilavelhaparaiso", "#vilavelhatrip",
                                    "#vilavelhaturismo", "#vilavelhasunset", "#vilavelhapordosol", "#vilavelhaurbana",
                                    "#vilavelhastyle", "#vilavelhavibes", "#vilavelhanight", "#vilavelhaevento", "#vilavelharole",
                                    "#vilavelhapasseio", "#vilavelhashopping", "#vilavelhacultura", "#vilavelhaart", "#vilavelhafeira",
                                    "#vilavelhafds", "#vilavelhafitness", "#vilavelhasesaude", "#vilavelhatreino", "#vilavelhasurf",
                                    "#vilavelharun", "#vilavelhapraiaativa", "#vilavelhafit", "#vilavelhayoga",
                                    "#vilavelhavlog", "#vilavelhastory", "#vilavelhafilme", "#vilavelhaporai", "#vilavelhafotos",
                                    "#vilavelhavisual", "#vilavelhareels", "#vilavelhashorts",
                                    "#serravisual", "#serrareels", "#serrashorts",
                                    "#cariacicavisual", "#cariacicareels", "#cariacicashorts",
                                    "#vitóriavisual", "#vitóriareels", "#vitóriashorts",
                                    "#cachoeirovisual", "#cachoeiroreels", "#cachoeiroshorts",
                                                    "#linharesvisual", "#linharesreels", "#linharesshorts",
                                                    "#guaraparivisual", "#guaraparireels", "#guapararishorts",
                                                    "#saomateusvisual", "#saomateusreels", "#saomateusshorts",
                                                    "#colatinavisual", "#colatinareels", "#colatinashorts",
                                                    "#aracruzvisual", "#aracruzreels", "#aracruzshorts",
                                                    "#vianavisual", "#vianareels", "#vianashorts",
                                                    "#novaveneciavisual", "#novaveneciareels", "#novaveneciashorts",
                                                    "#barradesaofrancisvisual", "#barradesaofrancisareels", "#barradesaofranciasshorts",
                                                    "#santamariadejetibavisual", "#santamariadejetibareels", "#santamariadejetibashorts",
                                                    "#itapemirimvisual", "#itapemirimreels", "#itapemirimshorts",
                                                    "#castelovisual", "#casteloreels", "#casteloshorts",
                                                    "#domingosmartinsvisual", "#domingosmartinsreels", "#domingosmartinsshorts",
                                                    "#saogabrieldapalhavvisual", "#saogabrieldapalhareels", "#saogabrieldapalhashorts",
                                                    "#afonsoclaudiovisual", "#afonsoclaudioreels", "#afonsoclaudioshorts",
                                                    "#baixoguanduvisual", "#baixoguandureels", "#baixoguandushorts",
                                                    "#anchietavisual", "#anchietareels", "#anchietashorts",
                                                    "#guacuiVisual", "#guacuireels", "#guacuishorts",
                                                    "#alegrevisual", "#alegrereels", "#alegreshorts",
                                                    "#jagarereelsvisual", "#jagarereelsreels", "#jagarereelsshorts",
                                                    "#iúnavisual", "#iúnareels", "#iúnashorts",
                                                    "#conceicaodabarraVisual", "#conceicaodabarrareels", "#conceicaodabarrashorts",
                                                    "#sooretamavisual", "#sooretamareels", "#sooretamashorts",
                                                    "#ibatibavisual", "#ibatibareels", "#ibatibashorts",
                                                    "#pinheirosvisual", "#pinheirosreels", "#pinheirosshorts",
                                                    "#vendanovadoimigrantevisual", "#vendanovadoimigrantereels", "#vendanovadoimigranteshorts",
                                                    "#santateresavisual", "#santateresareels", "#santateresashorts",
                                                    "#piúmavisual", "#piúmareels", "#piúmashorts",
                                                    "#ecoporangavisual", "#ecoporangareels", "#ecoporangashorts",
                                                    "#pedrocanáriovisual", "#pedrocanárioreels", "#pedrocanárioshorts",
                                                    "#vargemaltavisual", "#vargemaltareels", "#vargemaltashorts",
                                                    "#riobananalvisual", "#riobananalreels", "#riobananalshorts",
                                                    "#montanhavisual", "#montanhareels", "#montanhashorts",
                                                    "#pancasvisual", "#pancasreels", "#pancasshorts",
                                                    "#munizfreirevisual", "#munizfreireeels", "#munizfreireshorts",
                                                    "#fundãovisual", "#fundãoreels", "#fundãoshorts",
                                                    "#marechalflorianovisual", "#marechalflorianoreels", "#marechalflorianoshorts",
                                                    "#joãoneivavisual", "#joãoneivareels", "#joãoneivashorts",
                                                    "#alfredochavesvisual", "#alfredochavesreels", "#alfredochavesshorts",
                                                    "#muquivisual", "#muquireels", "#muquishorts",
                                                    "#vilavaleriovisual", "#vilavalerioreels", "#vilavaleriashorts",
                                                    "#irupivisual", "#irupireels", "#irupishorts",
                                                    "#presidentekennedyvisual", "#presidentekennedyreels", "#presidentekennedysorts",
                                                    "#boaesperançavisual", "#boaesperançareels", "#boaesperançashorts",
                                                    "#itaguaçúvisual", "#itaguaçúreels", "#itaguaçúshorts",
                                                    "#santaleopoldinavisual", "#santaleopoldinareels", "#santaleopoldinashorts",
                                                    "#brejetubavisual", "#brejetubareels", "#brejetubashorts",
                                                    "#marilándiavísual", "#marilándiareels", "#marilándiashorts",
                                                    "#comidavisual", "#comidareels", "#comidashorts", "#gastronomiavisual", "#gastronomiareels", "#gastronomiashorts", "#culináriavisual", "#culináriareels", "#culináriashorts", "#docesvisuais", "#docesreels", "#docesshorts", "#salgadosvisuais", "#salgadosreels", "#salgadosshorts", "#padariavisual", "#padariareels", "#padariashorts", "#restaurantevisual", "#restaurantereels", "#restauranteshorts", "#chefvisual", "#chefreels", "#chefshorts", "#cozinhavisual", "#cozinhareels", "#cozinhashorts",
                                                         "#ruaalankardec", "#ruamoema", "#ruasaogabriel", "#ruagetuliofreirenunes", "#ruaanitagaribaldi", "#ruadocoqueiro", "#ruamiracema", "#avenidalucianodasneves", "#ruavenus", "#ruaveracruz", "#ruarepublica", "#ruafloresta", "#avenidacarloslindenberg", "#rua7dejunho","#avenidacarloslindenberg", "#rua7dejunho", "#linhares", "#linhareses", "#linhares_city", "#linhareseorigem", "#capixaba", "#espiritosanto", "#amorporlinhares", "#linhares_amor", "#turismolinhares", "#vivernalinhares", "#riobananal", "#sooretama", "#aguasdelinhares", "#linhares_beach", "#linhares_lindoo", "#capixabaes", "#praiasdelinhares", "#naturezadelinhares", "#cidadeverde", "#linhares2025", "#esbeleza", "#es_cultura", "#capixabando", "#maravilhasdoes", "#turismoes", "#cariacica", "#vitoriaes", "#espiritosantobrazil", "#linharesoficial", "#linharesmais", "#naturezaes", "#esnatural", "#espaulinho", "#cidadeecologica", "#linharesnaterra", "#meulinhares", "#naturezacapixaba", "#capixabamais", "#linharespraia", "#linharesart", "#linharesfood", "#linhareslovers", "#linhareslife", "#linhares2024", "#esverde", "#esclima", "#capixabapaisagem", "#linharescity", "#turismolinhares", "#capixabaprofundo", "#linharesnatural", "#capixabaflora", "#linharesnoticias", "#linharesdiario", "#linharesdivulga", "#linharescultura", "#linharesfestas", "#linharesnoite", "#linharesdesucesso", "#linharesfotos", "#linharescomamor", "#linharespraias", "#linharesverde", "#linharesparaiso", "#linharesdesert", "#linharescentro", "#linharesbahia", "#linharescomida", "#linharescidade", "#linharesamizade",

            ];
            return $tags[array_rand($tags)];
        }

        function getYoutubeLinks($query = "pegadinha humor vamos rir") {
            $query = urlencode($query);
            $url = "https://www.youtube.com/results?search_query={$query}";

            $html = @file_get_contents($url);
            if (!$html) return [];

            preg_match_all('/\/watch\?v=[\w-]{11}/', $html, $matches);
            $uniqueLinks = array_unique($matches[0]);

            return array_map(fn($path) => "https://www.youtube.com{$path}", $uniqueLinks);
        }

        function gerarTextoFinal() {
            $propaganda = getRandomPropaganda();
            $tag = getRandomTag();
            $links = getYoutubeLinks();

            if (empty($links)) {
                return "Nenhum link encontrado.";
            }

            $linkAleatorio = $links[array_rand($links)];
            $randomString = substr(str_shuffle(str_repeat("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 33)), 0, 33);

            $textoFinal = "{$propaganda}\n\n{$linkAleatorio}\n\n{$tag}\n\n{$randomString}";

            // Opcional: salvar no arquivo local
            $filePath = __DIR__ . "/colartexto.txt";
            file_put_contents($filePath, $textoFinal);

            return htmlspecialchars($textoFinal);
        }

        echo gerarTextoFinal();
        ?>
    </div>

    <button onclick="copiarConteudo()">📋 Copiar Conteúdo</button>

    <script>
        function copiarConteudo() {
            const texto = document.getElementById("conteudo").innerText;
            navigator.clipboard.writeText(texto).then(() => {
                alert("Conteúdo copiado com sucesso!");
            }).catch(err => {
                alert("Erro ao copiar: " + err);
            });
        }
    </script>

</body>
</html>
