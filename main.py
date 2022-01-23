from user import User
from newsletter import NewsLetter
from category import Category
from subscriber import Subscriber

userCount = 0
newsCount = 0 
categoryCount = 0
subsCount = 0
userList = []
categoryList = []
newsList = []
subsList = []

def registerUser(name, email):
    global userCount
    userCount = userCount + 1
    userList.append(User(userCount, name, email))
    return {"UserID":(userCount - 1)}

def createNewsletter(title, userId, price, categoriesList):
    global categoryCount, newsCount

    if checkUserExistence(userId):
        for i in range(len(categoriesList)):
            flag = False
            for j in range(len(categoryList)):
                if categoriesList[i] == categoryList[j].name:
                    flag = True
                    break
            if not(flag):
                categoryCount = categoryCount + 1
                categoryList.append(Category(categoryCount, categoriesList[i]))

        newsList.append(NewsLetter(newsCount,categoriesList,title, userId, price))
        newsCount = newsCount + 1
        return {"NewsLetter ID": (newsCount-1)}

    else:
        return "Unable to register NewsLetter coz UserID is not created"

def getNewsLetters(categoriesList):
    for i in range(len(categoriesList)):
        print(categoriesList[i])
        for j in range(len(newsList)):
            if categoriesList[i] in newsList[j].categoryList:
                print(newsList[j].newsId, newsList[j].title)
                print()
        print()
        print()

    return ""


def checkUserExistence(userId):
    flag = False

    for i in range(len(userList)):
        if userList[i].userId == userId:
            flag = True
            break

    return flag



if __name__ == "__main__":

    print(registerUser("John Doe", "johnDoe@gmail.com"))
    print(registerUser("Clarke", "clarke@gmail.com"))

    print(createNewsletter("Latest in tech by John Doe",1,10,["technology","latest","science"]))
    print(createNewsletter("Old Science",2,20,["technology"]))



    print(getNewsLetters(["technology", "latest"]))
    print(getNewsLetters(["xyz"]))

