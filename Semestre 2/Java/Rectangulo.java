/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package triangulo;

public class Rectangulo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int base, altura, area, perim;
        String n;
        
        n = javax.swing.JOptionPane.showInputDialog("base");
        base = Integer.parseInt(n);
        
        n = javax.swing.JOptionPane.showInputDialog("Altura");
        altura = Integer.parseInt(n);
        
        area= base * altura;
        perim= (base + altura)*2;
        
        javax.swing.JOptionPane.showMessageDialog(null, "Area del rectangulo" + ":" + area);
        javax.swing.JOptionPane.showMessageDialog(null, "Perim del rectangulo" + ":" + perim);
    }
    
}