import java.io.FileReader;
import java.util.Scanner;
import javax.script.Bindings;
import javax.script.Invocable;
import javax.script.ScriptContext;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class ExecuJs {
    public static void main(String[] args) throws Exception {

        // 获取JS执行引擎
        ScriptEngine se = new ScriptEngineManager().getEngineByName("javascript");
        // 获取变量
        Bindings bindings = se.createBindings();
        bindings.put("number", 3);
        se.setBindings(bindings, ScriptContext.ENGINE_SCOPE);
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println("输入的参数【" + a + "】 + 【" + b + "】");
            se.eval(new FileReader("D:\\project\\java\\demo\\src\\add.js"));
            // 是否可调用
            if (se instanceof Invocable) {
                Invocable in = (Invocable) se;
                double result = (double) in.invokeFunction("add", a, b);
                System.out.println("获得的结果：" + result);

            }

        }

    }
}
