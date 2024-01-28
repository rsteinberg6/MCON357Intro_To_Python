#Rina Steinberg
#MCON 357 - Practicum
#Intro to Python

#method that takes the number and does the conversion
def convert_to_words(num):
    if num == 0:
        return "zero"

    #defines list for the numbers written out
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    words = ""

    #10-19
    if num >= 10 and num <= 19:
        words += teens[num - 10] + " "
        num = 0
    #20 and up
    elif num >= 20:
        words += tens[num // 10] + " "
        num %= 10

    #1-9
    if num >= 1 and num <= 9:
        words += ones[num] + " "

        
    return words.strip()

#method to break up the sentence, then piece it back together to find the numbers
def convert_string_to_words(input_string):
    #split string into words
    wordsSplit = input_string.split()

    result_words = [] #store results

    for word in wordsSplit:
        if word.isdigit():
            #if num convert to text
            numeric_value = int(word)
            converted_result = convert_to_words(numeric_value)
            result_words.append(converted_result)
        else:
            result_words.append(word)

    #join back together into string
    result_string = ' '.join(result_words)

    return result_string

#get user input as a string
user_input = input("Enter a string: ")

#convert numbers to words from the input string and print
output_string = convert_string_to_words(user_input)
print("Output:", output_string)
