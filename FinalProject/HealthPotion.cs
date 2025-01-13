class HealthPotion : Consumable {

    private int _healFactor;
    public HealthPotion(string name, int healFactor) : base(name) {
        _name = $"+{healFactor} HEALTH";
        _description = "Heals the player!";
        _healFactor = healFactor;
    }

    public override int ReturnValue() {
        return _healFactor * -1;
    }

}
