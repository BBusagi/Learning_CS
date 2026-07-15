Tutorial URL:  
30 天精通 Git 版本控制  
https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-cn/README.md  
**另外详见Git笔记**

### Git逻辑
四大状态：
Untracked，Unmodify，Modified，Staged

![Git层级关系](GitLogic.PNG)

### 添加到库
![GitHub官方说明](GitHub_HowToSetup.PNG)

### Git Bash
由于窗口显示有限，持续按回车显示所有历史记录

### 变量设置
git config -l  
git config --system -l  
path:git/MINGW64/etc/gitconfig

git config --global -l  
path:C:\Users\BBRabbit\gitconfig  
Setting:  
git config --global user.name "[name]"  
git config --global user.email "[email]"  

### 部分常用指令
git init：初始化一个新的 Git 仓库  
git clone：克隆一个远程仓库  
git add：将文件添加到暂存区  
git commit：提交暂存区的更改  
git pull：从远程仓库拉取代码  
git push：将本地更改推送到远程仓库  
git branch：查看、创建或删除分支  
git checkout：切换到一个不同的分支或版本  
git merge：合并两个或更多分支的代码  
git status：查看仓库状态  
git log：查看提交历史

### 删除指令
git branch -a  
git fetch -p

git branch -d <localbranch>

git branch -r  
git push -d origin <remotebranch>  
远程支线

### 大型文件处理
https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github