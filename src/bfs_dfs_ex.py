import algorithms as a


def bfs_dfs_examples():
        rootNode=5

        ###########Grafo ErdosRenyi############################
        #Grafo ErdosRenyi de 30 nodos
        grafoErdos=a.randomErdosRenyi(30, 50, directed=False, auto=False)
        grafoErdos.saveGV()
        grafoErdosBFS=grafoErdos.BFS(rootNode)
        grafoErdosBFS.saveGV()
        grafoErdosDFS=grafoErdos.DFS_I(rootNode)
        grafoErdosDFS.saveGV()
        grafoErdosDFSR=grafoErdos.DFS_R(rootNode)
        grafoErdosDFSR.saveGV()

        #Grafo ErdosRenyi de 100 nodos
        grafoErdos=a.randomErdosRenyi(100, 200, directed=False, auto=False)
        grafoErdos.saveGV()
        grafoErdosBFS=grafoErdos.BFS(rootNode)
        grafoErdosBFS.saveGV()
        grafoErdosDFS=grafoErdos.DFS_I(rootNode)
        grafoErdosDFS.saveGV()
        grafoErdosDFSR=grafoErdos.DFS_R(rootNode)
        grafoErdosDFSR.saveGV()
        

        #Grafo ErdosRenyi de 500 nodos
        grafoErdos=a.randomErdosRenyi(500, 700, directed=False, auto=False)
        grafoErdos.saveGV()
        grafoErdosBFS=grafoErdos.BFS(rootNode)
        grafoErdosBFS.saveGV()
        grafoErdosDFS=grafoErdos.DFS_I(rootNode)
        grafoErdosDFS.saveGV()
        grafoErdosDFSR=grafoErdos.DFS_R(rootNode)
        grafoErdosDFSR.saveGV()


        #####################Grafo Gilbert ####################################

        #Grafo Gilbert de 30 nodos
        grafoGilbert=a.randomGilbert(30, 0.4, directed=False, auto=False)
        grafoGilbert.saveGV()
        grafoGilbertBFS=grafoGilbert.BFS(rootNode)
        grafoGilbertBFS.saveGV()
        grafoGilbertDFS=grafoGilbert.DFS_I(rootNode)
        grafoGilbertDFS.saveGV()
        grafoGilbertDFSR=grafoGilbert.DFS_R(rootNode)
        grafoGilbertDFSR.saveGV()

        #Grafo Gilbert de 100 nodos
        grafoGilbert=a.randomGilbert(100, 0.2, directed=False, auto=False)
        grafoGilbert.saveGV()
        grafoGilbertBFS=grafoGilbert.BFS(rootNode)
        grafoGilbertBFS.saveGV()
        grafoGilbertDFS=grafoGilbert.DFS_I(rootNode)
        grafoGilbertDFS.saveGV()
        grafoGilbertDFSR=grafoGilbert.DFS_R(rootNode)
        grafoGilbertDFSR.saveGV()

        #Grafo Gilbert de 500 nodos
        grafoGilbert=a.randomGilbert(500, 0.2, directed=False, auto=False)
        grafoGilbert.saveGV()
        grafoGilbertBFS=grafoGilbert.BFS(rootNode)
        grafoGilbertBFS.saveGV()
        grafoGilbertDFS=grafoGilbert.DFS_I(rootNode)
        grafoGilbertDFS.saveGV()
        grafoGilbertDFSR=grafoGilbert.DFS_R(rootNode)
        grafoGilbertDFSR.saveGV()


        #####################Grafo Malla################################

        #Grafo Malla de 30 nodos
        grafoMalla=a.gridGraph(10,3,directed=False)
        grafoMalla.saveGV()
        grafoMallaBFS=grafoMalla.BFS(rootNode)
        grafoMallaBFS.saveGV()
        grafoMallaDFS=grafoMalla.DFS_I(rootNode)
        grafoMallaDFS.saveGV()
        grafoMallaDFSR=grafoMalla.DFS_R(rootNode)
        grafoMallaDFSR.saveGV()

        #Grafo Malla de 100 nodos
        grafoMalla=a.gridGraph(10,10,directed=False)
        grafoMalla.saveGV()
        grafoMallaBFS=grafoMalla.BFS(rootNode)
        grafoMallaBFS.saveGV()
        grafoMallaDFS=grafoMalla.DFS_I(rootNode)
        grafoMallaDFS.saveGV()
        grafoMallaDFSR=grafoMalla.DFS_R(rootNode)
        grafoMallaDFSR.saveGV()
        
        
        #Grafo Malla de 500 nodos
        grafoMalla=a.gridGraph(20,25,directed=False)
        grafoMalla.saveGV()
        grafoMallaBFS=grafoMalla.BFS(rootNode)
        grafoMallaBFS.saveGV()
        grafoMallaDFS=grafoMalla.DFS_I(rootNode)
        grafoMallaDFS.saveGV()
        grafoMallaDFSR=grafoMalla.DFS_R(rootNode)
        grafoMallaDFSR.saveGV()

        ###########################Grafo Geografico#######################################

        #Grafo Geografico de 30 nodos
        grafoGeografico=a.randomGeografico(30, 0.5, directed=False, auto=False)
        grafoGeografico.saveGV()
        grafoGeograficoBFS=grafoGeografico.BFS(rootNode)
        grafoGeograficoBFS.saveGV()
        grafoGeograficoDFS=grafoGeografico.DFS_I(rootNode)
        grafoGeograficoDFS.saveGV()
        grafoGeograficoDFSR=grafoGeografico.DFS_R(rootNode)
        grafoGeograficoDFSR.saveGV()

        #Grafo Geografico de 100 nodos
        grafoGeografico=a.randomGeografico(100, 0.3, directed=False, auto=False)
        grafoGeografico.saveGV()
        grafoGeograficoBFS=grafoGeografico.BFS(rootNode)
        grafoGeograficoBFS.saveGV()
        grafoGeograficoDFS=grafoGeografico.DFS_I(rootNode)
        grafoGeograficoDFS.saveGV()
        grafoGeograficoDFSR=grafoGeografico.DFS_R(rootNode)
        grafoGeograficoDFSR.saveGV()


        #Grafo Geografico de 500 nodos
        grafoGeografico=a.randomGeografico(500, 0.1, directed=False, auto=False)
        grafoGeografico.saveGV()
        grafoGeograficoBFS=grafoGeografico.BFS(rootNode)
        grafoGeograficoBFS.saveGV()
        grafoGeograficoDFS=grafoGeografico.DFS_I(rootNode)
        grafoGeograficoDFS.saveGV()
        grafoGeograficoDFSR=grafoGeografico.DFS_R(rootNode)
        grafoGeograficoDFSR.saveGV()


        #####################Grafo BarabasiAlbert################################
        
        #Grafo BarabasiAlbert de 30 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(30, 5, directed=False, auto=False)
        grafoBarabasiAlbert.saveGV()
        grafoBarabasiAlbertBFS=grafoBarabasiAlbert.BFS(rootNode)
        grafoBarabasiAlbertBFS.saveGV()
        grafoBarabasiAlbertDFS=grafoBarabasiAlbert.DFS_I(rootNode)
        grafoBarabasiAlbertDFS.saveGV()
        grafoBarabasiAlbertDFSR=grafoBarabasiAlbert.DFS_R(rootNode)
        grafoBarabasiAlbertDFSR.saveGV()

    
        #Grafo BarabasiAlbert de 100 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(100, 3, directed=False, auto=False)
        grafoBarabasiAlbert.saveGV()
        grafoBarabasiAlbertBFS=grafoBarabasiAlbert.BFS(rootNode)
        grafoBarabasiAlbertBFS.saveGV()
        grafoBarabasiAlbertDFS=grafoBarabasiAlbert.DFS_I(rootNode)
        grafoBarabasiAlbertDFS.saveGV()
        grafoBarabasiAlbertDFSR=grafoBarabasiAlbert.DFS_R(rootNode)
        grafoBarabasiAlbertDFSR.saveGV()
        #Grafo BarabasiAlbert de 500 nodos
        grafoBarabasiAlbert= a.randomBarabasiAlbert(500, 2, directed=False, auto=False)
        grafoBarabasiAlbert.saveGV()
        grafoBarabasiAlbertBFS=grafoBarabasiAlbert.BFS(rootNode)
        grafoBarabasiAlbertBFS.saveGV()
        grafoBarabasiAlbertDFS=grafoBarabasiAlbert.DFS_I(rootNode)
        grafoBarabasiAlbertDFS.saveGV()
        grafoBarabasiAlbertDFSR=grafoBarabasiAlbert.DFS_R(rootNode)
        grafoBarabasiAlbertDFSR.saveGV()

        #####################Grafo DorogovtsevMendes################################

        #Grafo DorogovtsevMendes de 30 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=30, directed=False)
        grafoDorogovt.saveGV()
        grafoDorogovtBFS=grafoDorogovt.BFS(rootNode)
        grafoDorogovtBFS.saveGV()
        grafoDorogovtDFS=grafoDorogovt.DFS_I(rootNode)
        grafoDorogovtDFS.saveGV()
        grafoDorogovtDFSR=grafoDorogovt.DFS_R(rootNode)
        grafoDorogovtDFSR.saveGV()
        #Grafo DorogovtsevMendes de 100 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=100, directed=False)
        grafoDorogovt.saveGV()
        grafoDorogovtBFS=grafoDorogovt.BFS(rootNode)
        grafoDorogovtBFS.saveGV()
        grafoDorogovtDFS=grafoDorogovt.DFS_I(rootNode)
        grafoDorogovtDFS.saveGV()
        grafoDorogovtDFSR=grafoDorogovt.DFS_R(rootNode)
        grafoDorogovtDFSR.saveGV()
        #Grafo DorogovtsevMendes de 500 nodos
        grafoDorogovt= a.randomDorogovtsevMendes(n=500, directed=False)
        grafoDorogovt.saveGV()
        grafoDorogovtBFS=grafoDorogovt.BFS(rootNode)
        grafoDorogovtBFS.saveGV()
        grafoDorogovtDFS=grafoDorogovt.DFS_I(rootNode)
        grafoDorogovtDFS.saveGV()
        grafoDorogovtDFSR=grafoDorogovt.DFS_R(rootNode)
        grafoDorogovtDFSR.saveGV()

        return