# 
##
### CPP编译 vs CSharp编译
+ C++ AOT 直接编译到原生码
  + Preprocess -> Compile -> Link
  > main.cpp -> Preprocessor -> 展开后的源码 -> Lexer -> Token -> Parser -> AST  -> Assembler -> Compiler -> obj -> Linker -> exe/dll
  + 特点 原生二进制 不需要运行时
+ C# 两段式编译
  + IL -> CLR + JIT
  + 特点 可移植IL，需要运行时，GC JIT等额外开销

### R 存储单元结构
+ SSD/Disk -> RAW(Stack, Heap, Global, Code) -> Cache(L3, L2, L1) -> Register

### 字节序endianness
+ 大端序 vs 小端序

## Cherno CPP
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

### 8/9/12/14/15 基础语法
+ unsigned 无符号位为32位，正常为符号位+31位
+ char short int long longlong float double bool
+ bit(1/0) -> 一个16进制(4bit) -> byte(2个16进制/8bit) -> int = 4byte(32位)
+ sizeof → byte
+ pointer* reference&
+ 通过debug模式和关闭优化来通过反汇编(disassembly)查看是否存在优化方法
+ 可以通过if来判断空指针的问题

### 5 How C++ Works
+ << 左移 / console output
+ 重要的两个参数
  + 模式 Debug / Release
  + 平台 x86 / x64
+ cpp --Compiler-> obj --Linker-> exe

### 6 How the C++ Compiler Works
+ text -> Abstract Syntax Code
+ file has no meaning,(unlike java c#)
+ pre-processing
  + #include #define #if endif #pragma once
  + .i可以查看预处理后的文件
+ .obj为二进制不可读，但是可以转化为.asm可读文件

### 7 How the C++ Linker Works
+ 连接不同的obj, lib
+ 明确是compile error还是link error
+ symbol error
  + static, inline, 保持只定义一次

### 16 POINTERS in C++
+ pointer(*) 保存内存地址的数字
+ 指针不止有地址信息还有类型信息，所以需要存在不同类型，但是不重要
+ 可以通过VS的Memory工具查看
+ 通过*ptr来访问
```cpp
char* buffer = new char[8]; //heap中 申请8个char
memset(buffer,0,8);         //清空原有的数据
delete[] buffer;            //删除
```
+ cpp中存在两种存储方式heap和stack
+ delete表示释放内存，但是heap不清空，stack会自动清空
+ `char**` - 二级指针

### 17 REFERENCES in C++

#42 Object Lifetime
#54 Stack vs Heap（经典追问）
#38 new
#25/#68 Destructor/Virtual Destructor
#43 Smart Pointers（RAII 核心）
#44 Copy Constructor
#85 lvalue/rvalue
#89 Move Semantics + #90 std::move（经典追问）
#33 const
#35 Member Initializer List
#53 Templates
#46/#47/#106 vector 三连
