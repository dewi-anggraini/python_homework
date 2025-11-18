# Write your code here.
#Task 1: Hello function
def hello():
    return "Hello!"

#Task 2: Greet function
def greet(name):
    return f"Hello, {name}!"

#Task 3: Calc function
def calc(m, n, operation="multiply"):
    try:
        match operation:
            case "add" :
                return m + n
            case "subtract":
                return m - n
            case "multiply":
                return m * n
            case "divide":
                return m / n
            case "modulo":
                return m % n
            case "int_divide":
                return m // n
            case "power":
                return m ** n
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# test
if __name__ == "__main__":
    print(greet("Dewi"))
    print(calc(21, 3))
    
#Task 4: Data type convertion
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case 'float':
                return float(value)
            case 'str':
                return str(value)
            case 'int':
                return int(value)
            case _:
                return "Invalid data type"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    except Exception as e:
        return f"Error: {e}"

#print(data_type_conversion("banana", "int"))

#Task 5: Grading system, Using "args"
def grade(*args):
    try:
        total = sum(args)
        count = len(args)
        average = total / count
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    except ZeroDivisionError:
        return "Error: No grade provided"
    except Exception as e:
        return f"Error: {e}"

#if __name__ == "__main__":
    print(grade(56, 90, 78))                  
            
#Task 6: Use a For Loop with Range
def repeat(string, count):
    try:
        return string * count 
    except TypeError:
        return "Error: Count must be an integer"
repeat("Hai", 3) 

#Task 7: Students Scores, using **kwargs
def student_scores(count, **kwargs):
    if count == "best":
        return max(kwargs, key=kwargs.get)
    elif count =="mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid count"

# Task 8: Titleize, with String and List Operations
def titleize(string):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = string.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)

# Task 9: Hangman, with more string options
def hangman(secret, guess):
    result = []
    for letter in secret:
        if letter in guess:
            result.append(letter)
        else:
            result.append("_")
    return "".join(result)

# Task 10: Pig Latin
def pig_latin(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    def convert_text(word):
        if word[0] in vowels:
            return word + "ay"
        elif word.startswith("qu"):
            return word[2:] + "quay"
        elif "qu" in word:
            qu_index = word.find("qu")
            return word[qu_index + 2:] + word[:qu_index + 2] + "ay"
        else:
            for i, char in enumerate(word):
                if char in vowels:
                    return word[i:] + word[:i] + "ay"
            return word + "ay"
    return ' '.join(convert_text(w) for w in text.split())
                







    
    


