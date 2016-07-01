

# def get_login(file):
#     f = open('users.txt')
#     logins = []
#     for line in f:
#         # print line
#         # print line.split()
#         names = line.split(' ')
#         low = names[0][0] + names[1]
#         print low.lower()
#
#
# get_login('users.txt')

#
def get_login(file):
    users = open(file)
    logins = []
    for line in users:
        names = line.split(' ')
        login = names[0][0] + '_' + names[1][:-1] + '@mail.ru'
        logins.append(login.lower())
    print logins


print get_login('users.txt')

