#Arora, Somesh
#2014-09-17
#program that prompts the user to enter a sentence and then prints the word statistics of the input sentence i.e. how many times each word is repeated.

my_sentence=input("Please Enter a Sentence Without any Punctuation(s)")
my_list=my_sentence.split()
my_list.sort()
list_to_check = []
print("List Statistics:")
for x in range(0,len(my_list)):
    y=my_list[x]
    str_check = False

    for z in range(0, len(list_to_check)):
        if(y == list_to_check[z]):
            str_check = True
            break;

    if(str_check == True):
        continue
    else:
        if my_list.count(y)==1:
            list_to_check.append(y)
            print ('"'+y+'"'+" is repeted 1 time." )
            continue
        else:
            list_to_check.append(y)
            occur=my_list.count(y)
            print('"'+y+'"'+" is repeted " + str(occur)+" times. " )
