// Sword.cs

using System;

public class Sword : NonConsumable {
    private int _damageIncreaseAmount;

    // public Sword(string name, string description, int value, int damageIncreaseAmount) : base(name, description, value) {
    //     this.damageIncreaseAmount = damageIncreaseAmount;
    // }

    public Sword(string name, int damageIncreaseAmount) : base(name) {
        _name = name;
        _damageIncreaseAmount = damageIncreaseAmount;
        _description = $"Hold this {_name.ToUpper()} in your bag to increase your base damage by {_damageIncreaseAmount}!";
    }

    public override int ReturnValue() {
        return _damageIncreaseAmount;
    }

}
