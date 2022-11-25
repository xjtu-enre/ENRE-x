/**
 * @author darkFernMoss
 * since 2022/11/10
 * at project JNI2
 */
public class MethodWithParams {
    public static native int f1(int a, int b);

    static {
        System.loadLibrary("JNI2");
    }

    public static void main(String[] args) {
        System.out.println(f1(13,32));
    }

}
