public class Shape {
    protected Point center;
    protected Shape( Point center ){
        this.center = center;
    }
    public Point getCenter(){
        return center;
    }
    public abstract Rectangle getBounds();
    public abstract void draw( Graphics g );

}

public class Rectangle extends Shape {
    private int h;
    private int w;

    public Rectangle( Point center, int w, int h ){
        super(center);
        this.w = w;
        this.h = h;
    }
    public Rectangle getBounds(){
        return this;
    }
    public int getH(){ return h; }
    public int getW(){ return w; }
    public void draw( Graphics g ){
        // 그리는 코드
    }
}

public class Ellipse extends Shape {
    private int a;
    private int b;

    public Ellipse( Point center, int a, int b ){
        super(center);
        this.a = a;
        this.b = b;
    }

    public Rectangle getBounds() {
        return new Rectangle(center, a*2, b*2);
    }

    // 아래 전개...
}