from collections import namedtuple
from functools import wraps
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
from services import ReadService, CleanService, MarkovModel


class PerformanceTest:
    def setup(self):
        self.read_service = ReadService()
        self.results = []

    def time(func): 
        wraps(func)
        def wrapper(*args, **kwargs):
            point = namedtuple("point", "degree time")
            start = perf_counter()
            result = func(*args, **kwargs)
            time_elapsed = perf_counter() - start
            return point(kwargs.get("degree"), time_elapsed)
        return wrapper

    @time
    def test_time_performance(self, degree: int) -> None:
        self.read_service.text = self.read_service.available_stories[0]
        clean_service = CleanService(self.read_service.text)
        markov_model = MarkovModel(clean_service.clean_text, degree)
        return markov_model.model

    def run_tests(self):
        for i in range(1, 21):
            point = self.test_time_performance(degree=i)
            self.results.append(point)

    def plot_results(self):
        x = np.array([i.degree for i in self.results])
        y = np.array([i.time for i in self.results])

        plt.scatter(x, y)

        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)

        plt.plot(x, p(x))
        plt.show(block=False)
        plt.pause(15)
        plt.close()

if __name__ == "__main__":
    performance_test = PerformanceTest()
    performance_test.setup()
    performance_test.run_tests()
    performance_test.plot_results()