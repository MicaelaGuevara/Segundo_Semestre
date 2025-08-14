package Clase_1;

public class Ciclo_Do_while {
     public static void main(String[] args) {
        var conteo = 0;
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);
    }
}
        
    