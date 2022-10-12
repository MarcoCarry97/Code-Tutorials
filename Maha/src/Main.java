public class Main {


    public static void main(String[] args)
    {
        Address address=new Address("Via Tortona",15,"Tortona");
        Person person=new Person("Carlo","Rossi",34,address);
        System.out.println("Person: "+person.toString());
        //person.setName("Carlo");
        //person.setSurname("Rossi");
        address.setCity("Alessandria");
        System.out.println("Person: "+person);
    }
}
