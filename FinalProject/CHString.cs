using System.ComponentModel.Design;

class CHString {

    // MEMBER VARIABLES / ATTRIBUTES

    // MEMBER METHODS / FUNCTIONS / BEHAVIORS

        // CONSTRUCTORS ( METHODS )

        // GETTERS / ACCESSORS ( METHODS )

        // SETTERS / MUTATORS ( METHODS )

        // OTHER METHODS

    public string TextRepeated(string text, int repetitions) {
        string outStr = "";
        for (int i = 0; i < repetitions; i ++) {
            outStr = outStr + text;
        }
        return outStr;
    }

    public string CenterAligned(string text, int totalLength) {
        int lPad = (totalLength - text.Count()) / 2;
        int rPad = (totalLength - text.Count()) - lPad;
        return $"{TextRepeated(" ", lPad)}{text}{TextRepeated(" ", rPad)}";
    }

    public string LeftAligned(string text, int totalLength) {
        int rPad = (totalLength - text.Count());
        return $"{text}{TextRepeated(" ", rPad)}";
    }

    public void SlowPrint(string text, int printSpeed = 25) {
        for (int i = 0; i < text.Count(); i ++) {
            Console.Write(text[i]);
            Thread.Sleep(printSpeed);
        }
    }

    public string ResetColor() { return "\u001b[0m"; }
    public string Red() { return "\u001b[91m"; }
    public string Red(string text) {
        return $"\u001b[91m{text}\u001b[0m";
    }
    public string DarkGrey(string text) {
        return $"\u001b[90m{text}\u001b[0m";
    }
    public string Green() { return "\u001B[32m"; }
    public string Yellow() { return "\u001B[93m"; }

}
