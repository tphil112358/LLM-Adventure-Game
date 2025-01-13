class HeavyBoss : Boss {

    // MEMBER VARIABLES / ATTRIBUTES

    private int _weight;

    // MEMBER METHODS / FUNCTIONS / BEHAVIORS

        // CONSTRUCTORS ( METHODS )

    public HeavyBoss(int score) : base(score) {
        // From Enemy
        _name = "CHONK";
        _maxHp = 200 + (score * 10);
        _hp = _maxHp;
        // From Boss
        // _droppableItems = [new Item()];
        // From Self
        Random rand = new Random();
        _weight = rand.Next(300 + (score * 10), 300 + ((score + 1) * 10));
    }

        // GETTERS / ACCESSORS ( METHODS )

        // SETTERS / MUTATORS ( METHODS )

        // OTHER METHODS

    public override int Attack() {
        Random rand = new Random();
        int damage = rand.Next(_weight - 50, _weight + 50);
        return damage;
    }

    public override string GetName() { return $"{_weight} POUND {_name}"; }

}
