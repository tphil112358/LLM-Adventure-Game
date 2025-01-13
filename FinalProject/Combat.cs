using System.Runtime.CompilerServices;

class Combat {

    // MEMBER VARIABLES / ATTRIBUTES

    Player _player;
    Enemy _enemy;

    // MEMBER METHODS / FUNCTIONS / BEHAVIORS

        // CONSTRUCTORS ( METHODS )

    public Combat(Player _playerP) {
        _player = _playerP;
    }

        // GETTERS / ACCESSORS ( METHODS )

        // SETTERS / MUTATORS ( METHODS )

        // OTHER METHODS

    public void GetEnemy(int scoreP) {
        
        Random rand = new Random();

        int typeSelection = rand.Next(0, 3);

        if (((scoreP + 1) % 5) == 0) {
            if (typeSelection == 0) {
                _enemy = new HeavyBoss(scoreP);
            }
            else if (typeSelection == 1) {
                _enemy = new HealerBoss(scoreP);
            }
            else {
                _enemy = new HeavyBoss(scoreP);
            }
        }
        else {
            if (typeSelection == 0) {
                _enemy = new FireEnemy(scoreP);
            }
            else if (typeSelection == 1) {
                _enemy = new IceEnemy(scoreP);
            }
            else {
                _enemy = new FireEnemy(scoreP);
            }
        }
    }

    // vvv
    private string GetPlayerHealthString() {
        CHString chstring = new CHString();
        int numOfChars = _player.GetHealthFactor();
        string textColor = "";
        if (numOfChars < 15) {
            textColor = chstring.Red();
        }
        else if (numOfChars < 35) {
            textColor = chstring.Yellow();
        }
        else {
            textColor = chstring.Green();
        }
        // return chstring.TextRepeated("X", numOfChars) + chstring.TextRepeated(" ", 50 - numOfChars);
        return $"{textColor}{chstring.TextRepeated("X", numOfChars) + chstring.TextRepeated(" ", 50 - numOfChars)}\u001b[0m";
    }

    private string GetEnemyHealthString() {
        CHString chstring = new CHString();
        int numOfChars = _enemy.GetHealthFactor();
        string textColor = "";
        if (numOfChars < 15) {
            textColor = chstring.Red();
        }
        else if (numOfChars < 35) {
            textColor = chstring.Yellow();
        }
        else {
            textColor = chstring.Green();
        }
        // return chstring.TextRepeated("X", numOfChars) + chstring.TextRepeated(" ", 50 - numOfChars);
        return $"{textColor}{chstring.TextRepeated("X", numOfChars) + chstring.TextRepeated(" ", 50 - numOfChars)}\u001b[0m";
    }

    public string GetEnemyName() { return _enemy.GetName(); }

    public void DisplayBattleScreen() {
        CHString chstring = new CHString();
        Console.Clear();
        Console.WriteLine("[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]");
        Console.WriteLine("[]                                                          []");
        Console.WriteLine("[]  [][][][][][][][][][][][][][][][][][][][][][][][][][][]  []");
        Console.WriteLine("[]  []                                                  []  []");
        Console.WriteLine("[]  [][][][][][][][][][][][][][][][][][][][][][][][][][][]  []");
        Console.WriteLine("[]                                                          []");
        Console.WriteLine("[]                      RRRR      RRRR                      []".Replace("RR", chstring.Red("[]")));
        Console.WriteLine("[]                      RR  RRRRRR  RR                      []".Replace("RR", chstring.Red("[]")));
        Console.WriteLine("[]                      RR    RR    RR                      []".Replace("RR", chstring.Red("[]")));
        Console.WriteLine("[]                      RRRRRRRRRRRRRR                      []".Replace("RR", chstring.Red("[]")));
        Console.WriteLine("[]                        RR      RR                        []".Replace("RR", chstring.Red("[]")));
        Console.WriteLine("[]                          RRRRRR                          []".Replace("RR", chstring.Red("[]")));
        Console.WriteLine("[]                                                          []");
        Console.WriteLine("[]                                                          []");
        Console.WriteLine("[]                                                          []");
        Console.WriteLine("[]  [][][][][][][][][][][][][][][][][][][][][][][][][][][]  []");
        Console.WriteLine("[]  []                                                  []  []");
        Console.WriteLine("[]  [][][][][][][][][][][][][][][][][][][][][][][][][][][]  []");
        Console.WriteLine("[]  []                        []                        []  []");
        Console.WriteLine("[]  []                        []                        []  []");
        Console.WriteLine("[]  []                        []                        []  []");
        Console.WriteLine("[]  [][][][][][][][][][][][][][][][][][][][][][][][][][][]  []");
        Console.WriteLine("[]                                                          []");
        Console.WriteLine("[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]");
        Console.WriteLine();
        Console.Write("");
    }
    // ^^^

    // vvv
    private Boolean BattleIsActive() {
        if (_player.IsAlive() && _enemy.IsAlive()) {
            return true;
        }
        else {
            return false;
        }
    }

    public void EngageInBattle() {
        DisplayBattleScreen();
        UpdateHealthBars();
        while (BattleIsActive()) {
            PlayerDoesTurn();
            if (_enemy.IsAlive()) {
                EnemyDoesTurn();
            }
            if (_player.IsBurned()) {
                UpdateBattleMessage($"{_player.GetName()} is burned!");
                Thread.Sleep(750);
                _player.GetsBurned();
            }
            if (_player.IsFrozen()) {
                UpdateBattleMessage($"{_player.GetName()}'S defense is lower because of frostbite!");
                Thread.Sleep(750);
            }
        }
    }
    // ^^^

    private void UpdateHealthBars() {

        CHString chstring = new CHString();

        Console.CursorTop = 3;
        Console.CursorLeft = 0;
        Console.Write("[]  []                                                  []  []");
        Console.CursorLeft = 6;
        chstring.SlowPrint(GetEnemyHealthString(), printSpeed: 20);

        Console.CursorTop = 16;
        Console.CursorLeft = 0;
        Console.Write("[]  []                                                  []  []");
        Console.CursorLeft = 6;
        chstring.SlowPrint(GetPlayerHealthString(), printSpeed: 20);
    }

    private void UpdateBattleMessage(string messageP) {
        CHString chstring = new CHString();
        Console.CursorTop = 13;
        Console.CursorLeft = 0;
        Console.Write("[]                                                          []");
        Console.CursorLeft = 7;
        chstring.SlowPrint(messageP);
    }

    private void EnemyDoesTurn() {
        UpdateBattleMessage($"The {_enemy.GetName()} attacks!");
        _player.ReceivesDamage(_enemy.Attack());
        _player.SetStatuses(_enemy.DoStatusAffect(_player.GetStatuses()));
        UpdateHealthBars();
    }

    private void PlayerDoesTurn() {

        string user = "HOME";
 
        Boolean decisionIsNotMade = true;
        while (decisionIsNotMade) {
            if (user == "HOME") {
                user = GetUserChoice([["1", "ATTACK"], ["2", "USE AN ITEM"]], ["", "  1. ATTACK", "", "", "  2. USE AN ITEM", ""]);
            }
            else if (user == "USE AN ITEM") {
                user = GetUserChoice(_player.GetItemValidReturnList(), _player.GetItemChoiceBoxList());
            }
            else {
                decisionIsNotMade = false;
            }
        }

        if (user == "ATTACK") {
            UpdateBattleMessage($"{_player.GetName()} attacks!");
            _enemy.ReceivesDamage(_player.DealsDamage());
        }
        else {
            int itemIndex = Int32.Parse(user) - 1;
            List<Item> playersItems = _player.GetItems();
            if (playersItems[itemIndex] is HealthPotion) {
                UpdateBattleMessage($"{_player.GetName()} uses a HEALTH POTION!");
                _player.ReceivesDamage(playersItems[itemIndex].ReturnValue());
                _player.RemoveItemAt(itemIndex);
            }
            else if (playersItems[itemIndex] is BurnCure) {
                UpdateBattleMessage($"{_player.GetName()} uses a BURN CURE!");
                _player.SetBurnStatus(false);
                _player.RemoveItemAt(itemIndex);
                UpdateBattleMessage($"{_player.GetName()} is no longer burning!");
            }
            else if (playersItems[itemIndex] is FrostbiteCure) {
                UpdateBattleMessage($"{_player.GetName()} uses a FROSTBITE CURE!");
                _player.SetFrostStatus(false);
                _player.RemoveItemAt(itemIndex);
                UpdateBattleMessage($"{_player.GetName()} is no longer frostbitten!");
            }
            // _player.
            // FIX THIS!!!
        }

        UpdateHealthBars();
    }

    private void CursorLT(int leftP, int topP) {
        Console.CursorLeft = leftP;
        Console.CursorTop = topP;
    }

    public void UpdateChoiceBox(List<string> stringList) {
        CHString chstring = new CHString();
        CursorLT(6, 18);
        Console.Write(chstring.LeftAligned(stringList[0], 24));
        CursorLT(6, 19);
        Console.Write(chstring.LeftAligned(stringList[1], 24));
        CursorLT(6, 20);
        Console.Write(chstring.LeftAligned(stringList[2], 24));
        CursorLT(32, 18);
        Console.Write(chstring.LeftAligned(stringList[3], 24));
        CursorLT(32, 19);
        Console.Write(chstring.LeftAligned(stringList[4], 24));
        CursorLT(32, 20);
        Console.Write(chstring.LeftAligned(stringList[5], 24));
    }

    public string GetUserChoice(List<List<string>> validReturnList, List<string> choiceBoxList) {
        
        Boolean IsNotValidAnswer(string param) {

            Boolean outBool = true;

            foreach (List<string> pair in validReturnList) {
                if (param == pair[0]) {
                    outBool = false;
                }
            }

            return outBool;

        }

        string outVal;

        UpdateChoiceBox(choiceBoxList);

        UpdateBattleMessage($"What will {_player.GetName()} do? ");
        outVal = Console.ReadLine();

        while (IsNotValidAnswer(outVal)) {
            UpdateBattleMessage($"What will {_player.GetName()} do? ");
            outVal = Console.ReadLine();
        }

        foreach (List<string> pair in validReturnList) {
            if (outVal == pair[0]) {
                outVal = pair[1];
                break;
            }
        }

        return outVal;

    }

    public string GetDroppedItem() {
        Item droppedItem = _enemy.DropItem();
        _player.GetItem(droppedItem);
        return droppedItem.GetName();
    }

}