// 抽象策略：定义所有收费算法都必须实现的统一接口。
// 不同促销方式只需要继承它，并实现自己的收费算法。
abstract class CashSuper
{
    public abstract string Name { get; }

    public abstract double AcceptCash(double money);
}
