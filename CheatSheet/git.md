<h3> Git setup commands   </h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>git config --global user.name [username] </td>
        <td>Add username</td>
    </tr>
    <tr>
        <td>git config --global user.email [user_email_id] </td>
        <td>Add email</td>
    </tr>
    <tr>
        <td>git init </td>
        <td>Add tracker to the folder</td>
    </tr>
    <tr>
        <td>rm -rf .git </td>
        <td>Remove tracker from the folder</td>
    </tr>
    <tr>
        <td>git clone [URL] [path] </td>
        <td>Cloning a remote repository</td>
    </tr>
    <tr>
        <td>git remote -v</td>
        <td>Shows info of the original repository</td>
    </tr>
</table>

<br/>

<h3>Difference commands </h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>git diff</td>
        <td>Shows changes made in the files</td>
    </tr>
    <tr>
        <td>git status</td>
        <td>Shows untracked and tracked files</td>
    </tr>
    <tr>
        <td>git log</td>
        <td>Shows the commit logs</td>
    </tr>
    <tr>
        <td>git log -p</td>
        <td>Shows all the changes made in the repo</td>
    </tr>
</table>

<br/>

<h3>Stagging commands </h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>git add \* </td>
        <td>Adds untracked files</td>
    </tr>
    <tr>
        <td>git checkout [file_name]</td>
        <td>Revert changes to modified files before they are staged</td>
    </tr>
    <tr>
        <td>git reset HEAD [file_name]</td>
        <td>Removes files from staging area</td>
    </tr>
</table>

<br/>

<h3>Commit commands</h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>git show</td>
        <td>Returns a list of commits andd commit id made in the repo</td>
    </tr>
    <tr>
        <td>git show [commit-id]</td>
        <td>Shows the changes made in the repo at that commit</td>
    </tr>
    <tr>
        <td>git commit -m "message"</td>
        <td>Commits the changes</td>
    </tr>
    <tr>
        <td>git commit -a -m "message"</td>
        <td>Stages files automatically and commits the changes</td>
    </tr>
    <tr>
        <td>git commit --amend</td>
        <td>Overwrite the previous commit</td>
    </tr>
</table>

<br/>

<h3>Rollback commands </h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>git revert HEAD</td>
        <td>makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.</td>
    </tr>
    <tr>
        <td>git revert HEAD^</td>
        <td>reverts back to last commit while keeping the changes</td>
    </tr>
    <tr>
        <td>git checkout HEAD~X</td>
        <td>Here X is the number of comits to go back to</td>
    </tr>
    <tr>
        <td>git revert [commit-id]</td>
        <td>roll back to the time where the specified commit was made with a new commit to the the repo
</td>
    </tr>
</table>

<br/>

<h3>Update to Github commands </h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>git pull origin master</td>
        <td>Updates changes from the repo</td>
    </tr>
    <tr>
        <td>git push origin master</td>
        <td>Updates to the remote repo</td>
    </tr>
    <tr>
        <td>git push --force origin master</td>
        <td>Force update the remote repo</td>
    </tr>
</table>


<br/>

<h3>Branch and Merge commands </h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>git branch</td>
        <td>Shows all the branches</td>
    </tr>
    <tr>
        <td>git branch -a</td>
        <td>Shows all the branch of the original repository</td>
    </tr>
    <tr>
        <td>git branch [branch_name]</td>
        <td>Creates a new branch</td>
    </tr>
    <tr>
        <td>git branch -d [branch_name]</td>
        <td>Deletes a local repo branch</td>
    </tr>
    <tr>
        <td>git branch -D [branch_name]</td>
        <td>Forcibly deletes the branch</td>
    </tr>
    <tr>
        <td>git branch --merged</td>
        <td>Shows all the branches we have merged</td>
    </tr>
    <tr>
        <td>git checkout [branch_name]</td>
        <td>Changes the branch</td>
    </tr>
    <tr>
        <td>git checkout -b [branch_name]</td>
        <td>Create a new branch and change to that branch</td>
    </tr>
    <tr>
        <td>git merge [branch_name]</td>
        <td>Merges branch to the current branch</td>
    </tr>
    <tr>
        <td>git merge --abort</td>
        <td>If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action</td>
    </tr>
    <tr>
        <td>git push -u origin [branch_name]</td>
        <td>Creates branch in remote repo</td>
    </tr>
    <tr>
        <td>git push origin --delete [branch_name]</td>
        <td>Deletes a remote repo branch</td>
    </tr>
    <tr>
        <td>git rebase [origin_branch_name]</td>
        <td>Rebase the origin branch from where the current branch is generated</td>
    </tr>
    <tr>
        <td>git rebase --continue</td>
        <td>continue rebase process</td>
    </tr>
</table>
