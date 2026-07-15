# Caching
+ 降低数据库负载，大幅削减延迟，但是有缓存失效和故障处理的新问题  

|类型|位置|作用范围|延迟|规模|典型用途|
| - | - | - | - | - | - |
| External Cache | 独立缓存服务（Redis等） | 所有服务共享 | 低  | 大 | 热数据/数据库加速 |
| CDN | 边缘节点（离用户近） | 全球用户 | 很低 | 超大 | 静态资源分发 |
| Client Cache | 用户设备 | 单用户 | 最低 | 很小 | UI/接口缓存 |
| In-Process Cache | 应用进程内 | 单实例 | 极低 | 很小 | 高频小数据 |

### 缓存架构模式
+ Cache-Aside
+ Write-Through 先写入缓存再同步数据库
+ Write-Behind 先写入缓存再异步写入数据库
+ Read-Through - Write-Through组合管理
  
### 缓存淘汰策略
+ LRU（最近最少使⽤，Least Recently Used）
+ LFU（最不常使⽤，Least Frequently Used）
+ FIFO（先进先出，First In First Out）
+ TTL（存活时间，Time To Live）

### 常见缓存问题
+ 缓存雪崩（Cache Stampede / Thundering Herd）
  + 请求合并（Request coalescing / Single flight）
  + 缓存预热（Cache warming）
+ 缓存⼀致性（Cache Consistency）
  + 写入时失效缓存
  + 短 TTL 容许过时数据
  + 接受最终⼀致性
+ 热 Key（Hot Keys）
  + 拷⻉热 key
  + 加⾏程内备援缓存
  + 套⽤ Rate Limiting

### 面试重点
+ 什么时候提到缓存 - 确认性能问题、⽤⼤概的数字量化它、说明缓存如何解决它
  + 读取密集的工作负载
  + 昂贵的查找
  + 数据库CPU负载过高
  + 延迟需求
+ 缓存策略
  1. 确认瓶颈
  2. 决定瓶颈
  3. 选择缓存架构
  4. 设置淘汰策略
  5. 说明缺点

### 总结
+ 缓存是将频繁访问的数据放在内存中，将读取跳过数据库