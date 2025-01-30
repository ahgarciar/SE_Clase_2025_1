import random as rnd

class opt_sum_of_squares:
    def __init__(self, minv, maxv):
        self.__min = minv
        self.__max = maxv
        rnd.seed = 5

    def _create_solution(self, n):
        solution = [rnd.randint(self.__min, self.__max) for i in range(n)]
        return solution

    def _objetive_function(self, solution):
        obj_value = sum([i**2 for i in solution])
        return obj_value

    def create_population(self, m, n):
        population = [self._create_solution(n) for i in range(m)]
        return population

    def _get_parents(self, p, pop):  # binary tournament
        parents = []
        temp = len(pop)-1
        for i in range(p):
            idx1 = idx2 = rnd.randint(0, temp)
            while idx1 == idx2:
                idx2 = rnd.randint(0, temp)
            obj_val1 = self._objetive_function(pop[idx1])
            obj_val2 = self._objetive_function(pop[idx2])
            if obj_val1 < obj_val2:
                parents.append(pop[idx1][:]) # custom copy
            else:
                parents.append(pop[idx2][:])
        return parents