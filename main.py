'''
Updated March 5, 2021

@author: Chloe Quinto
@class: SSW 567 - HW 4

Github API
NOTE: Optional replace TOKEN with Personal Github Token

I pledge my honor that I have abided by the Stevens Honor System - Chloe Quinto
'''
import json
import requests

TOKEN =''
headers = {'Authorization': 'token ' + TOKEN}

def retrieve_user_repos(id):
    '''
    Args:
        id - Github User ID
    Return:
        Given an id, this API will return a list of JSON Objects
        one for reach repositories for that users
    '''
    # id must be of type str
    if not isinstance(id, str):
        return "Invalid Input"

    # Use OA Token
    if TOKEN != '':
        # GET requests a user's repo with OA Token
        response = requests.get('https://api.github.com/users/' + str(id) + \
            '/repos?per_page=32', headers=headers)
    else:
        # GET requests a user's repo
        response = requests.get('https://api.github.com/users/' + str(id) + \
            '/repos?per_page=32')

    # Check for HTTP Errors
    if response.status_code != 200:
        return "ERROR: Status code for user: " + str(response.status_code)

    # convert JSON object to Python
    parsed_to_json = json.loads(response.text)

    all_repo_names = [] # List of User's Repo Names
    results = "\n" # Str result

    # Collect Repo Names in a list
    for i in range(len(parsed_to_json)):
        repo = parsed_to_json[i]
        name = repo['name']
        all_repo_names.append(name)

    # if user has no repos
    if all_repo_names == []:
        return "User has no public repos"

    for j in range(len(all_repo_names)):
        # Stop at 31th Repo for Optimized Performance
        if j == 31:
            return results + "... User has more than 30 public repos"
        # Call helper function to count number of commits per repo
        commit = retrieve_commits(id, all_repo_names[j])
        # Add to str of results
        results += "Repo: " + str(all_repo_names[j]) + " Number of commits " + str(commit) + "\n"

    return results

def retrieve_commits(id, repo):
    '''
    Args:
        id - Github User ID
        repo - Name of Repo
    Return:
        Given an ID and Repo, this function will return the number of commits
        for that specific Repo
    '''

    # Use OA Token
    if TOKEN != '':
        # GET requests number of commits for repo
        response_commit = requests.get('https://api.github.com/repos/' + \
            str(id) + '/' + str(repo) + '/commits?per_page=100', headers=headers)
    else:
        response_commit = requests.get('https://api.github.com/repos/' + \
            str(id) + '/' + str(repo) + '/commits?per_page=100')

    # Check for HTTP Errors
    if response_commit.status_code != 200:
        return "ERROR: Status code for repo: " + str(response_commit.status_code)

    # convert JSON object to Python
    parsed_to_json = json.loads(response_commit.text)

    # number of commits is the number of json objects in parsed_to_json
    num_commits =  len(parsed_to_json)

    # limit to 100 commits per page, if numCommits == 100, actual commits could be 100 or more
    if num_commits == 100:
        return "100 or more"

    return num_commits


if __name__ == "__main__":
    print("Making a GET request...may take some time...")

    # Examples
    print(retrieve_user_repos("chloequinto"))

    # print(retrieve_user_repos("richkempinski"))

    # User with over 100 repos and over 100 commits in some repo
    # print(retrieve_user_repos("cirosantilli"))
    # print(retrieve_commits("cirosantilli", "test-many-commits-1m"))

    # User with no public repos
    # print(retrieve_user_repos("guandicimo"))
