import string
import random


def random_char():
    return random.choice(string.ascii_letters + " ")


class Chromosome():
    """A class represents a chromosome as an array of characters
    Class Methods:
        - convert chromosome into a string
        - calculate "fitness" score for each chromosome
        - combine one chromosome with another
        - mutate chromosome
    """
    def __init__(self, length):
        self.genes = []
        self.fitness = 0
        for i in range(length):
            self.genes.append(random_char())

    def __repr__(self):
        info = "\nGenes: " + "".join(self.genes)
        info += "\nFitness score: " + str(self.fitness)
        return info

    def __len__(self):
        return len(self.genes)

    def get_phrase(self):
        """Character array to string"""
        return "".join(self.genes)

    def calculate_fitness(self, target):
        """Calculate percent of correct characters"""
        score = 0
        for sgene, tgene in zip(self.genes, target):
            if sgene == tgene:
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        """Combine by taking part from one parent and part from another"""
        child = Chromosome(len(self.genes))
        midpoint = random.randint(1, len(self.genes))

        for i in range(len(self.genes)):
            if i < midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutationRate):
        """Replace with a new random character,
         based on a mutation probability
        """
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = random_char()
