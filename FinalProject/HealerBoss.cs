class HealerBoss : Boss {

    // MEMBER VARIABLES / ATTRIBUTES

    private int _rank;

    // MEMBER METHODS / FUNCTIONS / BEHAVIORS

        // CONSTRUCTORS ( METHODS )

    public HealerBoss(int score) : base(score) {
        // From Enemy
        _name = "MED-PUNK";
        _maxHp = 200 + (score * 10);
        _hp = _maxHp;
        // From Boss
        // _droppableItems = [new Item()];
        // From Self
        Random rand = new Random();
        _rank = rand.Next(1, 3);
        _internalScore = score;
    }

        // GETTERS / ACCESSORS ( METHODS )

        // SETTERS / MUTATORS ( METHODS )

        // OTHER METHODS

    public override int Attack() {
        Random rand = new Random();

        int startFactor = rand.Next(_internalScore * 2 * 10, _internalScore * 4 * 10);
        int damage = (_rank / 4) * startFactor;
        _hp += ((4 - _rank) / 4) * startFactor;
        if (_hp > _maxHp) {
            _hp = _maxHp;
        }

        return damage;
    }

    public override string GetName() { return $"RANK {_rank} {_name}"; }

}
