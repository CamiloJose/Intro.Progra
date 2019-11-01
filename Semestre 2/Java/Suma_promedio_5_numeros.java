/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package triangulo;

/**
 *
 * @author user
 */
public class Suma_promedio_5_numeros {

    public static void main(String[] args) {
        int prim, segu, terc, cuart, quint, suma, promed;
        String n;
        
        n = javax.swing.JOptionPane.showInputDialog("Primero");
        prim = Integer.parseInt(n);
        
        n = javax.swing.JOptionPane.showInputDialog("Segundo");
        segu = Integer.parseInt(n);
        
        n = javax.swing.JOptionPane.showInputDialog("Tercero");
        terc = Integer.parseInt(n);
        
        n = javax.swing.JOptionPane.showInputDialog("Cuarto");
        cuart = Integer.parseInt(n);
        
        n = javax.swing.JOptionPane.showInputDialog("Quinto");
        quint = Integer.parseInt(n);
        
        suma = prim + segu + terc + cuart + quint;
        promed = ((prim + segu + terc + cuart + quint)/5);
                
        javax.swing.JOptionPane.showMessageDialog(null, "Suma" + ":" + suma);
        javax.swing.JOptionPane.showMessageDialog(null, "Promedio" + ":" + promed);
    }
    
}