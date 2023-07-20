#Calculates if someone is young or old based on their age that is inputed. This makes use of functions, object conversion and receiving text from user

def calc_if_old(age):
    if age > 45 :
        print('Wow, you are ' + str(age) + ' years old! That is old!')
    else:
        print('Wow! you are ' + str(age) + ' years old!  That is young!')

    
get_age = input('How old are you?')



calc_if_old(int(get_age))
