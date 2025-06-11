# generates headings (eg: ---- Heading ----)

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("Instructions", "-")


# main routine goes here
want_instructions = input("Press <enter> to "
                          "read the instructions or any key to continue")

# display instructions if requested
if want_instructions == "":
    instructions()
    print('''
    Instructions go here
     - Instruction one
     - Instruction two
     - etc
    ''')
    print("Program continues")
