// Shield.cs

using System;

public class Shield : NonConsumable {
    private int _damageReductionAmount;

    // public Shield(string name, string description, int value, int damageReductionAmount) : base(name, description, value) {
    //     this.damageReductionAmount = damageReductionAmount;
    // }

    public Shield(string name, int damageReductionAmount) : base(name) {
        _name = name;
        _damageReductionAmount = damageReductionAmount;
        _description = $"Hold this {_name.ToUpper()} in your bag to increase your base defence by {_damageReductionAmount}!";
    }

    // public override void Use() {
    //     // Apply the damage reduction effect description
    //     Console.WriteLine($"Used {Name}. Decreases damage taken by {damageReductionAmount}.");
    // }

    public override int ReturnValue() {
        return _damageReductionAmount;
    }

}
