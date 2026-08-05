// 具体策略：正常收费。
// 没有任何折扣或返利，直接返回原始金额。
sealed class CashNormal : CashSuper
{
    public override string Name => "正常收费";

    public override double AcceptCash(double money)
    {
        return money;
    }
}
