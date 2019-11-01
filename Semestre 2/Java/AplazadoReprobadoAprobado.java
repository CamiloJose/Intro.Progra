/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package triangulo;


public class AplazadoReprobadoAprobado {

    public static void main(String[] args) {
        int nota;
        String n;
        
        n = javax.swing.JOptionPane.showInputDialog("nota");
        nota = Integer.parseInt(n);
        
        if(nota < 70){
            if (nota>=60){
                javax.swing.JOptionPane.showMessageDialog(null, "aplazado");
            }
        }
        else{
            javax.swing.JOptionPane.showMessageDialog(null, "Aprobado");
        }
   }
}