## First Steps with Git

### Make a new branch, add a file

```bash
# Go to the assignments directory in the project
$ cd PythonEtc/assignments

# Checkout the branch called "master"
$ git checkout master

# Pull does two things:
# 1) synchronize your repository with origin (GitHub) -- same as `git fetch`, gets commits from GitHub
# 2) points the current branch, master, to the latest commit in its upstream branch, origin/master -- same as `git merge origin/master`
$ git pull

# Make a new branch for your work, starting from the current commit;
# Here, and below, replace hsw-assignments with whatever you want to call your branch
$ git checkout -b hsw-assignments

# Do some work, e.g. make a file called taxes2.py -- Do it!
$ touch taxes2.py
# Put something interesting in the file!
```
E.g. `taxes2.py`:
```python
def tax2017(income):
    assert income >= 0, str(income)

    if income >= 418400:
        return (income - 418400) * 0.396 + 121505.25
    if income >= 416700:
        return (income - 416700) * 0.35 + 120910.25
    if income >= 191650:
        return (income - 191650) * 0.33 + 46643.75
    if income >= 91900:
        return (income - 91900) * 0.28 + 18713.75
    if income >= 37950:
        return (income - 37950) * 0.25 + 5226.25
    if income >= 9325:
        return (income - 9325) * 0.15 + 932.5
    if income > 0:
        return 0.1 * income
    return 0
```
Do it!

### Add, commit, push

```bash
# Look at git's status, showing that it sees the file, but the file isn't tracked by git
$ git status
On branch hsw-assignments
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	taxes2.py

nothing added to commit but untracked files present (use "git add" to track)

# Have git add the file taxes2.py to the staging area (also called the index);
# now git is tracking the file
$ git add taxes2.py

# Look at git's status, showing that it is tracking the file, and the file is staged for being committed
$ git status
On branch hsw-assignments
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   taxes2.py

# Make a new commit that includes your assignment file (and anything in the staging area)
# This only puts the commit in your local repository
# The string in single quotes is the commit message, forever visible to the world
$ git commit -m 'hsw first assignment'
[hsw-assignments 671ddf8] hsw first assignment
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 assignments/taxes2.py

# Try to send your commit to GitHub;
# git will fail and give you a hint indicating what you need to do
$ git push
fatal: The current branch hsw-assignments has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin hsw-assignments

# Take the hint.
# This sends your new commit(s) to Git on branch hsw-assignments in the upstream repository;
# I.e. on the remote called origin, branch hsw-assignments is the upstream for local branch hsw-assignments
# On success, this synchronizes commits on your hsw-assignments branch to GitHub, now the world can see them
$ git push --set-upstream origin hsw-assignments
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 399 bytes | 0 bytes/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:hughsw/PythonEtc.git
 * [new branch]      hsw-assignments -> hsw-assignments
Branch hsw-assignments set up to track remote branch hsw-assignments from origin.

# Look at all the branches in your local repository
$ git branch -a
* hsw-assignments
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/hsw-assignments
  remotes/origin/master

# Look at all the commits in all your local branches;
# - ascii graphics of commits in branches tree
# - asterisk * marks commits
# - branches grow bottom to top
$ git log --pretty=format:"%h%d %an   %s" --graph --all
* ab5dc44 (origin/hsw-assignments, hsw-assignments) Hugh Secker-Walker   hsw first assignment
* e1fd7a2 Hugh Secker-Walker   [ASSIGNMENTS] Fix typo in taxrate.md
* 30dadaf Hugh Secker-Walker   [ASSIGNMENTS] Add doctest to test the tax bracket assignment, add extra credit
* 47f81a7 Hugh Secker-Walker   [ASSIGNMENTS] Add tax bracket assignment
* a71b75f Hugh Secker-Walker   Update README
* 5abf361 Hugh Secker-Walker   Initial commit
```
