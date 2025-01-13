using System;

class DanceEnemy : NormEnemy {

    public DanceEnemy(int score) : base(score) {
        List<string> posNames = ["Dancing Specter", "Twilight Dancer", "Waltz Phantom", "Rhythm Reaper"];
        Random rand = new Random();
        _name = posNames[rand.Next(0, 4)];
    }

    public override List<Boolean> DoStatusAffect(List<Boolean> playerCurrentStatuses) {
        List<Boolean> outLoB = playerCurrentStatuses;
        Random rand = new Random();
        int val = rand.Next(0, 5);
        if (val == 4) {
            if (outLoB[0] && !outLoB[1]) {
                outLoB[0] = true;
                outLoB[1] = false;
            }
            else if (outLoB[1] && !outLoB[0]) {
                outLoB[1] = true;
                outLoB[0] = false;
            }
        }
        return outLoB;
    }

}
