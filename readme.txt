git相关命令
将已有项目合并都远程仓库步骤
1、在http://github.com上创建一个仓库
2、在已有项目目录下执行git init
3、在已有项目目录下执行it add .，将所有文件加入到本地仓库
4、设置本地用户
git config --global user.email "zxqrenwen@163.com"
git config --global user.name "zxqrenwen"
5、将文件提交到本地仓库
git commit -m "first commit"
6、本地仓库与远程仓库关联
git remote add origin https://github.com/allening/flasky.git
7、将本地仓库push到远程仓库
git push -u origin master

后续本地提交代码到远程仓库
1）添加全部修改的代码，准备提交
git add .
2）将修改后的代码先提交到本地仓库
git commit -m ‘提交说明’
3）将 github 的代码拉取到本地，这样在 merge 解决冲突的时候稍微简便些。默认拉取到 master分支（如果只是自己做这个项目，可以忽略pull）
git pull
4）将代码推送到 github , 默认推送到 别名为 origin 的仓库中的 master 分支上。
git push
注意事项：
如果有多个远程仓库 或者 多个分支， 并且需要将代码推送到指定仓库的指定分支上，那么在 pull 或者 push 的时候，就需要 按照下面的格式书写：
git pull 仓库别名 仓库分支名 
git push 仓库别名 仓库分支名

git其他操作，初始化git仓库（git init,git clone）
1、git clone
git clone git://github.com/someone/some_project.git some_project 
将远程项目完全clone到本地目录some_project
查看远程仓库：$ git remote -v
