// 上下文：持有一个具体收费策略，并把收费请求委托给该策略对象。
// 这里结合简单工厂，根据促销类型创建具体策略，让客户端代码更简洁。
sealed class CashContext
{
    private readonly CashSuper _cashSuper;

    private CashContext(CashSuper cashSuper)
    {
        _cashSuper = cashSuper;
    }

    public string PromotionName => _cashSuper.Name;

    public static CashContext CreateByPromotionType(string? promotionType)
    {
        var cashSuper = promotionType switch
        {
            "1" => new CashNormal(),
            "2" => new CashRebate(0.8),
            "3" => new CashReturn(300, 100),
            _ => throw new NotSupportedException($"暂不支持促销类型：{promotionType}")
        };

        return new CashContext(cashSuper);
    }

    public double GetResult(double money)
    {
        return _cashSuper.AcceptCash(money);
    }
}
