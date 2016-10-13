#! /usr/bin/env python

import random
import string
import time

WORD = "Corgi"
PELLO = 40


def create_individual(entry_point):
    ind = ""
    while len(ind) < 5:
        ind += entry_point[random.randint(0, len(entry_point) - 1)]
    return ind

def solution(generation):
    if len(generation) == 0:
        return False
    for individu in generation:
        if individu == WORD:
            return True
    return False


def score(string):
    i = 0
    final_score = 0;
    while i < len(string):
        if string[i] == WORD[i]:
            final_score += 1;
        i += 1;
    return final_score

def order_list(generation):
    score_data = {}
    ordered_generation = []
    print(generation)
    for individu in generation:
        score_data[individu] = score(individu)
    for data in score_data:
        if len(ordered_generation) <= 0:
            ordered_generation.append(score_data[data])

def random_wheel(generation):
    total_roulette = 0
    for ind in generation:
        print("Score : {}, Value : {}".format(float(score(ind) / (len(WORD) * 1.0)), ind))
        total_roulette += (score(ind) / (len(WORD) * 1.0))
    ran = random.randint(0, 1000)
    prev = 0
    for i in range(0, len(generation) - 2):
        if rand in range(prev, score(generation[i]) / (len(word) * 1.0) * 1000):
            return i
        prev = score(generation[i]) / (len(word) * 1.0) * 1000



def select_indiv(generation):
    r1 = random.randint(0, len(generation) / 2)
    r2 = random.randint(0, len(generation) / 2)
    #print(r1, r2)
    while r1 == r2:
        r2 = random.randint(0, len(generation) / 2)
    total_roulette = 0
    for ind in generation:
        print("Score : {}, Value : {}".format(float(score(ind) / (len(WORD) * 1.0)), ind))
        total_roulette += (score(ind) / (len(WORD) * 1.0))
    #Finish the roulette wheel
    return generation[r1], generation[r2]

def random_my_gen(length):
    number = length / 2;
    list_random = []
    while len(list_random) < number:
        list_random.append(random.randint(0, length - 1))
        list(set(list_random))
    return list_random

def offspring(generation):
    new_gen = []
    while len(new_gen) < PELLO:
        # Crossover
        selectOne, selectTwo = select_indiv(generation)
        print(selectOne, selectTwo)
        time.sleep(500/1000000.0)
        random_list = random_my_gen(len(selectOne))
        #print("RD LIST " + str(random_list))
        new_one = selectOne
        tmp = list(new_one)
        for item in random_list:
            tmp[item] = list(selectTwo)[item]
        new_one = "".join(tmp)
        #print("New one : {}".format(new_one))
        new_gen.append(new_one)
    return new_gen

def mutation(generation):
    for i in range(0, int(len(generation) / 10)):
        r = random.randint(0, len(generation) - 1)
        generation[r] = create_individual(string.ascii_letters)
        #print("mutate at {}  : ".format(r) + generation[r])
    return generation


def recorder(generation, number):
    with open("recorder", 'a') as f:
        max_rank = float(score(generation[0]) / (len(WORD) * 1.0))
        print max_rank, generation[0]
        mean = 0
        for elem in generation:
            mean += float(score(elem) / (len(WORD) * 1.0))
            print mean
        rmean = float(mean / (len(generation) * 1.0))
        f.write("{}:{}\n".format(number, rmean))

#if __name__ == "__main__":
#    old_gen = []
#    new_gen = []
#    print(score("Corgi"))
#    #Create a population
#    while len(old_gen) < PELLO:
#        old_gen.append(create_individual(string.ascii_letters))
#    list.sort(old_gen, key=score, reverse=True)
#    recorder(old_gen, 0)


if __name__ == "__main__":
    old_gen = []
    new_gen = []
    print(score("Corgi"))
    #Create a population
    while len(old_gen) < PELLO:
        old_gen.append(create_individual(string.ascii_letters))
    #print(old_gen)
    # TESTING ORDERING LIST
    #old_gen = ["REDgO","Worgi", "Geogi", "SSSSS"]
    ##  list.sort(test, key=score)
    ##  print(" qweqwe " + str(test))
    ##  order_list(old_gen)
    list.sort(old_gen, key=score, reverse=True)
    time.sleep(1)
    #while solution(new_gen) == False:
    for i in range(0, 20):
        recorder(old_gen, i)
        new_gen = offspring(old_gen)
        #print("---> " + str(old_gen))
        old_gen = mutation(old_gen)
        #print("===> " + str(old_gen))
        old_gen = new_gen
        new_gen = []
        list.sort(old_gen, key=score, reverse=True)
