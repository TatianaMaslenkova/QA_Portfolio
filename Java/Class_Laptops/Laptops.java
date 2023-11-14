/*
 * Подумать над структурой класса Ноутбук для магазина техники - выделить поля и методы. 
 * Реализовать в java. Создать множество ноутбуков.
 */
package HW_6_Final;
public class Laptops {
    private int id;
    private String brand;
    private String model;
    private String cpu;
    private double screenDiagonal;
    private int ram;
    private int ssdCapacity;
    private String os;
    private String color;
    private int price;

    public Laptops(int id, String brand, String model, String cpu, double screenDiagonal, int ram, 
    int ssdCapacity, String os, String color, int price) {
        this.id = id;
        this.brand = brand;
        this.model = model;
        this.cpu = cpu;
        this.screenDiagonal = screenDiagonal;
        this.ram = ram;
        this.ssdCapacity = ssdCapacity;
        this.os = os;
        this.color = color;
        this.price = price;
    }

    @Override
    public String toString() {
        return "ID: " + this.id + ", " + "Brand: " + this.brand + ", " + "Model: " + this.model + ", " + "CPU: " + this.cpu + ", " 
        + "Screen Diagonal" + this.screenDiagonal + ", " + "RAM: " + this.ram + ", " + "SSD:" + this.ssdCapacity + ", " 
        + "OS: " + this.os + ", " + "Color: " + this.color + ", " + "Price: " + this.price + ".";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Laptops) {
            return this.brand.equals(((Laptops) obj).brand)
            && this.model.equals(((Laptops) obj).model) && this.cpu.equals(((Laptops) obj).cpu)
            && this.screenDiagonal == ((Laptops) obj).screenDiagonal && this.ram == ((Laptops) obj).ram 
            && this.ssdCapacity == ((Laptops) obj).ssdCapacity && this.os.equals(((Laptops) obj).os) 
            && this.color.equals(((Laptops) obj).color) && this.price == ((Laptops) obj).price;
        }
        return false;        
    }
    public String getBrand(){
        return this.brand;
    }
    public String getModel(){
        return this.model;
    }
    public String getCpu(){
        return this.cpu;
    }
    public double getScreenDiagonal(){
        return this.screenDiagonal;
    }
    public int getRam(){
        return this.ram;
    }
    public int getSsdCapacity(){
        return this.ssdCapacity;
    }
    public String getOS(){
        return this.os;
    }
    public String getColor(){
        return this.color;
    }
    public int getPrice(){
        return this.price;
    }
}