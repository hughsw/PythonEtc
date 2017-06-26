## First Steps with Git

### Make a new branch, add a file

```bash
# Go to the assignments directory in the project
cd PythonEtc/assignments

# Checkout the branch called "master"
git checkout master

# Pull does two things:
# 1) synchronize your repository with origin (GitHub) -- same as `git fetch`, gets commits from GitHub
# 2) points the current branch, master, to the latest commit in its upstream branch, origin/master -- same as `git merge origin/master`
git pull

# Make a new branch for your work, starting from the current commit;
# Here, and below, replace hsw-assignments with whatever you want to call your branch
git checkout -b hsw-assignments

# Do some work, e.g. make a file called taxes2.py -- Do it!
touch taxes2.py
# Put something interesting in the file!
```
Do it!

### Add, commit, push

```bash
# Look at git's status, showing that it sees the file, but the file isn't tracked by git
git status

# Have git add the file taxes2.py to the staging area (also called the index);
# now git is tracking the file
git add taxes2.py

# Look at git's status, showing that it is tracking the file, and the file is staged for being committed
git status

# Make a new commit that includes your assignment file (and anything in the staging area)
# This only puts the commit in your local repository
# The string in single quotes is the commit message, forever visible to the world
git commit -m 'hsw first assignment'

# Try to send your commit to GitHub;
# git will fail and give you a hint indicating what you need to do
git push

# Take the hint.
# This sends your new commit(s) to Git on branch hsw-assignments in the upstream repository;
# I.e. on the remote called origin, branch hsw-assignments is the upstream for local branch hsw-assignments
# On success, this synchronizes commits on your hsw-assignments branch to GitHub, now the world can see them
git push --set-upstream origin hsw-assignments

# Look at all the branches in your local repository
git branch -a

# Look at all the commits in all your local branches;
# - ascii graphics of commits in branches tree
# - asterisk * marks commits
# - branches grow bottom to top
git log --pretty=format:"%h%d %an   %s" --graph --all
```
