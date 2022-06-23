# importar librerias
import math
import pygame


class App:
    def __init__(self):
        # inicializacion de auxiliares del programa
        self.algorithm = 'springs'
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1000, 600
        self._clock = pygame.time.Clock()
        self._icon = pygame.image.load('flow.png')
        self._fps = 60
        self._graph = None
        self._nodeR = 4
        self._minDist = 15
        self._c = 0.001
        self._c1 = 3.5
        self._c2 = 0.01
        self._c3 = 0.33
        self._c4 = 0.08
        self._area = self.weight * self.height

    # funcion para inicializar pygame
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Proyecto5 - " + self._graph.id)
        pygame.display.set_icon(self._icon)
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self._running = True

    # funcion para salir de pygame en caso que usuario presione el boton de salir,
    # tambien si se maximiza la ventana, actualizar
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.VIDEORESIZE:
            self._display_surf = pygame.display.set_mode(event.dict['size'],
                                                         pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            self._display_surf.blit(pygame.transform.scale(self._display_surf, event.dict['size']), (0, 0))
            self.weight, self.height = self._display_surf.get_size()
            pygame.display.flip()

    def on_loop(self):
        # calculo de los resortes
        if self.algorithm == 'springs':
            self._spring_calculation()
        # algoritmo fruchterman reginold
        elif self.algorithm == 'fruchterman reginold':
            self._fruchterman_reginold()

    # se renderizan nodos y aristas.
    def on_render(self):
        # background negro
        self._display_surf.fill((0, 0, 0))

        # renderizar todas las aristas
        for key, edge in self._graph.edges.items():
            pygame.draw.line(self._display_surf, edge.attr["colour"],
                             (edge.source.attr["pgX"], edge.source.attr["pgY"]),
                             (edge.target.attr["pgX"], edge.target.attr["pgY"]))

        # renderizar todos los nodos
        for key, node in self._graph.nodes.items():
            center = (round(node.attr["pgX"]), round(node.attr["pgY"]))
            pygame.draw.circle(self._display_surf, node.attr["colour"],
                               center,
                               self._nodeR)
        # actualizar ventana
        pygame.display.flip()

    # salir de pygame
    def on_cleanup(self):
        pygame.quit()

    # ejecucion de pygame
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        # mientras el usuario no salga de pygame mandar a llamar las funciones
        while self._running:
            # para alcanzar a ver el movimiento de nodos y aristas
            self._clock.tick(self._fps)

            # para checar que presiona el usuario, salir o maximizar ventana
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    # grafica a renderizar
    def set_graph(self, graph):
        self._graph = graph

    # minimaDistancia puesta por el usuario
    def set_min_dist(self, value):
        self._minDist = value

    # algoritmo a usar
    def set_algoritmo(self, algorithm):
        self.algorithm = algorithm

    # calcular distancia entre nodos
    def _distance_n1_n2(self, node1, node2):
        # print("nodo1")
        # print(node1.attr["pgX"])
        # print("nodo2")
        # print(node2.attr["pgX"])
        return math.sqrt((node2.attr["pgX"] - node1.attr["pgX"]) ** 2 + (
                node2.attr["pgY"] - node1.attr["pgY"]) ** 2)

    # calcular angulo en radianes
    def _forces_x_y(self, node1, node2, force):
        radians = math.atan2(node2.attr["pgY"] - node1.attr["pgY"],
                             node2.attr["pgX"] - node1.attr["pgX"])

        return round(force * math.cos(radians), 2), round(force * math.sin(radians), 2)

    # calculo de resortes
    def _spring_calculation(self):
        nodes = self._graph.nodes.items()
        for key, node in nodes:
            neighbors = node.attr["neighbors"]
            fx = 0
            fy = 0

            for key2, node2 in nodes:
                if not node2.id == node.id:
                    # si el nodo2 esta en los vecinos del nodo, calcular fuerza de atraccion
                    if node2 in neighbors:
                        # Fuerza de atraccion
                        d = self._distance_n1_n2(node, node2)
                        # si distancia mayor que la minDista, caclcular fuerzas
                        if d > self._minDist:
                            force = self._c1 * math.log(d / self._c2)
                            fx2, fy2 = self._forces_x_y(node, node2, force)
                            fx += fx2
                            fy += fy2
                    else:
                        # Fuerza de repulsion
                        d = self._distance_n1_n2(node, node2)
                        # Si distancia es igual a cero, saltar calculo de fuerzas si no, realizarlo
                        if d == 0:
                            continue
                        force = self._c3 / math.sqrt(d)
                        fx2, fy2 = self._forces_x_y(node, node2, force)
                        fx -= fx2
                        fy -= fy2

            # Actualizar coordenadas
            node.attr["pgX"] += self._c4 * fx
            node.attr["pgY"] += self._c4 * fy

    def _fruchterman_reginold(self):
        C = 1
        temp = 1
        k = C * math.sqrt(self._area / self._graph.getTotalNodes())

        nodes = self._graph.nodes.items()
        for key, node in nodes:
            neighbors = node.attr["neighbors"]
            fx = 0
            fy = 0

            for key2, node2 in nodes:
                if node.id == node2.id:
                    continue

                d = self._distance_n1_n2(node, node2)
                if d == 0:
                    continue

                force = (d / abs(d)) * (k ** 2) / d
                fx2, fy2 = self._forces_x_y(node, node2, force)
                fx -= fx2
                fy -= fy2

                if node2 in neighbors:
                    d = self._distance_n1_n2(node, node2)
                    if d < 30:
                        continue

                    force = (d / abs(d)) * (d ** 2)/k
                    fx2, fy2 = self._forces_x_y(node, node2, force)
                    fx += fx2
                    fy += fy2

            # Actualizar coordenadas
            node.attr["pgX"] += self._c * fx
            node.attr["pgY"] += self._c * fy
