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
public class Suma_3_digitos_numero {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int numero, prim, segu, terc, suma;
        String n;
        
        n = javax.swing.JOptionPane.showInputDialog("Numero");
        numero = Integer.parseInt(n);
        if(numero <= 999){
            prim = (numero/100);
            segu = ((numero%100)/10);
            terc = (numero%10);
            
            suma = prim + segu + terc;
            
            javax.swing.JOptionPane.showMessageDialog(null, "Suma digitos Numero" + ":" + suma);
            
        }
        else{
            javax.swing.JOptionPane.showMessageDialog(null, "El numero no es de 3 digitos exactos");
        }  
    }
    
}