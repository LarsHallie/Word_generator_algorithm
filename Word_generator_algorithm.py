import pandas as pd

list_of_words = pd.read_csv("C:/Users/lars.hallie/Documents/Projects/Data Science/Algorithms/List_of_words.csv")
list_of_words = list_of_words['Overview of words']

list_of_letter = pd.read_csv("C:/Users/lars.hallie/Documents/Projects/Data Science/Algorithms/List_of_letters.csv")
list_of_letter = list_of_letter['Letters']

list_of_words = [i for i in list_of_words if len(i) == 5]

list_of_numbers = list(range(5))

question = "_____"

for _ in range(10):

    #Calculate number of letters per letter
    dic = {}
    for x in list_of_numbers:
        dic.setdefault(x, [])
        for i in list_of_letter:
            dic[x].append(sum(1 for f in list_of_words if f[x] == i))

    #Get highest number per position of the word
    dic_1 = {}
    for x in list_of_numbers:
        ind = dic[x].index(max(dic[x]))
        let = list_of_letter[ind]
        val = max(dic[x])
        name = "{}{}".format(x, let)
        dic_1[name] = val
        if _ > 0 and x == position:
            dic_1[name] = dic_1[name] + bonus_point

        if _ > 0 and answer == "Y" and x == (position - 1):
            dic_1[name] = dic_1[name] + bonus_point

    highest_letter = str(max(dic_1, key=dic_1.get)[1])
    position = int(max(dic_1, key=dic_1.get)[0])

    #Question
    question_list = list(question)
    question_list[position] = highest_letter
    new_question = ''.join(question_list)
    print(new_question)
    print(dic_1)
    answer = input("Y/N? ")

    if answer == "Y":
        question = new_question
        list_of_numbers.remove(position)
        list_of_words = [i for i in list_of_words if i[position] == highest_letter]
        bonus_point = 1000
        print("let's continue with {}".format(question))
        print(len(list_of_words))

    if answer == "N":
        print("ow, let me try again with {}".format(question))
        list_of_words = [i for i in list_of_words if i[position] != highest_letter]
        bonus_point = 1000
        print(len(list_of_words))

#Idee: Tel per positie vanaf letter met meer dan 0 hits, wat het gemiddelde is, en start daar
