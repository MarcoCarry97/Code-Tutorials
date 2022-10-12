public class Address {

    private String name;
    private int civicNumber;
    private String city;



    public Address(String name, int civicNumber, String city) {
        this.name = name;
        this.civicNumber = civicNumber;
        this.city = city;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCivicNumber() {
        return civicNumber;
    }

    public void setCivicNumber(int civicNumber) {
        this.civicNumber = civicNumber;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    @Override
    public String toString() {
        return name+" "+civicNumber+" "+city;
    }
}
