class BurnCure : Consumable {
    public BurnCure(string name) : base(name) {
        _name = name;
        _description = "Cures burn";
    }

    public override int ReturnValue() {
        return 1;
    }

}
