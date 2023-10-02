package pkg651arreglos;


public class Pkg651arreglos {

    public static void main(String[] args) {
        //problema escribir un programa para insertar el numero de episodios de una serie y nos devuelva la duración
        System.out.println("*************************");
        System.out.println("****Serie de DR House****");
        System.out.println("*************************");
        int[] episodioSerie = new int [5];
        
        episodioSerie[0] = 30;
        episodioSerie[1] = 50;
        episodioSerie[2] = 25;
        episodioSerie[3] = 60;
        episodioSerie[4] = 45;
        //numero de episodios
        //int duracion = episodioSerie.length;
       int acumulador = 0;
        for (int i = 0; i < episodioSerie.length; i++) {
           acumulador = acumulador + episodioSerie[i];
       } 
        System.out.println ("Duracion total de la serie:" + acumulador);
        
        System.out.println("Episodios con duración mayor a 40 minutos:");
        for (int i = 0; i < episodioSerie.length; i++) {
            if (episodioSerie[i] > 40) {
                System.out.println("Episodio " + (i + 1) + ": " + episodioSerie[i] + " minutos");
            }
        }
    }
}