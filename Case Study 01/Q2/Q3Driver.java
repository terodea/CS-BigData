package Q2;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class Q3Driver {
	public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
		//Step 1: Create a job
		Configuration conf = new Configuration();
		Job job =  Job.getInstance(conf,"Find Maximum Attend");
		
		//Step 2: Set the components
		job.setJarByClass(Q3Driver.class);
		job.setMapperClass(Q2Mapper.class);
		job.setReducerClass(Q2Reducer.class);
		
		//Step 3: Set the key-value class
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(FloatWritable.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(FloatWritable.class);
		
		//Step 4: Set input and output path
		Path inputPath = new Path("/",new Path("SSA-SA-FYWL.csv"));
		Path outputPath = new Path("/",new Path("AssignmentQ1"));
		
		//Step 5 : Assign the files to the job
		FileInputFormat.addInputPath(job, inputPath);
		FileOutputFormat.setOutputPath(job,outputPath);
		
		//Step 6 : Set the input/output formats
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		
		//Step 6 : Submit the job
		System.exit(job.waitForCompletion(true)?0:1);
	}
}