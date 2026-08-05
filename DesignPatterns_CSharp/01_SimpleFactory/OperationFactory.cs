// 简单工厂：根据外部传入的运算符创建对应的具体运算对象。
// 新增运算类型时，通常需要新增一个具体产品类，并在这里补充分支。
static class OperationFactory
{
    public static Operation CreateOperation(string? operateSymbol)
    {
        return operateSymbol switch
        {
            "+" => new OperationAdd(),
            "-" => new OperationSub(),
            "*" => new OperationMul(),
            "/" => new OperationDiv(),
            _ => throw new NotSupportedException($"暂不支持运算符：{operateSymbol}")
        };
    }
}
