from population import Population
import tkinter as tk
from window import Window
import math


def init():
    target_phrase = "An algorithm must be seen to be believed"
    mutation_rate = 0.01
    pop_size = 100
    population = Population(target_phrase, mutation_rate, pop_size)
    return population


def evolve(population, display):
    """Evolve from random string to target phrase"""
    while(not population.evolved):

        # Generate parents array
        population.selection()

        # Create next generation
        population.next_generation()

        # Calculate fitness score for every member of the population
        population.calculate_fitness()

        # Find the best phrase and check that we find target phrase
        population.evaluate()

        # Display population information in the window
        best_phrase = population.best_phrase
        gen = str(population.generations)
        avg_fit = str(round(population.get_average_fitness(), 3))
        pop_size = str(population.population_size)
        mutation_rate = str(math.floor(population.mutation_rate * 100))
        all_phrases = population.all_phrases()
        display.update_info(
            best_phrase, gen, avg_fit, pop_size, mutation_rate, all_phrases)

        print(population)


def main():
    mainWindow = tk.Tk()
    display = Window(mainWindow)

    population = init()
    evolve(population, display)

    mainWindow.mainloop()

if __name__ == "__main__":
    main()
