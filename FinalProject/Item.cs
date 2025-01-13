// Item.cs

using System;

public abstract class Item {
    // private string _name { get; private set; }
    // private string _description { get; private set; }
    // public int _value { get; private set; }
    protected string _name;
    protected string _description;

    // public Item(string name, string description, int value) {
    //     Name = name;
    //     Description = description;
    //     Value = value;
    // }

    public Item(string name) {
        _name = name;
    }

    // public abstract void Use();

    public abstract Boolean IsUsableInBattle();

    public string GetName() {
        return _name.ToUpper();
    }

    public abstract int ReturnValue();

}
