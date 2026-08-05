// 客户端：负责接收超市收银输入，选择具体策略，并通过 CashContext 得到最终应收金额。
// 纯策略模式下，客户端需要知道并创建具体策略对象，再把它交给上下文使用。
Console.WriteLine("策略模式示例：超市收银打折");
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
    var cashSuper = CreateCashSuper(promotionType);
    var cashContext = new CashContext(cashSuper);
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

static CashSuper CreateCashSuper(string? promotionType)
{
    return promotionType switch
    {
        "1" => new CashNormal(),
        "2" => new CashRebate(0.8),
        "3" => new CashReturn(300, 100),
        _ => throw new NotSupportedException($"暂不支持促销类型：{promotionType}")
    };
}
