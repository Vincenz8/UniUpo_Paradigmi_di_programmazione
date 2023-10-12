import jbook.util.Input;

public class Esercizio4 {
    public static void main(String[] args){
        String s, c;

        s = Input.readString("Inserisci stringa: ");
        c = Input.readString("Inserisci carattere: ");

        s = s.replaceAll(c, "?");
        System.out.println("Stringa rimpiazzata: " + s);
    }
}
