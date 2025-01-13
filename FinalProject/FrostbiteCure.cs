class FrostbiteCure : Consumable {
    public FrostbiteCure(string name) : base(name) {
        _name = name;
        _description = "Cures frostbite!";
    }

    public override int ReturnValue() {
        return 1;
    }

}
