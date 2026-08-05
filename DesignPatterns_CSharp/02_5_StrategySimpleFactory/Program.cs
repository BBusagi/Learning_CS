// 客户端：负责接收超市收银输入和促销类型，并通过 CashContext 得到最终应收金额。
// 策略模式 + 简单工厂下，客户端不直接创建具体策略，只把促销类型交给上下文。
Console.WriteLine("策略模式 + 简单工厂示例：超市收银打折");
Console.WriteLine("促销类型：");
Console.WriteLine("1. 正常收费");
Console.WriteLine("2. 打八折");
Console.WriteLine("3. 满 300 返 100");

try
{
    Console.Write("请输入商品单价：");
    var price = ReadMoney();

    Console.Write("请输入商品数量：");
    var quantity = ReadQuantity();

    Console.Write("请选择促销类型：");
    var promotionType = Console.ReadLine();

    var originalTotal = price * quantity;
    var cashContext = CashContext.CreateByPromotionType(promotionType);
    var finalTotal = cashContext.GetResult(originalTotal);

    Console.WriteLine($"原价合计：{originalTotal:F2}");
    Console.WriteLine($"促销方案：{cashContext.PromotionName}");
    Console.WriteLine($"应收金额：{finalTotal:F2}");
}
catch (Exception ex)
{
    Console.WriteLine($"输入或计算错误：{ex.Message}");
}

static double ReadMoney()
{
    var input = Console.ReadLine();

    if (double.TryParse(input, out var money) && money >= 0)
    {
        return money;
    }

    throw new ArgumentException("请输入有效的非负金额。");
}

static int ReadQuantity()
{
    var input = Console.ReadLine();

    if (int.TryParse(input, out var quantity) && quantity > 0)
    {
        return quantity;
    }

    throw new ArgumentException("请输入大于 0 的整数数量。");
}
