public class Person
{
    private String name;
    private String surname;
    private int age;
    private Address address;

    public Person()
    {
        name="";
        surname="";
        age=0;
        address=null;
    }

    public Person(String name, String surname,int age,Address address)
    {
        this.name=name;
        this.surname=surname;
        this.age=age;
        this.address=address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return name+" "+surname+" "+age+" "+address;
    }
}
