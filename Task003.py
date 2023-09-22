
def update_m(p_H, list_m, cases_P):
    if (cases_P == 'H'):
        return [p_H * list_m[i] for i in range(len(list_m))]
    elif (cases_P == 'T'):
        return [1 - (p_H * list_m[i]) for i in range(len(list_m))]

def bayes_function(list_m, list_pHm):
    a, b = 0.0, 0.0
    for i in range(len(list_m)):
        a += list_m[i] * list_pHm[i]
        b += list_pHm[i]
    return a/b

def start_pos():
    start_m = [0.1, 0.2, 0.4, 0.8, 0.9]
    #before starting discovery
    P_H = [sum(start_m)/len(start_m)]

    #starting discovery
    cases = ['H', 'H', 'H', 'T', 'H', 'T', 'H', 'H']

    for i in range(8): # Цикл та усі оновлення
        new_m = update_m(P_H[i], start_m, cases[i]) # оновлення списку p(m)
        P_H.append(round(bayes_function(start_m, new_m), 2)) # додавання p(H) у список
        start_m = new_m # оновлення даних p(m)
    return P_H[1:]

print(f'Answer or this task: {start_pos()}')

