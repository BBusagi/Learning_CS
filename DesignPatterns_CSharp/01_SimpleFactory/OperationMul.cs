// 具体产品：乘法运算。
// 负责实现 Operation 中定义的 GetResult 行为。
sealed class OperationMul : Operation
{
    public override string Symbol => "*";

    public override double GetResult()
    {
        return NumberA * NumberB;
    }
}
