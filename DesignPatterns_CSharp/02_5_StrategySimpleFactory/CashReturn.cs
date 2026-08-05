// 具体策略：满减返利。
// 当金额达到指定条件时，按倍数减去返利金额，例如满 300 返 100。
sealed class CashReturn : CashSuper
{
    private readonly double _moneyCondition;
    private readonly double _moneyReturn;

    public CashReturn(double moneyCondition, double moneyReturn)
    {
        if (moneyCondition <= 0)
        {
            throw new ArgumentOutOfRangeException(nameof(moneyCondition), "返利条件必须大于 0。");
        }

        if (moneyReturn < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(moneyReturn), "返利金额不能小于 0。");
        }

        _moneyCondition = moneyCondition;
        _moneyReturn = moneyReturn;
    }

    public override string Name => $"满 {_moneyCondition:0} 返 {_moneyReturn:0}";

    public override double AcceptCash(double money)
    {
        if (money < _moneyCondition)
        {
            return money;
        }

        return money - Math.Floor(money / _moneyCondition) * _moneyReturn;
    }
}
