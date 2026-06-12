# Git is a memory card for code
# Version control - save your progress so you dont lose it as you go
# Enter commands to save your progress
# Save them so if they get deleted, you can go back to last saved
# Initialize your folder or project with git
# Have git downloaded and installed
# Type git init (your memory card is in your system)
# Git add is how we save our progress
# Save all changes since last time we saved
# Or you can save something specific
# Add a file after git add if you want to save something specific
# Git add . would save everything.
# Most people push changes on everything
# Git add. is the most used
# All files are in saving
# Git commit actually saves those changes to memory
# Git commit - m 'This is the commit message'
# Git commit - m 'Add HTML and CSS file'
# Git add.
# I have a feeling git add. saves all changes since last change to staging
# Git commit -m committs those changes to memory along with a message
# Add the files you wanna save, and then committ
# Git log gives us our saved files. Its a log of all saved changes
# Github is a website like bitbucket and gitlab
# All saved progress on my local machine can go to the site
# Others can see the code and do whatever they want with it

"""
Git is a memory card for code.
Version control lets you save your progress so you don't lose it as you go.

Enter commands to save your progress.
Save them so if they get deleted, you can go back to the last saved version.

Initialize your folder or project with Git:
git init

Have Git downloaded and installed first.

git add stages your changes.
It saves changes since the last commit to the staging area.

You can stage a specific file:
git add filename

Or stage everything:
git add .

Most people commonly use:
git add .

All selected files are now staged and ready to be committed.

git commit actually saves those staged changes to Git's history.

git commit -m "This is the commit message"
git commit -m "Add HTML and CSS file"

Workflow:
1. git add .
2. git commit -m "Your message"

git add . stages all changes since the last commit.
git commit -m saves those staged changes permanently in Git's history along with a message.

Add the files you want to save, then commit them.

git log shows the commit history.
It is a log of all saved changes.

GitHub is a website for hosting Git repositories, similar to Bitbucket and GitLab.

All saved progress on your local machine can be pushed to GitHub.
Others can view, clone, and collaborate on your code depending on the repository's permissions.
"""


"""
Git is a memory card for code.
Version control lets you save your progress.
Use git init to initialize a repository.
Use git add . to stage all changes.
Use git commit -m "message" to save those changes.
Use git log to see commit history.
GitHub lets you store and share repositories online.
"""

"""
GIT NOTES

git init
    Creates a new Git repository.

git add .
    Stages all changed files.

git commit -m "message"
    Saves staged changes to the repository.

git log
    Shows commit history.

GitHub
    Online service for hosting Git repositories.


Repository is a folder. 
Git push pushes changes to github or the website in question
Website will have those changes.

By default, all code is in a master branch. Master memory
Someone else could trail off, and work on it in another branch.
Someone could make changes to my code in another branch
Git checkout -b new-branch
Checking change
M means changes are being tracked
.git folder contains all configuration files. We dont mess with this.
"""
name = 'Usama  Rashid'
dob = '1/1/2000'

string = 'Hello world' 
string2 = 'Eureka!!!'

now_try = 'Trying now'

''' Make a single functionality
Then make a commit
To make sure things are clean and trackable
Git status tells us the changes done locally
What changes occured after the recent commit

Staging area is local. ;
We need to shift files to staging area through git add
Git add . shifts new files to staging area. 
We can commit changes in staging area
Only changes in staging area are committed.

I can also revert to an older commit
Some mechanism to go back in case something wrong occurs
If our commmit history is good, we should be able to go back cleanly

Commits are like linked lists
Head points to the latest commit
Changing head to an older committ would do the same thing
Technically, that would remove the previously latest commit
We need to be careful when handling heads
We might lose a lot of our commits
We might need to remove only a single commit that is in the middle somewhere
git revert
git reset
Git basics are complete now
study git revert and git reset


Git is important for consistent coding
Across various machines and teams
Github
Gitlab
Bitbucket
We have several publically available servers where we can push and pull commits
History can remain on the cloud
That public server is called Github
They make a UI layer for us
Task management as well
We can make a server on our own as well if need be
Gitlab and bitbucket are paid, so people dont use them
Its a slightly social media type platform
Git init make a local repository
We made a repo on github, our remote server
Code on local machine needs to be told to be in sync with github
git remote -v











'''

print (True)
print (False)

# Equals sign means assigning a value in a variable, rather than equality
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2


# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j)) #Woah did that just do the actual calculation?
''' So if i place numbers after the comma, i can then print them out
BUT
If i write a calculation, with an operator, i can then print the number out as well
Wonder if this works with varibles as well. I might be able to calculate them out too
'''
