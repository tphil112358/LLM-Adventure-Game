using System.Runtime;

abstract class Enemy {

    // MEMBER VARIABLES / ATTRIBUTES

    protected string _name;
    protected int _hp;
    protected int _maxHp;
    protected List<Item> _droppableItems;

    // MEMBER METHODS / FUNCTIONS / BEHAVIORS

        // CONSTRUCTORS ( METHODS )

        // GETTERS / ACCESSORS ( METHODS )

        // SETTERS / MUTATORS ( METHODS )

        // OTHER METHODS

    public abstract List<Boolean> DoStatusAffect(List<Boolean> playerCurrentStatuses);

    public int GetHealthFactor() {
        if (_hp > 0) {
            int factor = Convert.ToInt32((double)_hp / ((double)_maxHp / 50.0));
            if (factor > 50) {
                factor = 50;
            }
            return factor;
        }
        else {
            return 0;
        }
    }

    public Boolean IsAlive() {
        if (_hp >= 1) {
            return true;
        }
        else {
            return false;
        }
    }

    public virtual string GetName() {
        return _name;
    }

    public abstract int Attack();

    public void ReceivesDamage(int damage) { _hp -= damage; }

    public abstract Item DropItem();

}
