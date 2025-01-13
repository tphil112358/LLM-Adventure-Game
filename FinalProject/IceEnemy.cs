// IceEnemy.cs

using System;

class IceEnemy : NormEnemy {

    public IceEnemy(int score) : base(score) {
        List<string> posNames = ["Frozen Specter", "Ice Wraith", "Frost Giant", "Glacial Phantom"];
        Random rand = new Random();
        _name = posNames[rand.Next(0, 4)];
    }

    public override List<Boolean> DoStatusAffect(List<Boolean> playerCurrentStatuses) {
        List<Boolean> outLoB = playerCurrentStatuses;
        Random rand = new Random();
        int val = rand.Next(0, 5);
        if (val == 4) {
            outLoB[1] = true;
        }
        return outLoB;
    }

}
