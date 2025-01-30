
from  Unidad_1 import Class_Optimization_SumOfSquares as opt

if __name__ == "__main__":
    minv = -10
    maxv = 10
    n = 5
    obj = opt.opt_sum_of_squares(minv, maxv)
    pop = obj.create_population(5,4)
    print("Pop:")
    for indv in pop:
        print(indv)
    parents = obj._get_parents(2, pop)
    print("\nParents:")
    for parent in parents:
        print(parent)
