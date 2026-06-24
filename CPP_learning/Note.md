# 
### 95 How to REALLY learn C++
+ 学习cpp之后，去查看真实的opensource cpp项目
+ 除了教材之外，还需要真实环境和使用
+ 从自己感兴趣的部分开始
+ 可以尝试bug bounty program
+ PVS studio 静态代码分析

### 2 How to Setup C++ on Windows
+ VS IDE
+ Visual Assist
+ VS setting

### 4 How to Setup C++ on Linux
+ WSL
+ sudo / apt-get / update - 管理员 / 包管理 / 更新
+ 安装包推荐 vim g++ codelite cmake
+ touch - 更新时间戳并创建
+ CMakeLists.txt - 如何构建项目
+ build.sh - 如何执行构建流程
+ codelite进行build并执行

### 8/9/12/14/15
+ unsigned 无符号位为32位，正常为符号位+31位
+ char short int long longlong float double bool
+ sizeof → byte
+ pointer* reference&
+ 通过debug模式和关闭优化来通过反汇编(disassembly)查看是否存在优化方法
+ 可以通过if来判断空指针的问题