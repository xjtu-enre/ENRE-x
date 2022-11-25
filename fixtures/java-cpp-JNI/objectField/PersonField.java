/**
 * @author darkFernMoss
 * since 2022/11/14
 * at project JNI3
 */
public class PersonField {

    static {
        System.loadLibrary("PersonField");
    }

    native void native_init();

    private int mAge = 10;

    public PersonField() {
        native_init();
    }

    @Override
    public String toString() {
        return "PersonField{" +
                "mAge=" + mAge +
                '}';
    }

    public static void main(String[] args) {
        System.out.println(new PersonField());
    }
}
