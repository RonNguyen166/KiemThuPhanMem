
users =[{"status": "register","username": "ronnguyen67" ,"email": "ron@test.com", "password": "pass1234", "passwordCheck": "pass1234"},
{"status":"login", "email": "nguyenron83@gmail.com", "password": "pass1234"}]


        
def statusUser(status):
    try:
        return next(user for user in users if user["status"] == status)
    except:
        print("\n User %s is not defined, enter a valid user.\n" % status)

