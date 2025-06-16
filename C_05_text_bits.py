# Calculates bits for text in ascii

def calc_text_bits():
    pass

    # get text from user
    response = input("Enter some text: ")
    print()
    # calc bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # set up answer and return it
    answer = (f"{response} has {num_chars} characters." 
             f" \nWe need {num_chars} x 8 bits to represent it "
              f"\nwhich is {num_bits} bits")
    print()
    return answer


# main routine goes here
text_ans = calc_text_bits()
print(text_ans)
