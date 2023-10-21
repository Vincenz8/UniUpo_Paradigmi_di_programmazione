import jbook.util.Input;

public class Esercizio {

    public static void main(String[] args){
        String s;

        s = Input.readString("Inserisci mese con iniziale maiuscola(Gennaio, Febbraio, etc): ");

        Mese mese;

        switch (s) {
            case "Gennaio" -> mese = Mese.GENNAIO;
            case "Febbraio" -> mese = Mese.FEBBRAIO;
            case "Marzo" -> mese = Mese.MARZO;
            case "Aprile" -> mese = Mese.APRILE;
            case "Maggio" -> mese = Mese.MAGGIO;
            case "Giugno" -> mese = Mese.GIUGNO;
            case "Luglio" -> mese = Mese.LUGLIO;
            case "Agosto" -> mese = Mese.AGOSTO;
            case "Settembre" -> mese = Mese.SETTEMBRE;
            case "Ottobre" -> mese = Mese.OTTOBRE;
            case "Novembre" -> mese = Mese.NOVEMBRE;
            case "Dicembre" -> mese = Mese.DICEMBRE;
            default -> mese = null;
        }

        if (mese != null) {
            Stagione stagione;

            switch (mese) {
                case SETTEMBRE, OTTOBRE, NOVEMBRE -> stagione = Stagione.AUTUNNO;
                case DICEMBRE, GENNAIO, FEBBRAIO -> stagione = Stagione.INVERNO;
                case MARZO, APRILE, MAGGIO -> stagione = Stagione.PRIMAVERA;
                case GIUGNO, LUGLIO, AGOSTO -> stagione = Stagione.ESTATE;
                default -> stagione = null;
            }
            System.out.println("Mese: " + s);
            System.out.println("Stagione: " + stagione);
        }
        else{
            System.out.print("Non hai inserito il mese correttamente");
        }

    }
}
