using System;

class Program
{
    static void Main(string[] args)
    {
        // IMPORTS
        CHString chstring = new CHString();

        Console.Clear();

        chstring.SlowPrint("\nWhat is the name of your hero? ");
        string heroName = Console.ReadLine().ToUpper();
        Player player = new Player(heroName);

        Combat combat = new Combat(player);

        chstring.SlowPrint($"\nWelcome, {heroName}.  Your journey is just beginning!");
        Thread.Sleep(2000);

        int finalScore = 0;

        while (player.IsAlive()) {

            Console.Clear();
            combat.GetEnemy(finalScore);
            chstring.SlowPrint($"\n{player.GetName()} encounters a {combat.GetEnemyName()}.");
            Thread.Sleep(1000);

            combat.EngageInBattle();
            if (player.IsAlive()) {
                finalScore ++;

                Console.Clear();
                chstring.SlowPrint($"\n{player.GetName()} picked up a {combat.GetDroppedItem()}!");
                if (player.BagIsFull()) {
                    chstring.SlowPrint($"\nBecause {player.GetName()}'S bag was full, they dropped the {player.GetFirstItemName()}!");
                    player.DropItem();
                }
                Thread.Sleep(1000);
            }
        }

        Console.Clear();
        chstring.SlowPrint($"\nYou were SLAIN...\n\nYour final score is {finalScore} enemies defeated.\n\n");
        
    }
}

