quiz_data = """\
What is the keyword used to define a function in Python?
1. func
2. define
3. function
4. def
Answer: 4

Which library is commonly used for data analysis in Python?
1. Matplotlib
2. NumPy
3. Pandas
4. SciPy
Answer: 3

What is the output of print(type(3.14)) in Python?
1. <class 'int'>
2. <class 'float'>
3. <class 'str'>
4. <class 'bool'>
Answer: 2

What is the default value of the sep parameter in the print() function in Python?
1. ","
2. " "
3. "_"
4. ";"
Answer: 2

What is the purpose of NumPy in Data Science?
1. Data Visualization
2. Data Analysis
3. Linear Algebra and Mathematical Operations
4. Data Storage
Answer: 3
"""

with open("questions.txt", "w") as file:
    file.write(quiz_data)

def load_questions():
    questions = []
    with open("questions.txt", "r") as file:
        lines = file.readlines()
        question = None
        options = []
        answer = None
        for line in lines:
            line = line.strip()
            if line.startswith("What"):
                if question:
                    questions.append([question, options, answer])
                question = line
                options = []
            elif line.startswith("Answer:"):
                answer = int(line.split(":")[1].strip())
            else:
                options.append(line)
        if question:
            questions.append([question, options, answer])
    return questions

def run_quiz():
    questions = load_questions()
    score = 0
    print("Quiz Start!\n")
    
    for q in questions:
        print(q[0])  # Display question
        for i, option in enumerate(q[1]):  # Display options
            print(f"{i + 1}. {option}")
        
        try:
            answer = int(input("Your answer (1-4): "))  # User selects an answer
            if answer == q[2]:
                score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is: {q[1][q[2] - 1]}\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")
    
    print(f"Your score: {score} out of {len(questions)}")

run_quiz()
