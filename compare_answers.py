def compare_answers(user_answer, correct_answer):
    """
    compare_answers : took two strings , compare them and return True or False
    It will be used inside a for loop to compare each user answer with the correct answer
    """
    if user_answer == correct_answer:
        return True
    else:
        return False


def check_answers(user_answers,correct_answers):
    """
    Function check_answers : given as one parameter user_answers to a quiz they get compared
    against the second parameter -correct_answers- to build a score for the user 
    Input : user_answers is a list of 5 strings containing user answers
            correct_answers is a list of 5 strings with correct answers
    Output  : A message with the user score. User requires 70% correct answers to pass-
    """
    results= [None, None, None, None, None]
    #answer_number = 0
    
    for n in range(5):
        results[n] = compare_answers(user_answers[n], correct_answers[n])
    print("debug : content of result comp after compare_answers : {} ".format(results))
        
    count_correct = 0
    
    for result in results:
        if result:
            count_correct += 1
    print("debug : content of count_correct {} ".format(count_correct))
    
        
    #count_incorrect = 0
    #for result in results:
    #    if result == True:
    #        count_correct += 1
    #    if result != True:
    #        count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    else:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
    
    
#user_answers = ["uno","doce","tres","cuatrocientos","cinco"]
#correct_answers = ["uno","dos","tres","cuatro","cinco"]

#check_answers(user_answers, correct_answers)