# generates headings (eg: ---- Heading ----)

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''To use this program:\n
    xxx to break
    image to calculate an image
    int to calculate an integer
    txt to calculate text\n''')


# asks users for file type (integer, image, text, xxx)

def get_filetype():
    while True:
        response = input("File type: ").lower()
        # check i or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if it's an image
        elif response in ['picture', 'image', 'img', 'p']:
            return "image"

        # check for text
        elif response in ['text', 'txt', 't']:
            return "text"

        # if the response is INVALID
        else:
            print("Please enter a valid file type")


# ASk the user for width and loop until they enter a
# number that is more than zero
def int_check(question, low):
    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))
            # check the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def integer_check(question, low):
        even_worse_error = "Please enter an integer more than 0"
        error = f"Please enter an integer (i.e: a positive number without a decimal part)"
        while True:

            try:
                # ask the user for a number
                response = int(input(question))
                # check the number is more than zero
                if response > low:
                    return response
                elif response == low:
                    print(even_worse_error)
                else:
                    print(error)

            except ValueError:
                print(error)


def integer_for_image_check(question, low):
    bad_error = "Please enter an integer that is more than 0"
    error = f"Please enter an integer (i.e: a positive number without a decimal part)"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))
            # check the number is more than zero
            if response > low:
                return response
            elif response == low:
                print(bad_error)
            else:
                print(error)

        except ValueError:
            print(error)


# calculates how many bits are needed to represent an image
def image_calc():
    pass

    # Main routine goes here

    width = integer_for_image_check("Width: ", 0)
    height = integer_for_image_check("Height: ", 0)

    # calcs pixels and calcs bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# calculates how many bits are needed to represent an integer
def int_calc():
    # ask the user to enter an integer (more than / equal to 0)
    integer = integer_check("Integer: ", 0)

    # convert the integer to raw_binary and work out bits needed
    raw_binary = bin(integer)
    # remove the 0b from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # set up answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer


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

# display instructions if requested
want_instructions = input("Press <enter> to "
                          "read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if the user chose "i" ask if they want an image or an integer
    if file_type == "i":

        want_int = input("Press <enter> for an integer or any ke"
                         "y for an image. ")
        if want_int == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
        print()
    elif file_type == "integer":
        int_ans = int_calc()
        print(int_ans)
        print()
    else:
        text_ans = calc_text_bits()
        print(text_ans)
        print()
