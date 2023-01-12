## Git 常用命令

git init
初始化git仓库

git status
查看修改文件信息

git add file
添加文件到暂存区

git add .
添加所有修改文件到暂存区

git log
查看之前git commit 的记录

git commit -m "修改的信息"
commit 本次修改

git checkout 上次版本号
从上个版本创建新的branch版本号可通过git log 查看）

git branch
查看所有的branch

git branch 名称
创建branch

git checkout 分支名称

git checkout -b 分支名称
创建并进入


git merge 分支名称
(在master 下运行)将分支合并到master

git switch 分支名称
进入分支

git switch -c 分支名称
创建并进入分支

git ls-files
查看文件

git rm 文件名
移除文件


git restore 文件名
恢复还未加入暂存区的文件到上次commit

git restore .
恢复还未加入暂存区的所有文件到上次commit

git clean -dn 
显示将要清除的还未加入暂存区的文件

git clenn -df
强制清除还未加入暂存区的文件

git restore --staged <file>
作用是将暂存区的文件从暂存区撤出，但不会更改文件

git restore <file>
表示将在工作空间但是不在暂存区的文件撤销更改

git reset HEAD~1
跳回上一个commit (同时清空暂存区, 不清楚工作空间)

git reset --soft HEAD~1
跳回上一个commit (不清空暂存区和工作空间)

git reset --soft HEAD~1
跳回上一个commit (清空暂存区和工作空间)






 




