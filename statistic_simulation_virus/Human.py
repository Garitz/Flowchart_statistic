import numpy as np
from constants import *

class Human:

    def __init__(self):
        self.status = "s" # or i or r or d
        self.sick_next_day = False
        self.recovery_time = -1
        self.was_already_sick = False
        self.max_time_ill = None  # wird im virussimulator
        self.times_already_ill = 0
        self.has_been_vaccinated = False

    def set_status(self, new_status):
        self.status = new_status
        self.sick_next_day = False
        if new_status == "i":
            if self.has_been_vaccinated and self.was_already_sick:
                self.recovery_time = int(get_normal_distribution(mean_vaccinated_and_sick, sigma_vaccinated_and_sick))
            if not self.has_been_vaccinated and self.was_already_sick:
                self.recovery_time = int(get_normal_distribution(mean_already_sick, sigma_already_sick))
            if self.has_been_vaccinated and not self.was_already_sick:
                self.recovery_time = int(get_normal_distribution(mean_vaccinated, sigma_vaccinated))
            if not self.has_been_vaccinated and not self.was_already_sick:
                self.recovery_time = int(get_normal_distribution(recoveryTimeMean, recoveryTimeSigma))
            self.recovery_time = 0 if self.recovery_time < 0 else self.recovery_time


    def has_been_infected(self):
        #if self.status == "s":
        if self.has_been_vaccinated:
            if np.random.random() < 0.5:
                return
        self.times_already_ill += 1
        if self.status == "r":
            self.was_already_sick = True
        if self.times_already_ill <= self.max_time_ill:
            self.sick_next_day = True
