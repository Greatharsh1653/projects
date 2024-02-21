import csv

def ask_questions(n, questions):
    total = 0
    for i in range(n):
        while True:
            try:
                response = input(questions[i])
                total += int(response)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return total

def store_details(username,sum1, sum2):
    with open('details.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username,sum1, sum2, sum1+sum2])

def main():
    username = input("Enter your username: ")
    print("Let me explain you how the bot works and how to answer the following question...\n")
    print("Not at all = 0; Several days = 1;\nMore than half the days = 2\nNearly every day = 3\n")

    print("Phase 1 Started")
    questions_phase1 = ["I felt that I had nothing to look forward to:","I found myself getting agitated:","I found it difficult to relax:","I felt down-hearted and blue:","I felt down-hearted and blue:","I felt I wasn’t worth much as a person:","I felt that I was rather touchy:","I felt that life was meaningless:","I felt scared without any good reason:","I tended to over-react to situation:"]
    sum1 = ask_questions(10, questions_phase1)
    print("Phase 1 Completed")

    print("Phase 2 Begins\n")

    questions_phase2 = ["Little interest or pleasure in doing things:","Feeling down, depressed, or hopeless:","Trouble falling or staying asleep, or sleeping too much:","Feeling tired or having little energy:","Poor appetite or overeating:","Feeling bad about yourself or that you are a failure:","Thoughts that you would be better of dead:","Trouble concentrating on things, such as reading newspaper,books:","Moving or speaking slowly to other people:","Having anixety attacks in day to day life:"]
   
    sum2 = ask_questions(10, questions_phase2)
    print("Phase 2 Completed\n")

    total = sum1 + sum2
    if total < 20:
        print("LOW LEVEL DEPRESSION")
    elif 20 <= total < 40:
        print("MIDDLE LEVEL DEPRESSION")
    else:
        print("HIGH LEVEL DEPRESSION")

    store_details(username,sum1, sum2)

if __name__ == "__main__":
    main()
