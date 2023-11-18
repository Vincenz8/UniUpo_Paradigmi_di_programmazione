package rubrica;

import java.util.ArrayList;

public class Contatto {
    private String nome;
    private String email;
    private ArrayList<String> numeriTel;

    {
        numeriTel = new ArrayList<>();
    }


    public Contatto(String nome, String email) {
        this.setNome(nome);
        this.email = email;
    }

    public Contatto(String email) {
        this("", email);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public ArrayList<String> getNumeriTel() {
        return numeriTel;
    }

    public boolean inserisciNumTel(String num) {
        if (num.length() == 10) {
            if (!numeriTel.contains(num)) {
                numeriTel.add(num);
                return true;
            }

        }
        return false;
    }

    public boolean eliminaNumTel(String num) {
        if (numeriTel.contains(num)) {
            numeriTel.remove(num);
            return true;
        }
        else {
            return false;
        }
    }

    public String numTel() {
        return numeriTel.toString();
    }

    public boolean matchNome(String str) {
        return nome.contains(str);
    }

    public boolean matchEmail(String str) {
        return email.contains(str);
    }

    @Override
    public String toString() {
        return "Nome: " + nome + "\nEmail: " + email + "\nNumeri" + numTel();
    }

    @Override
    public boolean equals(Object contatto) {
        if (contatto instanceof Contatto) {
            return this.email.equals(((Contatto) contatto).getEmail());
        }
        return false;
    }
}
