package Q2;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Q2Reducer extends Reducer<Text, FloatWritable, Text, FloatWritable>{

	protected void reduce(Text arg0, Iterable<FloatWritable> arg1,
			Reducer<Text, FloatWritable, Text, FloatWritable>.Context arg2) throws IOException, InterruptedException {
		float sum= 0.0f;
		for(FloatWritable v: arg1){
			sum += v.get();
		}
		arg2.write(new Text(arg0), new FloatWritable(sum));
	}
}
