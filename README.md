# Git Setup and Push to GitHub

Git is a version control system that helps track changes in code and manage projects efficiently.

Below are the steps I followed to push my project code to a GitHub repository.

## 1. Install Git
Download Git on your laptop using the default settings.

## 2. Create a Repository on GitHub
My repository name:
```text
Python-internship-daily-tasks
```

## 3. Initialize Git in VS Code
```bash
git init
```
## 4. Add Files to the Staging Area
Add all files:
```bash
git add .
```
Or add a specific file:
```bash
git add <file_name>
```

## 5. Check the Status
Verify the files that have been added to the staging area:
```bash
git status
```

## 6. Commit the Changes
```bash
git commit -m "a useful message"
```

## 7. Connect the Local Repository to GitHub
```bash
git remote add origin <repository_url>
```

## 8. Verify the Remote Repository
```bash
git remote -v
```

## 9. Push the Code to GitHub
Rename the default branch to `main` and push the code:
```bash
git branch -M main
git push -u origin main
```
The `-u` flag sets the upstream branch, allowing future pushes with just `git push`.

## 10. Push Future Changes
Whenever I make new changes:
```bash
git add .
git commit -m "Describe the changes made"
git push
```

# Useful Git Commands

## View Commit History
```bash
git log
```

## View Available Branches
```bash
git branch
```

## Create a New Branch
```bash
git checkout -b branch_name
```

## Switch to an Existing Branch
```bash
git checkout branch_name
```

## Pull Latest Changes from GitHub
```bash
git pull origin main
```

## View Remote Repositories
```bash
git remote -v
```

# Complete Git Workflow
For the first push:

```bash
git init
git add .
git status
git commit -m "Initial commit"
git remote add origin <repository_url>
git branch -M main
git push -u origin main
```
For future updates:

```bash
git add .
git commit -m "Updated project files"
git push
```