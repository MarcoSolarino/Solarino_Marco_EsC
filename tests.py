import ChainedHash as Ch
import random
import LinearHash as Lh
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def plot_function(v, N, stringa):
    plt.ylabel("collisioni")
    plt.xlabel("alpha")
    plt.plot(N, v, label=stringa)
    plt.grid()
    plt.legend()
    plt.show()


def plot_comparison(v1, v2, N):
    plt.ylabel("collisioni")
    plt.xlabel("alpha")
    plt.plot(N, v1, label="Chained Hash")
    plt.plot(N, v2, label="Linear Hash")
    plt.grid()
    plt.legend()
    plt.show()


def generate_vector(n):
    vector = []
    for i in range(n):
        vector.append(i*10**3)
    random.shuffle(vector)
    return vector


def random_vector(n):
    vector = []
    for i in range(n):
        vector.append(random.randint(10**3, 10**5))
    return vector


def generate_mean(matrix):
    v = []
    for j in range(len(matrix[0])):
        mean = 0
        for i in range(len(matrix)):
            mean += matrix[i][j]
        mean = mean/len(matrix)
        v.append(mean)
    return v

'''
def test_chsearch():   # testo la ricerca con un fattore di caricamento alpha = n/m
    esplorazioni = []
    for i in range(100, 1000, passo):
        vector = random_vector(i - 1)
        vector.append(0)
        random.shuffle(vector)
        chained = Ch.ChainedHash(1000)
        for x in vector:
            chained.insert(x)
        esplorazioni.append(chained.chained_search(0))
    return esplorazioni
'''

def test_chdelete(n):  # testo la cancellazione
    times = []
    return times

'''
def test_lnsearch():
    esplorazioni = []
    for i in range(100, 1000, passo):
        linear = Lh.LinearHash(1000)
        vector = random_vector(i - 1)
        vector.append(0)
        random.shuffle(vector)
        for x in vector:
            linear.linear_insert(x)
        esplorazioni.append(linear.linear_search(0))
    return esplorazioni
'''

def test_lndelete(n):
    times = []
    return times


def test_chsearch():
    times = []
    for i in range(100, 10**4, 100):
        chained = Ch.ChainedHash(10000)
        element = random.randint(0, 1000)
        vector = random_vector(i - 1)
        random.shuffle(vector)
        for x in vector:
            chained.insert(x)
        init = timer()
        chained.chained_search(element)
        times.append(timer() - init)
    return times


def test_lnsearch():
    times = []
    for i in range(100, 10**4, 100):
        linear = Lh.LinearHash(10000)
        element = random.randint(0, 1000)
        vector = random_vector(i - 1)
        random.shuffle(vector)
        for x in vector:
            linear.linear_insert(x)
        init = timer()
        linear.linear_search(element)
        times.append(timer() - init)

    return times


def test_chcollision():
    collisions = []
    for i in range(1, 1000, 10):
        v = random_vector(i)
        chained = Ch.ChainedHash(1000)
        for x in v:
            chained.insert(x)
        chained.calculate_collision()
        collisions.append(chained.collision)
    return collisions


def test_lncollision():
    collisions = []
    for i in range(1, 1000, 10):
        v = random_vector(i)
        linear = Lh.LinearHash(1000)
        for x in v:
            linear.linear_insert(x)
        collisions.append(linear.collision)
    return collisions


def test_chlistlength():
    l = []
    for i in range(0, 30):
        l.append(i)
    n_matrix = []
    for itr in range(100):
        vector = random_vector(10**4)
        chained = Ch.ChainedHash(10**3)
        for x in vector:
            chained.insert(x)
        N = []
        for i in range(0, 30):
            percentual = 0
            for y in range(10**3):
                if len(chained.hash[y]) == i:
                    percentual += 1
            percentual = percentual/10**3
            N.append(percentual)
        n_matrix.append(N)
    nmean = generate_mean(n_matrix)
    plt.plot(l, nmean)
    plt.show()


# Here comes the tests dudududu


iterazioni = 100  # setto la precisione dei test
chained_matrix = []
linear_matrix = []

test_chlistlength()
for itr in range(iterazioni):
    print(itr, "di", iterazioni)
    #chained_matrix.append(test_chcollision())
    #linear_matrix.append(test_lncollision())
    #chained_matrix.append(test_chdelete(chainedn))
    #linear_matrix.append(test_lndelete(linearn))
    linear_matrix.append(test_lnsearch())
    chained_matrix.append(test_chsearch())


# calcolo le medie

chained_mean = generate_mean(chained_matrix)
linear_mean = generate_mean(linear_matrix)

Nc = []
for i in range(100, 10**4, 100):
    Nc.append(i / 10000)

Nl = []
for i in range(100, 10**4, 100):
    Nl.append(i / 10000)

plot_function(chained_mean, Nc, "Chained Hash")
#plot_function(linear_mean, Nl, "Linear Hash")
plot_comparison(chained_mean, linear_mean, Nc)
