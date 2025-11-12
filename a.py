spam_keywords =["limited offer","discount","claim","money","click","win", "free", "offer", "click", "buy now", "claim", "prize", "money"]

def spam(text):
    return any (word in text.lower() for word in spam_keywords)

email = input("enter the emsil txt :")

print ("spam" if  spam(email)else "ham")


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_




# def college_chatbot():
#     print("🤖 MovieBot: Hello! Welcome to Movie Ticket Booking System.")
#     print("Type 'bye' to exit.\n")

#     while True:
#         user_input = input("You: ").lower()

#         if "admission" in user_input:
#             print("🤖 College Bot: Admissions are open from June to August. You can apply online through our college website.")

#         elif "courses" in user_input or "programs" in user_input:
#             print("🤖 College Bot: We offer B.Sc, B.A, B.Com, B.Tech, and M.Tech programs. Which course are you interested in?")

#         elif "fees" in user_input or "fee" in user_input:
#             print("🤖 College Bot: The average annual fee is around ₹50,000. Exact fees depend on the course.")

#         elif "scholarship" in user_input:
#             print("🤖 College Bot: Yes, we provide scholarships based on merit and need. Please check the scholarship section on our website.")

#         elif "hostel" in user_input:
#             print("🤖 College Bot: We provide separate hostels for boys and girls with Wi-Fi, mess, and gym facilities.")

#         elif "contact" in user_input or "phone" in user_input:
#             print("🤖 College Bot: You can reach us at +91-12345-67890 or email: info@abccollege.edu")

#         elif "bye" in user_input:
#             print("🤖 College Bot: Thank you for contacting ABC College. Have a great day!")
#             break

#         else:
#             print("🤖 College Bot: Sorry, I don't have information about that. Please contact the college office for details.")


# college_chatbot()



