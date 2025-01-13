// FireEnemy.cs

using System;

class FireEnemy : NormEnemy {

    public FireEnemy(int score) : base(score) {
        List<string> posNames = ["Blazing Inferno", "Flame Warden", "Ember Spirit", "Inferno Beast"];
        Random rand = new Random();
        _name = posNames[rand.Next(0, 4)];
    }

    public override List<Boolean> DoStatusAffect(List<Boolean> playerCurrentStatuses) {
        List<Boolean> outLoB = playerCurrentStatuses;
        Random rand = new Random();
        int val = rand.Next(0, 5);
        if (val == 4) {
            outLoB[0] = true;
        }
        return outLoB;
    }

}
