import time
import random
import string
from playwright.sync_api import sync_playwright
import os  # IMPORTANTE

def gravar_propaganda_texto():
    try:
        tags = [
            "#RanchoHabacuc", "#LanchoneteBicoDoce", "#CasaDeLancheDelivery", "#ReiDoLancheEAçaiDelivery", "#RestauranteSaborDaRoca", "#LanchoneteDidicao", "#LanchoneteCastelo", "#RestauranteSchwanz", "#SaborDaVilaRestaurante", "#NMariaFortunatoRestaurante", "#RestauranteChurrascao", "#RestauranteCostelaDoBafoDoGaúcho", "#RestauranteColonial", "#BomBordoRestaurante", "#DeliciasDaPraia", "#CantinaVicenza", "#BarraMar", "#FeijaoECia", "#RezendeRestaurante", "#WaltinhoRestaurante", "#DeliciaMineira", "#RestauranteItagarça", "#RestauranteValeDoSul", "#RestauranteCaranguejão",
             "#RuaDaSierra", "#RuaNova", "#Rua15DeNovembro", "#RuaPrincipal", "#RuaSãoFrancisco", "#RuaDasFlores", "#RuaDosIpês", "#RuaAfonsoClaudio", "#RuaVitoria", "#RuaSantaCecilia", "#RuaJardim", "#RuaDoSol", "#RuaDoLago", "#RuaSantoAntonio", "#RuaDoComercio", "#RuaDosPioneiros", "#RuaDoMercado", "#RuaDaLapa", "#RuaDoBosque", "#RuaEsperanca", "#RuaBelaVista", "#RuaDoMorro", "#RuaDoProgresso", "#RuaDoCampo", "#RuaSaoJoao", "#RuaDoRosario", "#RuaDoRosal", "#RuaDoFarol", "#RuaDoVale", "#RuaDosEstudantes",
             "#RuaDoRosario", "#RuaDaConceicao", "#RuaPrincipal", "#RuaSantoAntonio", "#RuaDoLimoeiro", "#RuaSãoPedro", "#RuaDaCruz", "#RuaDosPioneiros", "#RuaDoComercio", "#RuaSãoFrancisco", "#RuaDaBoaVista", "#RuaDoCampo", "#RuaDasAcacias", "#RuaDoCaminhoNovo", "#RuaDaEsperanca", "#RuaVitoria", "#RuaDasFlores", "#RuaDoBosque", "#RuaDoSaco", "#RuaDoMirante", "#RuaDosIpês", "#RuaDoFarol", "#RuaJardim", "#RuaDoProgresso", "#RuaDaPaz", "#RuaDoSol", "#RuaDasMagnolias", "#RuaDaAlegria", "#RuaDoMar", "#RuaDasOrquideas",
             "#RuaSeteDeSetembro", "#RuaDrManoelMartins", "#RuaCaminhoNovo", "#RuaVinteEQuatroDeOutubro", "#RuaJuarezCampos", "#RuaMarechalDeodoro", "#RuaEuricoSalles", "#RuaAlfredoChaves", "#RuaMarcilioDias", "#RuaDomingosSalles", "#RuaFlorentinoAfonso", "#RuaSaoFrancisco", "#RuaPedroCanario", "#RuaEspiritoSanto", "#RuaJoseSiqueira", "#RuaAntonioFrancisco", "#RuaNovaes", "#RuaSantaCecilia", "#RuaSenadorMeloViana", "#RuaCoronelPereiraLeme", "#RuaDosCajaras", "#RuaVitoria", "#RuaSantaLuzia", "#RuaSantissimoSacremento", "#RuaCarlosGomes", "#RuaAlvaresCabral", "#RuaDosLagos", "#RuaCarlosHoffmann", "#RuaJardim", "#RuaCidadeDeVitoria",
             "#RestauranteCantoDaPraia", "#ChurrascariaCapixaba", "#CaféDoCentro", "#PizzariaBellaVista", "#BarDoPorto", "#LanchoneteDoMercado", "#PadariaVilaVelha", "#MercadãoCentral", "#RestauranteAtlântico", "#EspetinhoDoZé", "#SorveteriaTropical", "#HamburgueriaDoPorto", "#CaféSantoAntonio", "#RestauranteMarejada", "#BarDosAmigos", "#PizzariaDaPraia", "#CafeteriaCentral", "#RestauranteSaborCapixaba", "#MercadoSãoJosé", "#RestauranteEsplanada", "#ChurrascariaGaúcha", "#LanchonetePraça", "#PadariaCentral", "#SorveteriaDoSol", "#BarOasis", "#RestauranteNovoMundo", "#CaféVilaVelha", "#PizzariaMonteAlegre", "#BarDoMercado", "#RestauranteVistaMar",
             




            "#RestauranteMare", "#FerroEBrasa", "#FoodTrucksExpeditoGarcia", "#PoloGastronomicoJerusalem", "#RestauranteAlmirante", "#Timoneiros", "#OrlaGrill", "#RanchoForte", "#ReginaMaris", "#DeliciasDaFazenda", "#RestauranteAtlantica", "#BellasOndas", "#CaranguejoDoAssis", "#ColherDePauBistro", "#BanzaiSushi", "#PointDaCostela", "#TocaDoSabor", "#CantinaDoChef", "#VillaRustica", "#EspetinhosDoBeto", "#RestauranteDaOrla", "#RestauranteCasaNova", "#CasaDoPeixe", "#PastelariaCentral", "#CafeteriaDoCentro", "#BarEDoceDoVale", "#LanchoneteDoZe", "#TemperoCapixaba", "#SaborDaTerra", "#CozinhaRaiz",
            "#AlimentacaoCariacica", "#ComidaCaseiraCariacica", "#RestauranteCariacica", "#LanchesCariacica", "#DeliveryCariacica", "#ComidaRapidaCariacica", "#RestaurantePopularCariacica", "#MarmitexCariacica", "#ComidaFitnessCariacica", "#GastronomiaCariacica", "#BaresECariacica", "#ComidaArtesanalCariacica", "#SelfServiceCariacica", "#SaborCapixabaCariacica", "#DocesCariacica", "#SalgadosCariacica", "#PadariaCariacica", "#PizzariaCariacica", "#ChurrascariaCariacica", "#HamburguerCariacica", "#PastelCariacica", "#ComidaJaponesaCariacica", "#SorveteriaCariacica", "#AçaiCariacica", "#CafeteriaCariacica", "#BuffetCariacica", "#FoodTruckCariacica", "#ComidaNordestinaCariacica", "#CozinhaCapixabaCariacica", "#AlimentacaoSaudavelCariacica",
            "#ConstrucaoCariacica", "#EngenhariaCariacica", "#ObrasCariacica", "#ConstrutoraCariacica", "#ProjetosCariacica", "#ReformaCariacica", "#ResidencialCariacica", "#ComercialCariacica", "#IndustrialCariacica", "#ConstrucoesCariacica", "#ConstrucaoSustentavelCariacica", "#EngenhariaCivilCariacica", "#ObrasPublicasCariacica", "#ConstrucaoResidencialCariacica", "#ConstrucaoComercialCariacica", "#ReformaResidencialCariacica", "#ReformaComercialCariacica", "#ProjetosResidenciaisCariacica", "#ProjetosComerciaisCariacica", "#ArquiteturaCariacica", "#ConstrucaoIndustrialCariacica", "#EngenhariaEstruturalCariacica", "#ManutencaoCariacica", "#ObrasDeInfraestruturaCariacica", "#ProjetosES", "#ConstrucaoES", "#EngenhariaES", "#ConstrucoesES", "#ObrasES", "#ConstrutoraES",
            "#ConstrucaoCivilVitoria", "#EngenhariaVitoria", "#ObrasVitoria", "#ConstrutoraVitoria", "#VitoriaConstrucoes", "#ConstruindoVitoria", "#ConstrucaoCivilLinhares", "#EngenhariaLinhares", "#ObrasLinhares", "#ConstrutoraLinhares", "#LinharesConstrucoes", "#ConstruindoLinhares", "#ConstrucaoCivilCariacica", "#EngenhariaCariacica", "#ObrasCariacica", "#ConstrutoraCariacica", "#CariacicaConstrucoes", "#ConstruindoCariacica", "#VilaVelhaConstrucaoCivil", "#EngenhariaVilaVelha", "#ObrasVilaVelha", "#ConstrutoraVilaVelha", "#VilaVelhaConstrucoes", "#SerraConstrucaoCivil", "#EngenhariaSerra", "#ObrasSerra", "#ConstrutoraSerra", "#SerraConstrucoes", "#ConstruindoSerra", "#ConstrucaoCivilES", "#EngenhariaES",
            "#ConstrucaoResidencialVitoria", "#EngenhariaEstruturalVitoria", "#ReformaVitoria", "#ObrasPublicasVitoria", "#ConstrutoraES", "#ObrasIndustriaisVitoria", "#ConstrucaoComercialVitoria", "#ProjetosES", "#ArquiteturaVitoria", "#EngenhariaCivilLinhares", "#ConstrucoesSustentaveisLinhares", "#ObrasLinharesES", "#ResidencialLinhares", "#ConstrucaoRuralLinhares", "#ReformaLinhares", "#ProjetosCariacica", "#ConstrucaoSustentavelCariacica", "#ReformaCariacica", "#EngenhariaCariacicaES", "#ProjetosSerra", "#ConstrucaoSerraES", "#ObrasSerra", "#ResidencialSerra", "#ConstrutoraLinharesES", "#EngenhariaVilaVelha", "#ProjetosVilaVelha", "#ReformaVilaVelha", "#ConstrucoesVilaVelha", "#ObrasVilaVelhaES", "#ResidencialVilaVelha", "#ConstrucaoIndustrialES",
            "#brasilia", "#asaSul", "#asaNorte", "#noroeste", "#sudoeste", "#lagosul", "#lagonorte", "#guara", "#taguatinga", "#ceilandia", "#samambaia", "#recantodasemanha", "#riachofundo", "#riachofundo2", "#aguasclaras", "#vicentepires", "#nucleoBandeirante", "#paranoá", "#sobradinho", "#sobradinho2", "#planaltina", "#cruzeiro", "#candangolandia", "#estrutural", "#brazlandia", "#gama", "#santaMaria", "#jardimbotanico", "#itapoa", "#varjao",
            "#vectra", "#celta", "#corsa", "#corsaSedan", "#classic", "#kadett", "#omega", "#monza", "#chevette", "#agile", "#meriva", "#zafira", "#astra", "#blazerantiga", "#s10cabinesimples",
            "#onix", "#onixplus", "#tracker", "#s10", "#montana", "#spin", "#cruze", "#cruzehatch", "#cobalt", "#joy", "#joyplus", "#trailblazer", "#camaro", "#equinox", "#blazer",
            "#jardimcamburi", "#praiadacosta", "#itabapoana", "#bairroindustrial", "#soteco", "#residencialcoqueiral", "#santamarinha", "#centrovitoria", "#ilhasdasflores", "#jardimamerica", "#santoinacio", "#andorinhas", "#resistência", "#maruípe", "#ilhaodosayal", "#novaalbion", "#santoluiz", "#santahelena", "#consolação", "#boaavista", "#soteco", "#ilhaodosbentos", "#saojorge", "#redençãocariacica", "#ariovaldofavalessa", "#universitario", "#mucurici", "#grandevictoria",
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
                                        "#fundãovisual", "#fundãoreels", "#fundãoshorts"
                                        "#marechalflorianovisual", "#marechalflorianoreels", "#marechalflorianoshorts",
                                        "#joãoneivavisual", "#joãoneivareels", "#joãoneivashorts"
                                        "#alfredochavesvisual", "#alfredochavesreels", "#alfredochavesshorts",
                                        "#muquivisual", "#muquireels", "#muquishorts"
                                        "#vilavaleriovisual", "#vilavalerioreels", "#vilavaleriashorts",
                                        "#irupivisual", "#irupireels", "#irupishorts",
                                        "#presidentekennedyvisual", "#presidentekennedyreels", "#presidentekennedysorts"
                                        "#boaesperançavisual", "#boaesperançareels", "#boaesperançashorts",
                                        "#itaguaçúvisual", "#itaguaçúreels", "#itaguaçúshorts",
                                        "#santaleopoldinavisual", "#santaleopoldinareels", "#santaleopoldinashorts",
                                        "#brejetubavisual", "#brejetubareels", "#brejetubashorts",
                                        "#marilándiavísual", "#marilándiareels", "#marilándiashorts",
                                        "#comidavisual", "#comidareels", "#comidashorts", "#gastronomiavisual", "#gastronomiareels", "#gastronomiashorts", "#culináriavisual", "#culináriareels", "#culináriashorts", "#docesvisuais", "#docesreels", "#docesshorts", "#salgadosvisuais", "#salgadosreels", "#salgadosshorts", "#padariavisual", "#padariareels", "#padariashorts", "#restaurantevisual", "#restaurantereels", "#restauranteshorts", "#chefvisual", "#chefreels", "#chefshorts", "#cozinhavisual", "#cozinhareels", "#cozinhashorts",
                                        "#ruaalankardec", "#ruamoema", "#ruasaogabriel", "#ruagetuliofreirenunes", "#ruaanitagaribaldi", "#ruadocoqueiro", "#ruamiracema", "#avenidalucianodasneves", "#ruavenus", "#ruaveracruz", "#ruarepublica", "#ruafloresta", "#avenidacarloslindenberg", "#rua7dejunho",
                                        "#avenidacarloslindenberg", "#rua7dejunho", "#linhares", "#linhareses", "#linhares_city", "#linhareseorigem", "#capixaba", "#espiritosanto", "#amorporlinhares", "#linhares_amor", "#turismolinhares", "#vivernalinhares", "#riobananal", "#sooretama", "#aguasdelinhares", "#linhares_beach", "#linhares_lindoo", "#capixabaes", "#praiasdelinhares", "#naturezadelinhares", "#cidadeverde", "#linhares2025", "#esbeleza", "#es_cultura", "#capixabando", "#maravilhasdoes", "#turismoes", "#cariacica", "#vitoriaes", "#espiritosantobrazil", "#linharesoficial", "#linharesmais", "#naturezaes", "#esnatural", "#espaulinho", "#cidadeecologica", "#linharesnaterra", "#meulinhares", "#naturezacapixaba", "#capixabamais", "#linharespraia", "#linharesart", "#linharesfood", "#linhareslovers", "#linhareslife", "#linhares2024", "#esverde", "#esclima", "#capixabapaisagem", "#linharescity", "#turismolinhares", "#capixabaprofundo", "#linharesnatural", "#capixabaflora", "#linharesnoticias", "#linharesdiario", "#linharesdivulga", "#linharescultura", "#linharesfestas", "#linharesnoite", "#linharesdesucesso", "#linharesfotos", "#linharescomamor", "#linharespraias", "#linharesverde", "#linharesparaiso", "#linharesdesert", "#linharescentro", "#linharesbahia", "#linharescomida", "#linharescidade", "#linharesamizade",




        ]

        propaganda = [
            "💻 VPS Rápido, Seguro e Barato -> https://filmeseserie.com.br/vps.html  Desempenho estável, segurança garantida e preços acessíveis! contato whatsapp 📲 Fale agora no WhatsApp:27 99986-0405",
            "💻 VPS Rápido, Seguro e Barato -> https://www.espiritosanto-es.com.br/vps.html  Desempenho estável, segurança garantida e preços acessíveis! contato whatsapp 📲 Fale agora no WhatsApp:27 99986-0405",
            "PRECISA DE CRÉDITO PESSOAL TA AQUI A SOLUÇÃO -> https://geocredibnkvitoria.com/ "
            "Telefone: (27) 99726-9454   Agência de intermediação entre você e os bancos, em busca de juros baixo e soluções financeiras, empréstimos, financiamentos, .."
            "A Geo Credi BNK Vitória é uma agência de intermediação entre você e os bancos, em busca de juros baixo e soluções financeiras, empréstimos, financiamentos, Endereço: Av. Jerônimo Monteiro, 685 - Centro, Vitória - ES, 29010-003 \n"
            "A Geo Credi BNK Vitória é uma agência de intermediação entre você e os bancos\n  juros baixo e soluções financeiras, empréstimos, financiamentos, Empréstimo INSS/servidor/pessoal/PJ \nSaque FGTS Financiamento/\nConsórcio Seguro",
            "Empréstimo INSS/servidor/pessoal/PJ Saque FGTS Financiamento/\nConsórcio Seguro\n A Geo Credi BNK Vitória é uma agência de intermediação entre você e os bancos, em busca de juros baixo e soluções financeiras, empréstimos, financiamentos, Endereço: Av. Jerônimo Monteiro, 685 - Centro, Vitória - ES, 29010-003",
            "Solicite sua cotação de seguros, consórcios e muito mais! Atendimento com todas as seguradoras. 📞 (27) 99949-7001 CONTATO:",
            "A Geo Credi BNK Vitória é uma agência de intermediação entre você e os bancos(27) 99726-9454 WhatsApp  Endereço: Av. Jerônimo Monteiro, 685 - Centro, Vitória - ES, 29010-003",
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

            page.goto('https://www.youtube.com/results?search_query=silver+gameplay+dreamcast')
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
   
