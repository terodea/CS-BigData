package Q1;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Q1Reducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable>{

	@Override
	protected void reduce(Text arg0, Iterable<DoubleWritable> arg1,
			Reducer<Text, DoubleWritable, Text, DoubleWritable>.Context arg2) throws IOException, InterruptedException {
		double totalPopulation = 0.0;
		for(DoubleWritable value : arg1) {
			totalPopulation = value.get();
		}
		arg2.write(arg0, new DoubleWritable(totalPopulation));
	}
}