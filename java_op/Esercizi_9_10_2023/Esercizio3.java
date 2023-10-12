import jbook.util.Input;

public class Esercizio3 {
    public static void main(String[] args){

        int matrice[][];
        final int RIGHE, COLONNE;
        int i, j;

        RIGHE = 5;
        COLONNE = 3;
        matrice = new int[RIGHE][COLONNE];

        for (i = 0; i < RIGHE; i++){
            for(j = 0; j < COLONNE; j++){
                matrice[i][j] = Input.readInt("Insersci matrice[" + i +"][" + j + "]: ");
            }
        }

        for (i = 0; i < RIGHE; i++){
            for(j = 0; j < COLONNE; j++){
                System.out.print(matrice[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
