using System.Reflection.Metadata;

abstract class Consumable : Item {

    // public Consumable(string name, string description, int value, int quantity) : base(name, description, value) {
    //     Quantity = quantity;
    // }

    public Consumable(string name) : base(name) {
        _name = name;
    }

    public override Boolean IsUsableInBattle() { return true; }

}
