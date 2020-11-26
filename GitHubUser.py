import requests
import sys
from collections import Counter

token = ''
headers = {'Authorization': 'token ' + token}

class GitHubUser:
    
    def __init__(self, *args):
        if any(isinstance(i, list) for i in args):
            print('nested')
            self.usernames = list(*args)
        else:
            print('not nested')
            self.usernames = list(args)
            
    def __str__(self):
        x = ' '.join(self.usernames)
        return f'{x}'
    
    def get_req(self, user):
        req = requests.get(f'https://api.github.com/users/{user}/repos', headers=headers) 
        return req.json()
    
    def names_repos(self):
        user_name = input(f'Choose a username: {", ".join(self.usernames)}\n')
        info_repos = []
        req = self.get_req(user_name)
        for i in req:
            name = i['name'] 
            descript = i['description']
            info = f'Repository name: {name}, description: {descript}'
            info_repos.append(info)
        return '\n'.join(info_repos)
    
    def all_langs(self):
        c = Counter()
        user_name = input(f'Choose a username: {", ".join(self.usernames)}\n')
        req = self.get_req(user_name)
        for i in req:
            c[i['language']] += 1
        result = []
        for l in c:
            res = f'Language: {l}, Number of repos: {c[l]}'
            result.append(res)
        return '\n'.join(result)
    
    def user_max_repos(self):
        n_repos = Counter()
        for user in self.usernames:
            req = self.get_req(user)
            for i in req:
                n_repos[user] += 1
        return f'The user with the biggest number of repos is {n_repos.most_common(1)[0][0]} '\
               f'with {n_repos.most_common(1)[0][1]} repos'
    
    def most_popular_lang(self):
        total = Counter()
        for user in self.usernames:
            req = self.get_req(user)
            for i in req:
                total[i['language']] += 1
        # print(total)
        return f'The most common language among these users is {total.most_common(1)[0][0]}'
            
    def most_popular_user(self):
        followers = Counter()
        for user in self.usernames:
            req = requests.get(f'https://api.github.com/users/{user}', headers=headers)
            followers[user] = req.json()['followers']
        return f'The user with the biggest number of followers is {followers.most_common(1)[0][0]} ' \
               f'with {followers.most_common(1)[0][1]} followers'
        
                  
def main(): 
    # python GitHubUser.py torvalds gvanrossum poettering dhh moxie0 fabpot brendangregg bcantrill antirez
    gh = GitHubUser(sys.argv[1:])
    # gh = GitHubUser('torvalds', 'gvanrossum', 'poettering', 'dhh', 'moxie0',
    #                  'fabpot', 'brendangregg', 'bcantrill', 'antirez')
    print(gh.names_repos())
    print(gh.all_langs())
    print(gh.most_popular_lang())
    print(gh.user_max_repos())
    print(gh.most_popular_user())
    
if __name__ == '__main__': 
    main()   
