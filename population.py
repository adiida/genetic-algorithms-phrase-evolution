from chromosome import Chromosome
import numpy as np
import math
import random


class Population():
    """A class to describe a population, where each member 
    is an instance of a chromosome object
    """
    def __init__(self, phrase, mutation_rate, pop_size):
        self.population_size = pop_size
        self.population = [] # List to store the current population
        self.population_fitness = [] # List to store fitness score for each member
        self.parents = [] # List from which we choose parents to create childs 
        self.probability = [] # Probability of each parent to be choosen
        self.generations = 0
        self.evolved = False # Are we finished evolving
        self.target_phrase = phrase
        self.mutation_rate = mutation_rate
        self.perfect_match_score = 1.0
        self.best_phrase = "" # The current phrase with highest fitness score

        for i in range(self.population_size):
            self.population.append(Chromosome(len(self.target_phrase)))

        self.calculate_fitness()

    def __repr__(self):
        info = "\nTotal generations: " + str(self.generations)
        info += "\nPopulation size: " + str(self.population_size)
        info += "\nAverage fitness: " + str(self.get_average_fitness())
        info += "\nMutation rate: "
        info += str(math.floor(self.mutation_rate * 100)) + "%"
        info += "\nBest phrase: " + self.best_phrase
        return info

    def calculate_fitness(self):
        """calculate fitness function for every chromosome in population"""
        self.population_fitness = []
        for member in self.population:
            member.calculate_fitness(self.target_phrase)
            self.population_fitness.append(member.fitness)

    def selection(self):
        """Create parents array and probability array
        each element (normilized probability based on fitness score)
        """
        self.parents = []
        self.probability = []
        max_fitness = max(self.population_fitness)
        total_fitness = 0.0

        # Based on fitness score calculate probability 
        # for each parent to be choosen:
        # a higher fitness score = higher probability to be picked as a parent
        # a lower fitness score = lower probability to be picked as a parent
        for member in self.population:
            if member.fitness > 0:
                self.parents.append(member)
                normalized_fitness = member.fitness / max_fitness
                self.probability.append(normalized_fitness)
                total_fitness += normalized_fitness

        for i in range(len(self.probability)):
            normalized_probability = self.probability[i] / total_fitness
            self.probability[i] = normalized_probability

    def next_generation(self):
        """Create a new generation using crossover and mutation on parents"""
        for i in range(self.population_size):
            parent_a = np.random.choice(self.parents, p=self.probability)
            parent_b = np.random.choice(self.parents, p=self.probability)
            child = parent_a.crossover(parent_b)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.generations += 1

    def evaluate(self):
        """Find the member with highest fitness score in the population"""
        best_fitness_score = 0.0
        index = 0
        for i, member in enumerate(self.population):
            if member.fitness > best_fitness_score:
                index = i
                best_fitness_score = member.fitness

        self.best_phrase = self.population[index].get_phrase()
        if best_fitness_score == self.perfect_match_score:
            self.evolved = True

    def get_average_fitness(self):
        """Compute average fitness score for the population"""
        total = 0
        for member in self.population:
            total += member.fitness
        return round(total / self.population_size, 3)

    def all_phrases(self):
        """Convert all members of population to string"""
        phrases = ""
        for member in self.population:
            phrases += member.get_phrase() + "\n"
        return phrases
