import jbook.util.Input;

public class Esercizio2 {

    public static int mcd(int x, int y){
        
        int resto;

        resto = 1;

        while (resto > 0){
            resto = x % y;
            x = x / y;
            y = resto;
        }

        return y;
    }
    public static void main(String[] args){
        
        int x, y;
        int risultato;

        
        x = Input.readInt("Inserisci x: ");
        y = Input.readInt("Inserisci y: ");
        risultato = 0;

        if (x > 0 && y > 0){

            risultato = mcd(x, y);
            System.out.print("MCD: " + risultato);
        }
        else{

            System.out.print("Operazione impossibile");
        }
    }
}
