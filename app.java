class HelloWorld {
    public static void main(String[] args) {
        int a=0;
        int b=1;
        System.out.println(a); 
        int sum=0;
        while (sum<100) 
        {
        sum=a+b;
        a=b;
        b=sum;
        System.out.println(sum); 
        }

    }
}