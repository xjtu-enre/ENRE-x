import java.io.FileReader;
import javax.script.Invocable;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class ExecuJs {
    public static void main(String[] args) throws Exception {
        ScriptEngine se = new ScriptEngineManager().getEngineByName("javascript");
        se.eval(new FileReader("D:\\project\\java\\demo\\src\\hello.js"));
        Invocable in = (Invocable) se;
        in.invokeFunction("hello");
    }
}
