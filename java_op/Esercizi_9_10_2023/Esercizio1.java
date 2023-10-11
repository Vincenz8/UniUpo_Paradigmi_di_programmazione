import jbook.util.Input;

public class Esercizio1{
    public static void main(String[] args){
        
        float temperatura;

        temperatura = Input.readFloat("Inserisci temperatura in Fahreneheit: ");
        temperatura = (5 * (temperatura - 32)) / 9;

        System.out.print("Temperatura in Celsius: " + temperatura);
    }
}