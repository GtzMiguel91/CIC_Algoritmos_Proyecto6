import random


class Node:
    def __init__(self, id):
        """
        Constructor
        :param id: node identifier
        """
        #Auxiliares pygame
        self._weight = 990
        self._height = 590
        self._colors = {
            "RED": (255, 0, 0),
            "FUCHSIA": (255, 0, 255),
            "BLUE": (0, 0, 255),
            "YELLOW": (255, 255, 0),
            "CYAN": (0, 255, 255),
            "PURPLE": (202, 113, 219)
        }
        self.id = id
        self.attr = {
            "edges": [],
            "neighbors": [],
            "geoX_Y": [],
            # Auxiliar para BFS
            "visitedBFS": False,
            # axiliares para DFS
            "visitedDFSI": False,
            "rootNodeDFSI": -1,
            # Auxiliares para algoritmo Dijkstra
            "parent": None,
            "distance": float('inf'),
            "edgeWeight": float('inf'),
            # Auxiliares para algoritmo KruskalD
            "setGroup": id,
            "rank": 0,
            # Auxiliares para algoritmo Prim
            "parentP": None,
            "distanceP": float('inf'),
            # Auxiliares para PyGame
            "pgX": random.randint(10, self._weight),
            "pgY": random.randint(10, self._height),
            "colour": random.choice(list(self._colors.values())),
        }

    def __str__(self):
        """
        Convert node to str
        """
        return str(self.id) + str(self.attr["neighbors"])
