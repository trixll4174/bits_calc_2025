# asks users for file type (integer, image, text, xxx)

def get_filetype():
    response = input("File type: ").lower()
    while True:

        # check i or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if it's an image
        elif response in ['picture', 'image', 'img', 'p']:
            return "Image"

        # check for text
        elif response in ['text', 'txt', 't']:
            return "text"

        # if the response is INVALID
        else:
            print("Please enter a valid file type")


# main routine goes here
while True:
    file_type = get_filetype()

    # if the user chose "i" ask if they want an image or an integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any ke"
                           "y for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You choose {file_type} ")

    if file_type == "xxx":
        break

