spam_keywords =["limited offer","offer","discount","claim","money","click","win", "free", "offer", "click", "buy now", "claim", "prize", "money"]

def spam(text):
    return any (word in text.lower() for word in spam_keywords)

email = input("enter the emsil txt :")

print ("spam" if  spam(email)else "ham")