/**
 * @author darkFernMoss
 * since 2022/11/14
 * at project JNI3
 */
public class PersonMethod {

    static {
        System.loadLibrary("PersonMethod");
    }

    native void native_init();

    private String mName;

    public PersonMethod() {
        native_init();
    }

    public void setName(String name) {
        mName = name;
    }

    @Override
    public String toString() {
        return "PersonMethod{" +
                "mName='" + mName + '\'' +
                '}';
    }

    public static void main(String[] args) {
        System.out.println(new PersonMethod());
    }
}
