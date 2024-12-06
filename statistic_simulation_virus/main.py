from VirusSimulator import VirusSimulation

if __name__ == '__main__':
    params = {"population": 100000,
              "contact_rate": 0.12,  # Wahrscheinlichkeit, dass jemand an einem bestimmten Tag angesteckt wird
              "sick_at_start": 100,
              "days": 220, # Länge der Simulation
              "death_rate": 0.048, # Wahrscheinlichkeit, dass vom kranken Zustand in den verstorbenen Zustand gegangen wird
              "death_rate_vaccinated": 0.024,  # Todesrate von geimpften
              "vaccination_day": 100,  # Tag, an dem geimpft wird
              "vaccinate_per_day": 0,  # Anzahl Impfungen pro Tagß
              "max_time_ill": 1  # Wie oft man erkranken kann
                 }

    VS = VirusSimulation(params)