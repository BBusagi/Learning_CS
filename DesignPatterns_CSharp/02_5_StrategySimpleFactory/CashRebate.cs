// 具体策略：打折收费。
// 通过传入折扣率控制折扣力度，例如 0.8 表示打八折。
sealed class CashRebate : CashSuper
{
    private readonly double _moneyRebate;

    public CashRebate(double moneyRebate)
    {
        if (moneyRebate < 0 || moneyRebate > 1)
        {
            throw new ArgumentOutOfRangeException(nameof(moneyRebate), "折扣率必须在 0 到 1 之间。");
        }

        _moneyRebate = moneyRebate;
    }

    public override string Name => $"打 {_moneyRebate * 10:0.#} 折";

    public override double AcceptCash(double money)
    {
        return money * _moneyRebate;
    }
}
