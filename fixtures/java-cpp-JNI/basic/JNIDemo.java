/**
 * @author 袁宇浩
 * @version 1.0
 */
public class JNIDemo {

    public static native void testHello();

    static {
        System.loadLibrary("TestJNI");
    }

    public static void main(String[] args) {
        testHello();
    }
}
