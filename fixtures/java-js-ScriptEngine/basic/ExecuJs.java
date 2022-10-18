import java.io.FileReader;
import java.util.Scanner;
import javax.script.Bindings;
import javax.script.Invocable;
import javax.script.ScriptContext;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class ExecuJs {
    public static void main(String[] args) throws Exception {

        // get JS ScriptEngine
        ScriptEngine se = new ScriptEngineManager().getEngineByName("javascript");
        // get variate
        Bindings bindings = se.createBindings();
        bindings.put("number", 3);
        se.setBindings(bindings, ScriptContext.ENGINE_SCOPE);
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println("input parameter【" + a + "】 + 【" + b + "】");
            se.eval(new FileReader("D:\\project\\java\\demo\\src\\add.js"));
            // call or not
            if (se instanceof Invocable) {
                Invocable in = (Invocable) se;
                double result = (double) in.invokeFunction("add", a, b);
                System.out.println("result：" + result);

            }

        }

    }
}
