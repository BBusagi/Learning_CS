// 具体产品：减法运算。
// 负责实现 Operation 中定义的 GetResult 行为。
sealed class OperationSub : Operation
{
    public override string Symbol => "-";

    public override double GetResult()
    {
        return NumberA - NumberB;
    }
}
