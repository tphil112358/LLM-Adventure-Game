using System.Net;
using System.Reflection.Metadata.Ecma335;

class Player {

    // MEMBER VARIABLES / ATTRIBUTES

    private string _name;
    private int _hp;
    private int _maxHp;
    private int _attackStat;
    private List<Item> _items;

    private List<Boolean> _statuses;

    // MEMBER METHODS / FUNCTIONS / BEHAVIORS

        // CONSTRUCTORS ( METHODS )

    public Player(string nameP) {
        _name = nameP;
        _hp = 1000;
        _maxHp = 1000;
        _attackStat = 100;
        _items = new List<Item>();
        // _items.Add(new Sword("Confusion Blade", 500));
        // _items.Add(new Shield("Confusion Shield", 50));
        //           BURN   FROZEN
        _statuses = [false, false];
    }

        // GETTERS / ACCESSORS ( METHODS )

        // SETTERS / MUTATORS ( METHODS )

        // OTHER METHODS
    
    public string GetName() { return _name; }

    public int GetHealthFactor() {
        if (_hp > 0) {
            return _hp / (_maxHp / 50);
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

    public void ReceivesDamage(int damage) {
        int damageToReceive = damage;
        foreach (Item item in _items) {
            if (item is Shield) {
                damageToReceive -= item.ReturnValue();
            }
        }
        if (damageToReceive < 0) {
            damageToReceive = 1;
        }
        if (_statuses[1]) {
            damageToReceive += 50;
        }
        _hp -= damageToReceive;
    }

    public int DealsDamage() {
        int damageVal = _attackStat;
        foreach (Item item in _items) {
            if (item is Sword) {
                damageVal += item.ReturnValue();
            }
        }
        return damageVal;
    }

    public List<List<string>> GetItemValidReturnList() {
        List<List<string>> outLoLoS = new List<List<string>>();
        int indexer = 1;
        foreach (Item item in _items) {
            if (item.IsUsableInBattle()) {
                outLoLoS.Add([$"{indexer}", $"{indexer}"]);
            }
        }
        outLoLoS.Add(["6", "HOME"]);
        return outLoLoS;
    }

    public List<string> GetItemChoiceBoxList() {
        CHString chstring = new CHString();
        List<string> outLoS = new List<string>();
        for (int i = 0; i < 5; i ++) {
            if (i < _items.Count()) {
                if (_items[i].IsUsableInBattle()) {
                    outLoS.Add(chstring.LeftAligned($"  {i + 1}. USE {_items[i].GetName()}", 24));
                }
                else {
                    outLoS.Add(chstring.DarkGrey(chstring.LeftAligned($"  {i + 1}. {_items[i].GetName()}", 24)));
                }
            }
            else {
                outLoS.Add(chstring.DarkGrey(chstring.LeftAligned($"  {i + 1}. EMPTY", 24)));
            }
        }
        outLoS.Add("  6. CANCEL");
        return outLoS;
    }

    public Boolean IsBurned() {
        return _statuses[0];
    }

    public Boolean IsFrozen() {
        return _statuses[1];
    }

    public void GetsBurned() {
        _hp -= 50;
    }

    public void DropItem() {
        _items.RemoveAt(0);
    }

    public Boolean BagIsFull(){
        if (_items.Count > 5) {
            return true;
        }
        else {
            return false;
        }
    }

    public string GetFirstItemName() {
        return _items[0].GetName();
    }

    // public List<int> UseItem(int itemIndex) {
    //     _items[itemIndex].Use();
    // }

    public void GetItem(Item item) {
        _items.Add(item);
    }

    public List<Item> GetItems() {
        return _items;
    }

    public void RemoveItemAt(int index) {
        _items.RemoveAt(index);
    }

    public void SetBurnStatus(Boolean burn) {
        _statuses[0] = burn;
    }

    public void SetFrostStatus(Boolean frost) {
        _statuses[1] = frost;
    }

    public List<Boolean> GetStatuses() {
        return _statuses;
    }

    public void SetStatuses(List<Boolean> statuses) {
        _statuses = statuses;
    }

}
