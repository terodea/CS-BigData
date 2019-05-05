package Q1;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Q1Mapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		double populationCount = 0.0;
		String [] inputValues = value.toString().split(",");
		try {
			populationCount = Double.parseDouble(inputValues[8]+inputValues[19]);
		}
		catch(NumberFormatException nfe) {
			
		}
		context.write(new Text(inputValues[4]), new DoubleWritable(populationCount));
	}
	
}
