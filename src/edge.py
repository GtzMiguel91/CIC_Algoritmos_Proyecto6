from random import randint


class Edge:

    def __init__(self, id, source, target):
        """
        Constructor
        :param source: source node
        :param target: target node
        :param id: edge id
        """
        self.source = source
        self.target = target
        self.id = id
        # atributos
        self.attr = {
            # peso random que tendra la arista de 1-30
            "weight": randint(1, 30),
            # auxiliar pygame
            "colour": (0,255,0)
        }

    def __str__(self):
        """
        convert edge to str
        :return: edge textual representation
        """
        return str(self.id)
