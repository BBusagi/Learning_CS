// 具体产品：除法运算。
// 除了实现除法算法，还负责处理除数为 0 的业务规则。
sealed class OperationDiv : Operation
{
    public override string Symbol => "/";

    public override double GetResult()
    {
        if (NumberB == 0)
        {
            throw new DivideByZeroException("除数不能为 0。");
        }

        return NumberA / NumberB;
    }
}
