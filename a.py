spam_keywords =["limited offer","offer","discount","claim","money","click","win", "free", "offer", "click", "buy now", "claim", "prize", "money"]

def spam(text):
    return any (word in text.lower() for word in spam_keywords)

email = input("enter the emsil txt :")

print ("spam" if  spam(email)else "ham")


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def movie_chatbot():
    print("🤖 MovieBot: Hello! Welcome to Movie Ticket Booking System.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().upper

        if "movie" in user_input or "movies" in user_input:
            print("🤖 MovieBot: Currently showing: Leo, Jawan, Avatar 2, Vikram. Which movie would you like to watch?")

        elif "timing" in user_input or "time" in user_input or "show" in user_input:
            print("🤖 MovieBot: We have show timings at 10AM, 1PM, 4PM, 7PM and 10PM.")

        elif "ticket price" in user_input or "price" in user_input or "cost" in user_input:
            print("🤖 MovieBot: Ticket prices are ₹150 for Normal and ₹250 for Premium seats.")

        elif "book" in user_input or "booking" in user_input:
            print("🤖 MovieBot: Sure! Please visit our booking website or box office to book your tickets.")

        elif "seat" in user_input or "availability" in user_input:
            print("🤖 MovieBot: Seats are available! Would you like Normal or Premium seats?")

        elif "bye" in user_input:
            print("🤖 MovieBot: Thanks for choosing MovieBot! Enjoy your show 🍿🎥")
            break

        else:
            print("🤖 MovieBot: Sorry, I didn’t understand that. Please ask about movies, timings, price, or booking.")


movie_chatbot()
