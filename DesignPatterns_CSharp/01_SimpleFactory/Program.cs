// 客户端：负责接收用户输入，调用简单工厂创建运算对象，并输出计算结果。
// 客户端不直接 new 具体运算类，从而把对象创建逻辑交给 OperationFactory 管理。
Console.WriteLine("简单工厂模式示例：计算器");
Console.WriteLine("支持的运算符：+  -  *  /");

try
{
    Console.Write("请输入数字 A：");
    var numberA = ReadNumber();

    Console.Write("请输入运算符：");
    var operateSymbol = Console.ReadLine();

    Console.Write("请输入数字 B：");
    var numberB = ReadNumber();

    var operation = OperationFactory.CreateOperation(operateSymbol);
    operation.NumberA = numberA;
    operation.NumberB = numberB;

    Console.WriteLine($"计算结果：{numberA} {operation.Symbol} {numberB} = {operation.GetResult()}");
}
catch (Exception ex)
{
    Console.WriteLine($"输入或计算错误：{ex.Message}");
}

static double ReadNumber()
{
    var input = Console.ReadLine();

    if (double.TryParse(input, out var number))
    {
        return number;
    }

    throw new ArgumentException("请输入有效数字。");
}
