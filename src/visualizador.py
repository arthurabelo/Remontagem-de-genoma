# Exibição gráfica da composição

import os
import tkinter as tk
from tkinter import Canvas

class VisualizadorGrafoKmers:
    def __init__(self, fita):
        self.fita = fita
        self.nodes = {}
        self.edges = []
        self.node_positions = {}
        self.selected_node = None
        self.offset_x = 0
        self.offset_y = 0

    def kmers(self, seq, k):
        kmers = []
        if k > len(seq):
            return kmers
        for i in range(len(seq) - k + 1):
            kmers.append(seq[i:i+k])
        return kmers

    def criar_grafo(self, k):
        kmers = self.kmers(self.fita, k)
        for i in range(len(kmers) - 1):
            prefix = kmers[i][:-1]
            suffix = kmers[i+1][1:]
            if prefix not in self.nodes:
                self.nodes[prefix] = len(self.nodes)
            if suffix not in self.nodes:
                self.nodes[suffix] = len(self.nodes)
            self.edges.append((prefix, suffix))

    def exibir_grafo(self, k):
        self.criar_grafo(k)
        root = tk.Tk()
        root.title("Visualizador de Grafo de De Bruijn")
        canvas = Canvas(root, width=800, height=600, bg='white')
        canvas.pack()

        # Inicializar posições dos nós
        for node in self.nodes:
            self.node_positions[node] = (100 + 600 * (self.nodes[node] % 5) / 5, 100 + 400 * (self.nodes[node] // 5) / 5)

        # Desenhar arestas
        for edge in self.edges:
            x1, y1 = self.node_positions[edge[0]]
            x2, y2 = self.node_positions[edge[1]]
            canvas.create_line(x1, y1, x2, y2)

        # Desenhar nós
        for node, (x, y) in self.node_positions.items():
            oval = canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightblue')
            canvas.create_text(x, y, text=node)
            canvas.tag_bind(oval, '<ButtonPress-1>', self.on_node_press)
            canvas.tag_bind(oval, '<B1-Motion>', self.on_node_motion)

        self.canvas = canvas
        root.mainloop()

    def on_node_press(self, event):
        self.selected_node = event.widget.find_closest(event.x, event.y)[0]
        self.offset_x = event.x
        self.offset_y = event.y

    def on_node_motion(self, event):
        if self.selected_node:
            dx = event.x - self.offset_x
            dy = event.y - self.offset_y
            self.canvas.move(self.selected_node, dx, dy)
            self.offset_x = event.x
            self.offset_y = event.y