using System.Net;

abstract class NormEnemy : Enemy {

    protected int _enemyDifficulty;

    public NormEnemy(int score) {
        _enemyDifficulty = score;
        _maxHp = 200 + (score * 50);
        _hp = _maxHp;
    }

    public override int Attack() {
        Random rand = new Random();
        int damage = rand.Next(_enemyDifficulty * 50, (_enemyDifficulty + 1) * 50);
        return damage;
    }

    public override Item DropItem() {
        Random rand = new Random();
        int index = rand.Next(0, 3);
        List<Item> posItems = [new BurnCure("BURN CURE"), new FrostbiteCure("FROSTBITE CURE")];
        if (_enemyDifficulty < 1) {
            posItems.Add(new HealthPotion("HEALTH POTION", 50));
        }
        else {
            posItems.Add(new HealthPotion("HEALTH POTION", _enemyDifficulty * 50));
        }
        Item item = posItems[index];
        return item;
    }

}
