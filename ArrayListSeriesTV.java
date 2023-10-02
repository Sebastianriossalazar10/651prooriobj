import java.util.ArrayList;
public class ArrayListSeriesTV {

    public static void main(String[] args) {
       ArrayList<String> listaSeries = new ArrayList<>();
       listaSeries.add("Braking Bad");
       listaSeries.add("Theoffice");
       listaSeries.add("Friends");
       System.out.println(listaSeries);
       
       listaSeries.remove("Friends");
       System.out.println(listaSeries);

       boolean contaninFriends = listaSeries.contains("Friends");
        System.err.println("La lista contiene a Friends?: " + contaninFriends);
        
        int tamano = listaSeries.size();
        System.out.println("El tamño del Array es: "+ tamano);
        //Declarar diversos tipos de Arrarlist
        ArrayList<Integer> listaInteger = new ArrayList<>();
        ArrayList<Double> listaDouble = new ArrayList<>();
        ArrayList<Boolean> listaBooleanos = new ArrayList<>();
    }
    
}
