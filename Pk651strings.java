package pk651strings;

public class Pk651strings {

    public static void main(String[] args) {
    String cadenaTexto = "El neto es puto";
    System.out.println("Cadena Original: " + cadenaTexto);
    System.out.println("La longitud de la cadena es: " + cadenaTexto.length());
    System.out.println("La primera letra de la cadena: " + cadenaTexto.charAt(0));
    
    int ultimaLetra = (cadenaTexto.length()) -1;
    System.out.println("La ultima letra de la cadena: " + cadenaTexto.charAt(ultimaLetra));
        System.out.println("Valor de la subcadena: " + cadenaTexto.substring(1,3));
        
        String cadena1 = "Hola";
        String cadena2 = "hola";
        String mayusculasC1 = cadena1.toUpperCase();
        String mayusculasC2 = cadena2.toUpperCase();
        System.out.println("La cadena 1 es igual a la cadena2?: "+ mayusculasC1.equals(mayusculasC2));
    }  
}
