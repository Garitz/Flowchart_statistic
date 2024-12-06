import numpy as np

from Human import Human
from draw_diagram import plot


class VirusSimulation:
    def __init__(self, params):

        self.population_size = params["population"]
        self.contact_rate = params["contact_rate"]
        self.sick_at_start = params["sick_at_start"]
        self.days = params["days"]
        self.death_rate = params["death_rate"]
        self.vaccination_day = params["vaccination_day"]
        self.vaccinate_per_day = params["vaccinate_per_day"]
        self.have_been_vaccinated = 0

        self.population = []

        for i in range(self.population_size):
            h = Human()
            h.max_time_ill = params["max_time_ill"]
            h.set_status("i") if i < self.sick_at_start else None
            self.population.append(h)

        self.counter = [[self.population_size-self.sick_at_start, self.sick_at_start, 0, 0]]  # for s i r d
        self.run()

    def run(self):
        vaccinate = False
        for i in range(self.days):
            self.daily_cycle(vaccinate)
            if i%5 == 0:
                print("day:", i)
            if i == self.vaccination_day:
                vaccinate = True

        plot(self.counter)


    def daily_cycle(self, vaccinate=False):
        if vaccinate:
            counter = 0
            while counter < self.vaccinate_per_day:
                if self.have_been_vaccinated == self.population_size:
                    break
                j = np.random.randint(0, self.population_size)
                if not self.population[j].has_been_vaccinated:
                    self.population[j].has_been_vaccinated = True
                    counter += 1
                    self.have_been_vaccinated += 1


        for h in self.population:
            if h.status == "i":
                h.recovery_time -= 1
                if h.recovery_time == 0:
                    rnd = np.random.random()
                    if rnd < self.death_rate:
                        h.set_status("d")
                    else:
                        h.set_status("r")
            if h.sick_next_day:
                h.set_status("i")


        for i, h in enumerate(self.population):
            if h.status == "i":
                rnd = np.random.random()
                if rnd < self.contact_rate:  # tries to infect someone
                    j = np.random.randint(0, self.population_size)
                    while j == i:  # cant infect himself
                        j = np.random.randint(0, self.population_size)
                    self.population[j].has_been_infected()
        sus, inf, rec, dead = self.count()
        self.counter.append([sus, inf, rec, dead])

    def count(self):
        s, i , r, d = 0, 0, 0, 0

        for h in self.population:
            if h.status == "s":
                s += 1
            if h.status == "i":
                i += 1
            if h.status == "r":
                r += 1
            if h.status == "d":
                d += 1
        return s, i, r, d