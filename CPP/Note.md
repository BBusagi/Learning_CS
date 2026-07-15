# 

## Mianshi
### C++的难点 -> 资源所有权设计（Ownership Design）
### cpp vs csharp
C++ 是提前编译型语言。源码经过预处理、编译、链接，直接生成和平台绑定的原生机器码，运行时不需要任何运行时环境，直接跑在 CPU 上，没有垃圾回收。
C# 不一样，它先编译成平台无关的中间语言 IL，运行时再由 CLR 的 JIT 把 IL 即时翻译成机器码，并提供垃圾回收、类型安全这些托管服务。
所以 C++ 贴硬件、内存管理，性能，和优化；C# 可移植、开发快，但带运行时和 GC 的开销。

### 为什么游戏/主机用 C++
因为热路径上不能容忍 GC 那种不可控的停顿，也不想付 JIT 预热的代价，要的是可预测的性能。

### C++编译过程
1 预处理，展开所有 include 和宏，生成一个摊平的翻译单元。
2 编译，编译器对每个源文件独立处理——先词法分析切成 token，再语法分析建成抽象语法树 AST，然后做语义检查和优化，最后生成机器码，输出目标文件.obj。
3 链接，把所有目标文件和库拼起来，解析符号引用，生成exe/dll。核心特点是：每个源文件是独立编译的，跨文件的引用要留到链接阶段才对上。

### Linker工作过程
Linker解决的是"跨文件引用"的问题。编译阶段每个源文件是独立编译的，所以当一个文件调用了在别处定义的函数，编译器只能先留一个"待解析的符号",相当于一张欠条。链接器的工作就是把所有目标文件和库收集起来，做符号解析——把每一张欠条对上它真正的定义，再把所有机器码和数据按最终内存布局拼成一个可执行文件。经典的 unresolved external symbol 报错，就是有欠条没找到对应的定义，通常是漏了实现或者库没链进来。
所以在build阶段，需要区分是编译错误还是链接错误

### 静态链接和动态链接的区别
静态链接是把库的机器码直接拼进最终文件；动态链接是运行时再去加载 .dll/.so，文件更小、库能共享，但运行时要能找到那个库。

### Rule of Five
自我管理时需要5类特殊成员:Destructor, Copy Constructor, Copy Assignment, Move Constructor, Move Assignment

### 浅拷贝 vs 深拷贝 vs 移动
浅拷贝会带来析构时候的double delete的问题，

##
### CPP编译 vs CSharp编译
+ C++ AOT 直接编译到原生码
  + x64 Native Tools Command Prompt for VS 可以进行精准控制
  + Preprocess -> Compile -> Link
  > main.cpp -> Preprocessor -> 展开后的源码 -> Lexer -> Token -> Parser -> AST  -> Assembler -> Compiler -> obj -> Linker -> exe/dll
  + 特点 原生二进制 不需要运行时
+ C# 两段式编译
  + IL -> CLR + JIT
  + 特点 可移植IL，需要运行时，GC JIT等额外开销

### 存储单元结构
+ SSD/Disk -> RAW(Stack, Heap, Global, Code) -> Cache(L3, L2, L1) -> Register

### SW的分类
+ Realtime，Interactive， Throughout， Batch Processing， Server/Backend, Embedded

### . vs ->
+ `.` - 对象成员
+ `->` - 指针对象的成员 = `(*player).xxx`
### 字节序endianness
+ 大端序 vs 小端序

### malloc & GC
+ 计算机科学的所有问题都能靠加一层中间层来解决——除了"中间层太多"这个问题本身
+ malloc无法做到压缩，就在于记录单位是地址而不是编号
+ GC语言可以进行GC就在于，在CLR层面上有人进行地址和编号的翻译，然后压缩
+ 现代malloc获得的就已经是虚拟地址而不是物理地址，MMU+TLB

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
+ pre-processing [vs -> preprocessor to a file]
  + #include #define #if endif #pragma once
  + .i 可以查看预处理后的文件
+ .obj为二进制不可读，可转为.asm可读文件 [vs -> assembler output]

### 7 How the C++ Linker Works
+ 连接不同的obj, lib
+ 明确是compile error还是link error
+ symbol error
  + static, inline, 保持只定义一次

### 16 POINTERS
+ pointer(*) 保存内存地址的数字
+ 指针不止有地址信息还有类型信息，所以需要存在不同类型，但是不重要
+ 可以通过VS的Memory工具查看
+ 通过*ptr来访问
```cpp
char* buffer = new char[8]; //heap中 申请8个char
memset(buffer,0,8);         //清空原有的数据
delete[] buffer;            //删除
```
+ delete表示释放内存，但是heap不清空，stack会自动清空
+ `char**` - 二级指针

### 17 REFERENCES
+ reference是pointer的上层语法糖syntax sugar
+ ref必须初始化，并且无法修改

### 19 CLASSES vs STRUCTS
+ class 默认private
+ struct 默认public, 兼容c

### 42 Object Lifetime (Stack/Scope Lifetimes)
+ cpp中存在两种lifetime,heap和stack
+ stack在结束后自动清空, heap不自动清空
+ 存在多种方法在scope外保留stack值
+ 也可以创建scope周期内的heap值

### 54 Stack vs Heap Memory （经典追问）
+ 物理存放地点 RAM，最大的不同在于allocation
+ stack的分配方式是线性的，紧凑的，但是不自由
+ heap从malloc中获取满足长度的free space，是离散的，后续扩张及其消耗性能，但是自由
+ 可以通过VS的Assembly With Source Code进行查看
+ ref
  + [dlmalloc](https://gee.cs.oswego.edu/dl/html/malloc.html)
  + [jemalloc](https://people.freebsd.org/~jasone/jemalloc/bsdcan2006/jemalloc.pdf)

### 55 Macros
+ 自定义宏可分割不同环境 [vs -> preprocessor definitions]
+ 宏必须在一行内声明，或者使用\
+ 可以利用内置的宏指令，例如new的时候追踪size或者memallo

### 38 The NEW Keyword
+ 五步，计算大小 -> 原始内存 -> malloc -> 构造函数 -> **返回指针**
+ new是一个运算符，并且允许重构
+ 用了之后必须删除来free

### 25/68 Destructor/Virtual Destructor
+ `~`，lifertime结束的时候自动调用
+ `virtual`: 编译器不绑定，以运行时对象为准

### 43 SMART POINTERS（RAII 核心）
+ std::unique_ptr：唯一拥有
+ std::shared_ptr：多个拥有
+ std::weak_ptr：仅观察，不拥有

### 44 Copying and Copy Constructors
+ shallow copy vs deep copy
+ copy带有指针的类的时候，会导致二次析构
+ 通过复制构造来指定copy的具体方法

### 60 Why I don't "using namespace std"
+ 部分库会重载关键词，导致难以区分标准库和第三方库

### 85 lvalues and rvalues
+ lvalue 长期对象, & 左值引用
+ rvalue 临时对象, && 右值引用, 常用于优化

### 89/90 Move Semantics / std::move and the Move Assignment Operator
+ 移动 = 偷取所有权
+ 用`std::move`实现**移动构造函数**，用于新建对象
+ Move Assignment Operator - **移动赋值操作符**，用于已有对象 

### 33 CONST
+ `const` 可以在多种位置，优先修饰左侧
+ class const后置，承诺不修改对象， multable 特例声明

### 35 Member Initializer Lists (Constructor Initializer List)
+ 初始化顺序需要和声明顺序保持一致
+ 成员初始化列表将会替代声明时默认初始化，避免初始化两次，保持性能高效

### 53 Templates 
+ 与c#中的泛型相似但更加强大
+ `template<typename T>`，也可以在调用时通过<>显式指定传参
+ 双刃剑，可用在重载，但是需要避免过度复杂

### 45 The Arrow Operator
+ 指针调用方法时使用 `->`
+ 允许重载
+ 可以获得内存的offset

### 46/47/106 `std::vector` - Dynamic Arrays / Optimizing / Wrong using
+ 速度优化不是标准库的目标
+ vector其实是ArrayList，动态扩容，连续内存，随机访问O(1)
+ 创建vector的时候优先使用对象，然后是指针
+ `for (Type variable : Container)` -- foreach
+ 优化点
  1. 简化从main中移动到vector中 - `.emplace_back`
  2. 简化扩容过程，提前告知内存 - `.reserve` / `.resize`(会初始化)
+ 性能是检验标准 *内置一个mem统计工具
  1. 能用array就不要用vector
  2. 预先分配内存
  3. 用移动代替复制vector