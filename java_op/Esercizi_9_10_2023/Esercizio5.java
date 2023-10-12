import jbook.util.Input;

public class Esercizio5 {
    public static void main(String[] args){
        String s1, s2, s3;
        int i;

        s1 = Input.readString("Inserisci stringa: ");
        s2 = "";
        s3 = "";

        for (i = 0; i < s1.length(); i++){

            if ((i % 2) == 0){
                s2 += s1.charAt(i);
            }
            s3 += s1.charAt(s1.length() - (i + 1));
        }


        System.out.println("Stringa senza indici dispari: " + s2);
        System.out.println("Stringa al contrario: " + s3);
    }
}
