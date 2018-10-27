package Q2;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Q2Mapper extends Mapper<LongWritable, Text, Text, FloatWritable> {

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, FloatWritable>.Context context)
			throws IOException, InterruptedException {
		float peopleCount = 0.0f;
		String [] inputValues = value.toString().split(",");
		try {
			peopleCount=Float.parseFloat(inputValues[9])+Float.parseFloat(inputValues[inputValues.length-11]);
		}
		catch(Exception e) {}
		context.write(new Text(inputValues[4]),new FloatWritable(peopleCount));
	}
}