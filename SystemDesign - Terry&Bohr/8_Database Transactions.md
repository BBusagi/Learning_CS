# Database Transactions
+ Transactions 将相关联的数据操作做为一个整体来保证运行

### ACID 
+ Atomicity 原子性
  + 要么成功 要么失败，不存在中间状态
  + 中途失败，全部回滚，WAL实现
+ Consistency 一致性
  + 数据库只能从一个合法状态转移到另一个合法状态
  + 商业逻辑上的一致性
+ Isolation 隔离性
  + 多个Transaction相互不应该干涉
+ Durability
  + 一旦commit之后就应该永久保留

### Isolation level
+ 从低到高 Read Uncommitted, Read Committed, Repeatable Read, Serializable
+ 仓库超卖本质为lost update，用Select For Update或原子Update即可，只有在金融等交易才会使用Serializable

### 三种并发异常
+ Dirty Read - 尚未commit
+ Non-repeatable Read - 同一笔数据有更新
+ Phantom Read - 查找范围有变化

### Multi-Version Concurrency Control
+ 对同一数据保持多版本，解决**读**的问题
+ 允许并行处理，旧版本在使用完毕后进行回收
+ Lost Update 存在**写**的问题
  + 乐观锁 更新时查看版本，适用于不常有冲突
  + 悲观锁 允许的时候将数据锁住，直到transaction完成，但是有Deadlock的问题

### 分布式Transactions
+ 2PC 两阶段提交
  + 先询问所有节点是否准备好
  + 所有节点Yes，进行commit，任一回答No，全部rollback
  + 协调者如果在二阶段前崩溃，需要人工干涉修复
+ Saga 将transaction转化为允许补偿的本地transaction

### 面试重点
+ 适用场景
  + 多步骤原子操作
  + 添加锁来防止Lost Update
  + 数据一致性要求较高
+ 并说明隔离等级
+ 跨服务挑战
+ 悲观锁需要提及Deadlock问题