package test;

import org.junit.jupiter.api.Test;
import rubrica.Contatto;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class ContattoTest {
    @Test
    void creaContatto2Param() {
        Contatto c1 = new Contatto("Bobby", "fischer@outlook.com");
        assertEquals("Bobby", c1.getNome());
        assertEquals("fischer@outlook.com", c1.getEmail());
        assertEquals(0, c1.getNumeriTel().size());
    }

    @Test
    void creaContatto1Param() {
        Contatto c1 = new Contatto("kasparov@gmail.com");
        assertEquals("", c1.getNome());
        assertEquals("kasparov@gmail.com", c1.getEmail());
        assertEquals(0, c1.getNumeriTel().size());
    }

    @Test
    void setNome() {
        Contatto c1 = new Contatto("Hari", "seldon@gmail.com");
        c1.setNome("Mule");
        assertEquals("Mule", c1.getNome());
    }

    @Test
    void inserisciNumTel() {
        Contatto c1 = new Contatto("Grothendieck", "alexander@gmail.com");
        c1.inserisciNumTel("1234567892");

        ArrayList<String> numeriTel;
        numeriTel = c1.getNumeriTel();
        assertEquals(1, numeriTel.size());
        assertEquals("1234567892", numeriTel.get(0));
    }

    @Test
    void inserisciNumTelPresente() {
        Contatto c1 = new Contatto("Grigorij", "perelman@gmail.com");
        c1.inserisciNumTel("1234567892");
        assertFalse(c1.inserisciNumTel("1234567892"));
        assertEquals(1, c1.getNumeriTel().size());
    }

    @Test
    void eliminaNumTel() {
        Contatto c1 = new Contatto("Ajeje", "brazorf@gmail.com");
        c1.inserisciNumTel("1234567892");
        assertTrue(c1.eliminaNumTel("1234567892"));
        assertEquals(0, c1.getNumeriTel().size());
    }

    @Test
    void eliminaNumTelNonPresente() {
        Contatto c1 = new Contatto("Gastani", "frinzi@gmail.com");
        assertFalse(c1.eliminaNumTel("1234567892"));
        assertEquals(0, c1.getNumeriTel().size());
    }

    @Test
    void matchNomeCorretto(){
        Contatto c1 = new Contatto("Carlo", "musmarra@gmail.com");
        assertTrue(c1.matchNome("Car"));

    }

    @Test
    void matchNomeErrato(){
        Contatto c1 = new Contatto("Carlo", "musmarra@gmail.com");
        assertFalse(c1.matchNome("one"));

    }
    @Test
    void matchEmailCorretto(){
        Contatto c1 = new Contatto("Carlo", "musmarra@gmail.com");
        assertTrue(c1.matchEmail("ra@g"));
    }

    @Test
    void matchEmailErrato(){
        Contatto c1 = new Contatto("Carlo", "musmarra@gmail.com");
        assertFalse(c1.matchEmail("one"));

    }
    @Test
    void equalsContattoUguale() {
        Contatto c1 = new Contatto("Jak", "dexter@gmail.com");
        Contatto c2 = new Contatto("sfera", "dexter@gmail.com");
        assertEquals(c1, c2);
    }

    @Test
    void equalsContattoDiverso() {
        Contatto c1 = new Contatto("Jak", "dexter@gmail.com");
        Contatto c2 = new Contatto("Ratchet", "clank@gmail.com");
        assertNotEquals(c1, c2);
    }

    @Test
    void equalsOggettoDiverso() {
        Contatto c1 = new Contatto("Lilo", "stitch@gmail.com");
        assertNotEquals(42, c1);
    }

}