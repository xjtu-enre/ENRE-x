/**
 * @author
 * @version 1.0
 */
public class Method {

    public static native void testHello();

    static {
        System.loadLibrary("JNI2");
    }

    public static void main(String[] args) {
        testHello();
    }
}
