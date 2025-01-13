// NonConsumable.cs

using System;

public abstract class NonConsumable : Item {
    // public NonConsumable(string name, string description, int value)
    //     : base(name, description, value) {
    // }

    public NonConsumable(string name) : base(name) {
        _name = name;
    }

    public override Boolean IsUsableInBattle() {
        return false;
    }

    // Abstract method for using non-consumable items

}
