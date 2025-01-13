abstract class Boss : Enemy {

    protected int _internalScore;

    public Boss (int score) {
        _droppableItems.Add(new Shield($"+{score * 10} SHIELD", score * 10));
        _droppableItems.Add(new Sword($"+{score * 10} SWORD", score * 10));
    }

    // MEMBER VARIABLES / ATTRIBUTES

    // List<Item> _droppableItems;

    // protected List<Item> _droppableItems;

    // MEMBER METHODS / FUNCTIONS / BEHAVIORS

    // CONSTRUCTORS ( METHODS )

    // GETTERS / ACCESSORS ( METHODS )

    // SETTERS / MUTATORS ( METHODS )

    // OTHER METHODS

    // public Item DropItem() {
    //     Random rand = new Random();
    //     int index = rand.Next(0, _droppableItems.Count);
    //     return _droppableItems[index];
    // }

    public override Item DropItem() {
        Random rand = new Random();
        int index = rand.Next(0, 2);
        return _droppableItems[index];
    }

    public override List<Boolean> DoStatusAffect(List<Boolean> playerCurrentStatuses) {
        return playerCurrentStatuses;
    }

}
