package test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;

import org.junit.jupiter.api.Test;

import rubrica.Contatto;
import rubrica.Rubrica;

class RubricaTest {

	@Test
	void testCostruttoredefault() {
		Rubrica rubricaTest = new Rubrica();
		assertEquals("Rubrica " + Rubrica.getNumRubriche(), rubricaTest.NOME);
		assertEquals(6, rubricaTest.MAX_DIM);
	}
	
	@Test
	void testCostruttoreTuttiParametri() {
		Rubrica rubricaTest = new Rubrica("Capablanca", 42);
		assertEquals("Capablanca", rubricaTest.NOME);
		assertEquals(42, rubricaTest.MAX_DIM);		
	}
	
	@Test
	void testCostruttoreMaxDim() {
		Rubrica rubricaTest = new Rubrica(42);
		assertEquals("Rubrica " + Rubrica.getNumRubriche(), rubricaTest.NOME);
		assertEquals(42, rubricaTest.MAX_DIM);		
	}
	
	@Test
	void testCostruttoreNome() {
		Rubrica rubricaTest = new Rubrica("Avengers");
		assertEquals("Avengers", rubricaTest.NOME);
		assertEquals(6, rubricaTest.MAX_DIM);		
	}
	
	@Test
	void aggiungiContatto() {
		Rubrica rubrica = new Rubrica("Power Rangers", 7);
		Contatto c1 = new Contatto("Red Ranger", "rosso@outlook.com");
		assertEquals(true, rubrica.aggiungi(c1));
		assertEquals(1, rubrica.numEl());
	}
	
	@Test
	void aggiungiContattoNomeEmail() {
		Rubrica rubrica = new Rubrica("Power Rangers", 7);
		assertEquals(true, rubrica.aggiungi("rosso@outlook.com", "Red Ranger"));
		assertEquals(1, rubrica.numEl());
	}
	
	@Test
	void aggiungiContattoEmail() {
		Rubrica rubrica = new Rubrica("Power Rangers", 7);
		assertEquals(true, rubrica.aggiungi("rosso@outlook.com"));
		assertEquals(1, rubrica.numEl());
	}
	
	@Test
	void aggiungiContattoPresente() {
		Rubrica rubrica = new Rubrica("Power Rangers", 7);
		rubrica.aggiungi("nero@outlook.com");
		assertEquals(false, rubrica.aggiungi("nero@outlook.com"));
		assertEquals(1, rubrica.numEl());
	}
	
	@Test
	void aggiungiContattoRubricaPiena() {
		Rubrica rubrica = new Rubrica("Superchicche", 3);
		String[] emailSuperChicche = {"lolly@outlook.com", "dolly@outlook.com", "molly@outlook.com"};
		
		for (String email: emailSuperChicche) {
			rubrica.aggiungi(email);
		}
		
		assertEquals(false, rubrica.aggiungi("ollie@outlook.com"));
		assertEquals(3, rubrica.numEl());
	}
	
	@Test
	void cercaPerNomePresenti() {
		Rubrica superChicche = new Rubrica("Superchicche", 3);
		String[] emailSuperChicche = {"lolly@outlook.com", "dolly@outlook.com", "molly@outlook.com"};
		
		for (String email: emailSuperChicche) {
			superChicche.aggiungi(email, email.substring(0, 5));
		}
		
		ArrayList<Contatto> sc_cercate = superChicche.cercaPerNome("olly");
		assertEquals(3, sc_cercate.size());
		
		for (Contatto superChicca: superChicche.getRubrica()) {
			assertEquals(true, sc_cercate.contains(superChicca));
		}
	}
	
	@Test
	void cercaPerNomeAssenti() {
		Rubrica superChicche = new Rubrica("Superchicche", 3);
		String[] emailSuperChicche = {"lolly@outlook.com", "dolly@outlook.com", "molly@outlook.com"};
		
		for (String email: emailSuperChicche) {
			superChicche.aggiungi(email, email.substring(0, 5));
		}
		
		ArrayList<Contatto> sc_cercate = superChicche.cercaPerNome("frank");
		assertEquals(0, sc_cercate.size());
	}
	
	@Test
	void cercaPerEmailPresenti() {
		Rubrica superChicche = new Rubrica("Superchicche", 3);
		String[] emailSuperChicche = {"lolly@outlook.com", "dolly@outlook.com", "molly@outlook.com"};
		
		for (String email: emailSuperChicche) {
			superChicche.aggiungi(email);
		}
		
		ArrayList<Contatto> sc_cercate = superChicche.cercaPerEmail("olly");
		assertEquals(3, sc_cercate.size());
		
		for (Contatto superChicca: superChicche.getRubrica()) {
			assertEquals(true, sc_cercate.contains(superChicca));
		}
	}
	
	@Test
	void cercaPerEmailAssenti() {
		Rubrica superChicche = new Rubrica("Superchicche", 3);
		String[] emailSuperChicche = {"lolly@outlook.com", "dolly@outlook.com", "molly@outlook.com"};
		
		for (String email: emailSuperChicche) {
			superChicche.aggiungi(email);
		}
		
		ArrayList<Contatto> sc_cercate = superChicche.cercaPerEmail("frank");
		assertEquals(0, sc_cercate.size());
	}
	
	@Test
	void eliminaPerNome() {
		Rubrica superChicche = new Rubrica("Superchicche", 3);
		String[] emailSuperChicche = {"lolly@outlook.com", "dolly@outlook.com", "molly@outlook.com"};
		
		for (String email: emailSuperChicche) {
			superChicche.aggiungi(email, email.substring(0, 5));
		}
		
		assertEquals(true, superChicche.eliminaPerNome("olly"));
		assertEquals(0, superChicche.numEl());
	}
	
	@Test
	void eliminaPerEmail() {
		Rubrica superChicche = new Rubrica("Superchicche", 3);
		String[] emailSuperChicche = {"lolly@outlook.com", "dolly@outlook.com", "molly@outlook.com"};
		
		for (String email: emailSuperChicche) {
			superChicche.aggiungi(email, email.substring(0, 5));
		}
		
		assertEquals(true, superChicche.eliminaPerEmail("olly"));
		assertEquals(0, superChicche.numEl());
	}
	
	
	
	
	
	
}
