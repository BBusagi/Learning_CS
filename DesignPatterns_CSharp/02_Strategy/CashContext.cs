// 上下文：持有一个具体收费策略，并把收费请求委托给该策略对象。
// 纯策略模式下，上下文不负责创建策略，只负责使用客户端传入的策略。
sealed class CashContext
{
    private readonly CashSuper _cashSuper;

    public CashContext(CashSuper cashSuper)
    {
        _cashSuper = cashSuper;
    }

    public string PromotionName => _cashSuper.Name;

    public double GetResult(double money)
    {
        return _cashSuper.AcceptCash(money);
    }
}
