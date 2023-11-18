package rubrica;

import java.util.ArrayList;

public class Rubrica {
	
	private static int numRubriche;
	private static int max_dim_default;
	private static String nome_default;
	public final String NOME;
	private ArrayList<Contatto> rubrica;
	public final int MAX_DIM;
	
	static {
		numRubriche = 0;
		nome_default = "Rubrica ";
		max_dim_default = 6;
	}
	
	{
		numRubriche += 1; 
		rubrica = new ArrayList<Contatto>();
	}
	
	public Rubrica(String nome, int maxDim){
		NOME = nome;
		MAX_DIM = maxDim;	
	}
	
	public Rubrica(){
		this(nome_default + (numRubriche + 1), max_dim_default);

	}
	
	public Rubrica(String nome){
		this(nome, max_dim_default);
	}
	
	public Rubrica(int maxDim) {
		this(nome_default + (numRubriche + 1), maxDim);
	}
	
	public static int getNumRubriche() {
		return numRubriche;
	}
	
	public ArrayList<Contatto> getRubrica() {
		return rubrica;
	}
	
	public int numEl() {
		return rubrica.size();
	}
	
	public boolean aggiungi(Contatto c) {
		if (!(rubrica.contains(c)) && this.numEl() < MAX_DIM){
			rubrica.add(c);
			return true;
		}
		
		return false;
	}
	
	public boolean aggiungi(String email, String nome) {
		
		return aggiungi(new Contatto(nome, email));
	}
	
	public boolean aggiungi(String email) {
		return aggiungi(new Contatto(email));
	}
	
	// to do cerca per nome e per email
	public ArrayList<Contatto> cercaPerNome(String nome) {
		ArrayList<Contatto> c_cercati = new ArrayList<Contatto>();
		
		for (Contatto c_rubrica: rubrica) {
			if (c_rubrica.matchNome(nome)) {
				c_cercati.add(c_rubrica);
			}
		}
		return c_cercati;
	}

	public ArrayList<Contatto> cercaPerEmail(String email) {
		ArrayList<Contatto> c_cercati = new ArrayList<Contatto>();
		
		for (Contatto c_rubrica: rubrica) {
			if (c_rubrica.matchEmail(email)) {
				c_cercati.add(c_rubrica);
			}
		}
		return c_cercati;
	}
	
	public boolean eliminaPerNome(String nome) {
		return rubrica.removeAll(cercaPerNome(nome));
	}
	public boolean eliminaPerEmail(String email) {
		// TODO Auto-generated method stub
		return rubrica.removeAll(cercaPerEmail(email));
	}
	
	@Override
	public String toString() {
		return "";
	}







}
