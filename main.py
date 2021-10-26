def main():
    # check if the file exist
    # try opening the file if file is not read then the except code will execute
    try:
        input_file = input("Please enter the name of the file: ")
        file = open(input_file + ".txt", "r")
        read_file = file.read()
        print("The DNA sequence format with 60 nt per lines")
        # looping through 0 to length of character file read_file with 60 step
        for i in range(0, len(read_file), 60):
            # printing out the character of files from i=0 to i+n=0+60 and from 60 to i+n=60+60 and so on unto length 259
            print(read_file[i:i + 60])

        # function that print the total and percentage of nucleotide
        total_percentage_nucleotide(read_file)

        ask_question = True
        while ask_question:
            # asking question to choose option again and again until the user choose any other letter than option where the program will stop asking
            requestOutput = input("Which of the following output you would like to see.\n"
                                  "Choose option A, B or C to see the desired result or Type any other keywords to exit from the option:\n"
                                  "A. The reverse sequence formatted to display 60 nt per line.\n"
                                  "B. The reverse-complement sequence formatted to display 60 nt per line.\n"
                                  "C. Would you like to view the open reading frames\n"
                                  "")

            # this function will return the reverse_sequence of any DNA file by just passing in the read file
            # if the user enters A or a then print out the reverse sequence
            if requestOutput == "A" or requestOutput == "a":
                print_reverse_sequence(read_file)

            # if the user enters B or b then print out the reverse complement
            elif requestOutput == "B" or requestOutput == "b":
                print_reverse_complement(read_file)

            elif requestOutput == "C" or requestOutput == "c":
                codon_func(read_file)

            else:
                # stop the loop and ask for the user whether to output the file or not
                ask_question = False

        # function to write a reverse sequence file
        file_output(return_reverse_sequence(read_file))

        file.close()

    except (FileNotFoundError, IOError):
        print("Wrong file or file path")


def total_percentage_nucleotide(file):
    # code for A nucleotide to display count and its percentage
    print("A nucleotide counts:", file.count("A"), "in a DNA sequence", file.count("A") / len(file) * 100,
          "% in a sequence")
    # code for C nucleotide to display count and its percentage
    print("C nucleotide counts:", file.count("C"), "in a DNA sequence", file.count("C") / len(file) * 100,
          "% in a sequence")
    # code for G nucleotide to display count and its percentage
    print("G nucleotide counts:", file.count("G"), "in a DNA sequence and ", file.count("G") / len(file) * 100,
          "% in a sequence")
    # code for T nucleotide to display count and its percentage
    print("T nucleotide counts:", file.count("T"), "in a DNA sequence", file.count("T") / len(file) * 100,
          "% in a sequence")


def return_reverse_sequence(file):
    # making a reverse_sequence by replacing letters "AGTC", "TCAG"
    reverse_sequence = file.replace("A", "t")
    reverse_sequence = reverse_sequence.replace("T", "a")
    reverse_sequence = reverse_sequence.replace("G", "c")
    reverse_sequence = reverse_sequence.replace("C", "g")
    reverse_sequence = reverse_sequence.upper()  # converting all the lowercase letters to upper
    return reverse_sequence


def print_reverse_sequence(file):
    reverse = return_reverse_sequence(file)
    for i in range(0, len(reverse), 60):
        print(reverse[i:i + 60])


def print_reverse_complement(file):
    reverse = return_reverse_sequence(file)
    reverse_complement = reverse[::-1]
    for i in range(0, len(reverse_complement), 60):
        print(reverse_complement[i:i + 60])


def codon_func(read_file):
    startCode = "ATG"  # set a substring contains begin code "ATG"
    startCode = read_file[(read_file.find(startCode)):]  # set a substring from the beginning of ATG to the end of datastr
    ORFs = ''
    for n in range(0, len(startCode), 3):  # set up a for loop to screen every three nucleotides
        if startCode[n:n + 3] == 'TAA' or startCode[n:n + 3] == 'TGA' or startCode[n:n + 3] == 'TAG':  # screen to find the stop code
            ORFs = startCode[0:n + 3]  # calculate the ORFs length
            print(f'\nThe number of open reading frames (ORFs) in the forward sequence is: {len(ORFs)}.')
            break
        else:
            ORFs = startCode[0:]  # get the incomplete ORFs sequence
    if ORFs[-3:] != 'TAA' and ORFs[-3:] != 'TGA' and ORFs[-3:] != 'TAG':
        print(f'\nThe number of open reading frames (ORFs) in the forward sequence is: {len(ORFs)}, but the ORFs is incomplete.')
    reverse = read_file[::-1]
    rev_code = reverse[reverse.find(startCode):]  # find begin code and then get the substring from the begin code to the end of the reverse sequence
    for p in range(0, len(rev_code), 3):  # set up a for loop to screen every three nucleotides
        if rev_code[p:p + 3] == 'TAA' or rev_code[p:p + 3] == 'TGA' or rev_code[p:p + 3] == 'TAG':  # screen to find the stop code
            rev_ORFs = rev_code[0:p + 3]  # calculate the ORFs length
            print(f'\nThe number of open reading frames (ORFs) in the reverse sequence is: {len(rev_ORFs)}.')
            break
        else:
            rev_ORFs = rev_code[0:]  # get the incomplete ORFs sequence
    if rev_ORFs[-3:] != 'TAA' and rev_ORFs[-3:] != 'TGA' and rev_ORFs[-3:] != 'TAG':
        print(f'\nThe number of open reading frames (ORFs) in the reverse sequence is: {len(rev_ORFs)}, but the ORFs is incomplete.')


def file_output(file):
    # asking user to create a output file or not
    # using try exception to write the file of the file is not written properly then the except code will execute
    try:
        output_file = input("Would you like to create an output file? Y or N")
        # if user type Y then create a file
        if output_file == "Y":
            name_of_file = input(
                "Write the name of the file you want.")  # asking for the name of the file to write
            writeFile = open(name_of_file + ".txt", "w") # open to write
            writeFile.write(file)  # write reverse_sequence in the user outputted name file
            writeFile = open(name_of_file + ".txt", "r")  # open that file to read
            print(writeFile.read())  # print that file to the console
            writeFile.close()
    except (FileNotFoundError, IOError):
        print("Wrong file or file path")


main()
