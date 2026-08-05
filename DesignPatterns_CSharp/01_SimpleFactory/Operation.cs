// 抽象产品：定义所有运算类共同拥有的数据和行为。
// 具体的算法实现由子类完成，客户端只依赖这个抽象类型。
abstract class Operation
{
    public double NumberA { get; set; }

    public double NumberB { get; set; }

    public abstract string Symbol { get; }

    public abstract double GetResult();
}
