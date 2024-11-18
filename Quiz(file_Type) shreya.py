import random

def load_user_data():
    user_data = {}
    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                if line.strip():
                    username, user_password = line.strip().split(", Password: ")
                    username = username.replace("Name: ", "")
                    user_data[username] = user_password
    except FileNotFoundError:
        pass
    return user_data


def save_user_data(username, user_password):
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {username}, Password: {user_password}\n")


user_data = load_user_data()


print("Hello User! This is a quiz app")


user_status = input("Are you a new user? (yes/no): ").strip().lower()

if user_status == "no":
    username = input("Enter your name: ")
    if username in user_data:
        user_password = input("Enter your password: ")
        if user_data[username] == user_password:
            print("Login successful!")
        else:
            print("Incorrect password. Exiting the program.")
            exit()
    else:
        print("No such user found. Please register as a new user.")
        exit()
else:
    username = input("Enter your name: ")
    user_password = input("Set a password you want: ")
    save_user_data(username, user_password)
    print("Registration successful!")

class QuizApp:
    def __init__(self, question_bank):
        self.selected_questions = random.sample(question_bank, 5)
        self.user_answers = {}

    def take_quiz(self):
        for question_number, (quiz_question, options, correct_option) in enumerate(self.selected_questions, 1):
            print(f"Question {question_number}: {quiz_question}")
            for option_number, option_text in enumerate(options, 1):
                print(f"  {option_number}. {option_text}")
            user_input = input("Select an option (1-4) or type 'mark' to attempt later: ")
            if user_input.lower() == 'mark':
                self.user_answers[question_number] = None
            else:
                self.user_answers[question_number] = int(user_input)

        for question_number, (quiz_question, options, correct_option) in enumerate(self.selected_questions, 1):
            if self.user_answers[question_number] is None:
                print(f"\nMarked for Review - Question {question_number}: {quiz_question}")
                for option_number, option_text in enumerate(options, 1):
                    print(f"  {option_number}. {option_text}")
                user_input = input("Select an option (1-4): ")
                self.user_answers[question_number] = int(user_input)

    def calculate_score(self):
        score = 0
        for question_number, (_, _, correct_option) in enumerate(self.selected_questions, 1):
            if self.user_answers[question_number] == correct_option:
                score += 1
        return score


quiz_topics = {
    "1": ("Python", questions_python),
    "2": ("C++", questions_cpp),
    "3": ("Java", questions_java),
    "4": ("DSA", questions_dsa)
}

questions_python = [
    ("What is the output of print(2 ** 3)?", ["6", "8", "9", "5"], 2),
    ("Which data type is used for text?", ["int", "float", "str", "bool"], 3),
    ("What keyword is used to define a function?", ["def", "func", "define", "lambda"], 1),
    ("What is the default data type for numbers in Python?", ["int", "float", "double", "str"], 1),
    ("Which module is used for math operations?", ["sys", "math", "random", "os"], 2),
    ("What will be the output of print(10 // 3)?", ["3.33", "3", "3.0", "None"], 2),
    ("Which function is used to get the length of a list in Python?", ["size()", "length()", "len()", "count()"], 3),
    ("What is the output of print('Hello'[1])?", ["e", "H", "l", "o"], 1),
    ("Which of the following data types is immutable in Python?", ["list", "dict", "set", "tuple"], 4),
    ("Which keyword is used to start a function definition in Python?", ["func", "def", "function", "define"], 2),
    ("What is the output of print(5 % 2)?", ["0", "2", "1", "5"], 3),
    ("Which of the following methods is used to add an item to a list?", ["add()", "append()", "insert()", "extend()"],2),
    ("How do you start a comment in Python?", ["//", "/*", "#", "<!-- -->"], 3),
    ("What is the result of bool('') in Python?", ["True", "False", "1", "0"], 2),
    ("Which of the following is used to create a new set in Python?", ["[]", "{}", "()", "set()"], 4),
    ("Which method is used to convert a string to lowercase in Python?",["toLower()", "lowercase()", "lower()", "casefold()"], 3),
    ("What does range(5) produce in Python?",["[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4, 5]", "[1, 2, 3, 4]"], 1),
    ("Which of the following is a built-in Python data type?", ["stack", "queue", "dict", "graph"], 3),
    ("What is the correct syntax to check if a is equal to b in Python?", ["a = b", "a == b", "a eq b", "a != b"], 2),
    ("What is the output of print(type(5.0))?",["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'decimal'>"], 2)
]

questions_cpp = [
    ("Which operator is used for insertion?", ["->", ">>", "<<", "::"], 3),
    ("How do you declare a constant variable?", ["const", "constant", "static", "define"], 1),
    ("What is used to terminate a statement?", [".", ":", ";", ","], 3),
    ("Which function returns the size of a data type?", ["sizeof", "length", "count", "size"], 1),
    ("Which of these is a logical operator?", ["&&", "+", "=", "*"], 1),
    ("Which operator is used to access members of a class through a pointer?", ["->", ".", "::", ":"], 1),
    ("What is the correct way to declare a constant variable in C++?", ["const int x = 10;", "constant int x = 10;", "int const x = 10;", "int constant x = 10;"], 1),
    ("Which loop structure is used to ensure the loop runs at least once?", ["for", "while", "do-while", "foreach"], 3),
    ("Which of the following is a correct way to allocate memory dynamically?", ["new int[10];", "alloc int[10];", "malloc(10);", "calloc(10);"], 1),
    ("Which of these is not a valid access modifier in C++?", ["public", "protected", "default", "private"], 3),
    ("What is the size of an int in C++ (assuming 32-bit architecture)?", ["2 bytes", "4 bytes", "8 bytes", "16 bytes"], 2),
    ("Which function is used to get the length of a string in C++?", ["length()", "size()", "strlen()", "Both length() and size()"], 4),
    ("Which of the following is used to terminate a statement in C++?", [";", ":", ".", ","], 1),
    ("Which function is used to get input from the user in C++?", ["cin", "cout", "scanf", "print"], 1),
    ("What does STL stand for in C++?", ["Standard Template Library", "Standard Type Library", "Standard Testing Library", "Simple Template Library"], 1),
    ("Which of the following is a feature of C++?", ["Object-oriented", "Procedural", "Functional", "All of the above"], 4),
    ("What is the output of 'cout << (5 > 3 ? 10 : 5);'?", ["5", "10", "3", "0"], 2),
    ("Which of the following is used to declare an array in C++?", ["int[] arr;", "array<int> arr;", "int arr[10];", "int arr{};"], 3),
    ("Which keyword is used to define a macro in C++?", ["macro", "define", "#define", "const"], 3),
    ("How do you declare a pointer in C++?", ["int *p;", "int p[];", "int &p;", "int p{};"], 1)
]

questions_java = [
    ("Java is platform-independent due to:", ["API", "JVM", "JRE", "JDK"], 2),
    ("Which keyword is used for inheritance?", ["inherits", "extends", "implements", "parent"], 2),
    ("What is the extension for compiled Java files?", [".jav", ".jv", ".class", ".java"], 3),
    ("Which is used for memory allocation?", ["malloc", "alloc", "new", "create"], 3),
    ("Java is:", ["Procedural", "Functional", "Scripting", "Object-Oriented"], 4),
    ("What is the size of an int data type in Java?", ["16-bit", "32-bit", "64-bit", "8-bit"], 2),
    ("Which of the following is not a Java keyword?", ["static", "public", "void", "integer"], 4),
    ("What is the purpose of the 'this' keyword in Java?",["Refers to current object", "Refers to parent class", "Refers to super class", "Refers to any class"], 1),
    ("Which method is called when an object is created in Java?", ["constructor", "method", "getter", "setter"], 1),
    ("What is the extension of a compiled Java class?", [".java", ".class", ".jav", ".byte"], 2),
    ("Which keyword is used for inheritance in Java?", ["inherits", "extends", "implements", "instanceof"], 2),
    ("What does JVM stand for?",["Java Variable Machine", "Java Virtual Machine", "Java Vector Machine", "Java Verification Machine"], 2),
    ("Which method can be used to find the length of a string in Java?", ["getSize()", "size()", "length()", "strlen()"],3),
    ("Which of these is not a feature of Java?",["Platform-Independent", "Object-Oriented", "Pointers", "Multithreading"], 3),
    ("Which keyword is used to create an interface in Java?", ["class", "extends", "interface", "implements"], 3),
    ("What is the default value of a boolean variable in Java?", ["true", "false", "1", "null"], 2),
    ("Which keyword in Java is used to handle exceptions?", ["try", "catch", "throw", "All of the above"], 4),
    ("Which of the following loops is entry-controlled?", ["do-while", "while", "for", "Both while and for"], 4),
    ("Which operator is used for bitwise AND in Java?", ["&", "|", "^", "%"], 1),
    ("How can you stop a loop in Java?", ["break", "return", "exit", "continue"], 1)
]

questions_dsa = [
    ("Which data structure follows LIFO?", ["Queue", "Stack", "Tree", "Graph"], 2),
    ("What is the time complexity of binary search?", ["O(n)", "O(log n)", "O(n^2)", "O(n log n)"], 2),
    ("Which is a linear data structure?", ["Graph", "Tree", "Stack", "Heap"], 3),
    ("Which sorting algorithm has the best average case performance?", ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort"], 2),
    ("What is the height of a balanced binary tree?", ["O(log n)", "O(n)", "O(n^2)", "O(1)"], 1),
    ("What is the size of an int data type in Java?", ["16-bit", "32-bit", "64-bit", "8-bit"], 2),
    ("Which of the following is not a Java keyword?", ["static", "public", "void", "integer"], 4),
    ("What is the purpose of the 'this' keyword in Java?",["Refers to current object", "Refers to parent class", "Refers to super class", "Refers to any class"], 1),
    ("Which method is called when an object is created in Java?", ["constructor", "method", "getter", "setter"], 1),
    ("What is the extension of a compiled Java class?", [".java", ".class", ".jav", ".byte"], 2),
    ("Which keyword is used for inheritance in Java?", ["inherits", "extends", "implements", "instanceof"], 2),
    ("What does JVM stand for?",["Java Variable Machine", "Java Virtual Machine", "Java Vector Machine", "Java Verification Machine"], 2),
    ("Which method can be used to find the length of a string in Java?", ["getSize()", "size()", "length()", "strlen()"],3),
    ("Which of these is not a feature of Java?",["Platform-Independent", "Object-Oriented", "Pointers", "Multithreading"], 3),
    ("Which keyword is used to create an interface in Java?", ["class", "extends", "interface", "implements"], 3),
    ("What is the default value of a boolean variable in Java?", ["true", "false", "1", "null"], 2),
    ("Which keyword in Java is used to handle exceptions?", ["try", "catch", "throw", "All of the above"], 4),
    ("Which of the following loops is entry-controlled?", ["do-while", "while", "for", "Both while and for"], 4),
    ("Which operator is used for bitwise AND in Java?", ["&", "|", "^", "%"], 1),
    ("How can you stop a loop in Java?", ["break", "return", "exit", "continue"], 1)
]


while True:
    print("\nSelect a topic for the quiz:")
    print("1. Python")
    print("2. C++")
    print("3. Java")
    print("4. DSA")
    selected_topic = input("Enter the number of your choice: ")

    if selected_topic in quiz_topics:
        topic_name, question_bank = quiz_topics[selected_topic]
        print(f"\nStarting quiz on {topic_name}...\n")
        quiz = QuizApp(question_bank)
        quiz.take_quiz()
        user_score = quiz.calculate_score()
        print(f"\nYour score: {user_score}/{len(quiz.selected_questions)}")

        with open("user_data.txt", "a") as file:
            file.write(f"Name: {username}, Topic: {topic_name}, Score: {user_score}/{len(quiz.selected_questions)}\n")

    else:
        print("Invalid choice. Please select a valid topic.")
