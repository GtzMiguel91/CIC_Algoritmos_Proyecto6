import algorithms as a
from pygameGraficador import App


def execute_pyGame(app, graph, minDist):
    app.set_graph(graph)
    app.set_min_dist(minDist)
    app.on_execute()


def pyGame_ex():
    theApp = App()

    ######################100 NODOS##############################

    ###########Grafo ErdosRenyi############################
    grafoErdos = a.randomErdosRenyi(100, 100, directed=False, auto=False)
    execute_pyGame(theApp, grafoErdos, 20)

    #####################Grafo Gilbert ####################################
    grafoGilbert = a.randomGilbert(100, 0.1, directed=False, auto=False)
    execute_pyGame(theApp, grafoGilbert, 150)

    ####################Grafo Malla################################
    grafoMalla = a.gridGraph(10, 10, directed=False)
    execute_pyGame(theApp, grafoMalla, 15)

    ###########################Grafo Geografico#######################################
    grafoGeografico = a.randomGeografico(100, 0.3, directed=False, auto=False)
    execute_pyGame(theApp, grafoGeografico, 60)

    #####################Grafo DorogovtsevMendes################################
    grafoDorogovt = a.randomDorogovtsevMendes(n=100, directed=False)
    execute_pyGame(theApp, grafoDorogovt, 60)

    #####################Grafo BarabasiAlbert###############################
    grafoBarabasiAlbert = a.randomBarabasiAlbert(100, 5, directed=False, auto=False)
    execute_pyGame(theApp, grafoBarabasiAlbert, 60)




    ######################500 NODOS##############################
    ###########Grafo ErdosRenyi############################
    grafoErdos = a.randomErdosRenyi(500, 600, directed=False, auto=False)
    execute_pyGame(theApp, grafoErdos, 40)

    #####################Grafo Gilbert ####################################
    grafoGilbert = a.randomGilbert(500, 0.1, directed=False, auto=False)
    execute_pyGame(theApp, grafoGilbert, 150)

    #####################Grafo Malla################################
    grafoMalla = a.gridGraph(22, 23, directed=False)
    execute_pyGame(theApp, grafoMalla, 10)

    ###########################Grafo Geografico#######################################
    grafoGeografico = a.randomGeografico(500, 0.08, directed=False, auto=False)
    execute_pyGame(theApp, grafoGeografico, 60)

    #####################Grafo DorogovtsevMendes################################
    grafoDorogovt = a.randomDorogovtsevMendes(n=500, directed=False)
    execute_pyGame(theApp, grafoDorogovt, 60)

    #####################Grafo BarabasiAlbert###############################
    grafoBarabasiAlbert = a.randomBarabasiAlbert(500, 4, directed=False, auto=False)
    execute_pyGame(theApp, grafoBarabasiAlbert, 20)

